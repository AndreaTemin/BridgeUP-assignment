
from fastapi import HTTPException
from app.models import Source, Category, Campaign, WeightUpdate
from app.data import get_clients_data

def get_weights_service(client_id: str):
    return get_clients_data(client_id)

def update_source_weight_service(client_id: str, source_name: str, weight_update: WeightUpdate):
    data = get_clients_data(client_id)
    
    if source_name not in data:
        raise HTTPException(status_code=404, detail="Source not found")

    total_weight = sum(s["w"] for s in data.values()) - data[source_name]["w"] + weight_update.w
    if total_weight > 100:
        raise HTTPException(400, "Weight of a source cannot exceed 100")

    data[source_name]["w"] = weight_update.w
    return data[source_name]


def update_category_weight_service(client_id: str, source_name: str, category_name: str, weight_update: WeightUpdate):
    data = get_clients_data(client_id)
    
    if source_name not in data \
        or "categories" not in data[source_name] \
            or category_name not in data[source_name]["categories"]:
        raise HTTPException(status_code=404, detail="Category not found")
    
    current_category = data[source_name]["categories"][category_name]
    
    total_category_weight = \
        sum(category["w"] for category in data[source_name]["categories"].values()) \
        - current_category["w"] + weight_update.w
    
    if total_category_weight > 100:
        raise HTTPException(status_code=400, detail=f"Total category weight exceeds 100 within the source: {source_name}"
        )
    
    current_category["w"] = weight_update.w
    return current_category



def update_campaign_weight_service(client_id: str, source_name: str, category_name: str, campaign_name: str, weight_update: WeightUpdate):
    data = get_clients_data(client_id)

    if source_name not in data \
        or "categories" not in data[source_name] \
            or category_name not in data[source_name]["categories"] \
                or "campaigns" not in data[source_name]["categories"][category_name] \
                    or campaign_name not in data[source_name]["categories"][category_name]["campaigns"]:
        raise HTTPException(status_code=404, detail="Campaign not found")

    current_campaign = data[source_name]["categories"][category_name]["campaigns"][campaign_name]
    current_category = data[source_name]["categories"][category_name]

    total_campaign_weight = sum(campaign["w"] for campaign in current_category["campaigns"].values()) \
                            - current_campaign["w"] + weight_update.w

    if total_campaign_weight != 100:
        raise HTTPException( status_code=400, detail="Total campaign weight must equal 100 within the category")

    current_campaign["w"] = weight_update.w
    return current_campaign
