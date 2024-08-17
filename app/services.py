# app/services.py

from fastapi import HTTPException
from app.costum_error import WeightOutOfRangeException
from app.data import data
from app.models import Source, Category, Campaign, WeightUpdate

def get_weights_service():
    return data

def __validate_weight_update(weight):
    if isinstance(WeightUpdate, weight):
        raise HTTPException(status_code=400, detail="Weight is wrong")
    if not 0 <= weight <= 100:
        raise WeightOutOfRangeException

def update_source_weight_service(source_name: str, weight_update: WeightUpdate):
    if source_name not in data:
        raise HTTPException(status_code=404, detail="Source not found")


    # - The total weight of all sources must be a non-negative number
    # and individual updates should not cause the weight to go below zero, 
    # but this cannot happen if the next point is enforced 
    
    # - The weight (`w`) for any entity should be between 0 and 100.
    __validate_weight_update(weight_update)   

    data[source_name]["w"] = weight_update.w
    return data[source_name]

def update_category_weight_service(source_name: str, category_name: str, weight_update: WeightUpdate):
    if source_name not in data or "categories" not in data[source_name] or category_name not in data[source_name]["categories"]:
        raise HTTPException(status_code=404, detail="Category not found")

    source = Source(**data[source_name])
    category = Category(**source.categories[category_name])

    total_category_weight = sum(c.w for c in source.categories.values()) - category.w + weight_update.w
    if total_category_weight > 100:
        raise HTTPException(status_code=400, detail="Total category weight exceeds 100 within the source")

    category.w = weight_update.w
    data[source_name]["categories"][category_name] = category.model_dump()
    return data[source_name]["categories"][category_name]

def update_campaign_weight_service(source_name: str, category_name: str, campaign_name: str, weight_update: WeightUpdate):
    if source_name not in data or "categories" not in data[source_name] or category_name not in data[source_name]["categories"] or "campaigns" not in data[source_name]["categories"][category_name] or campaign_name not in data[source_name]["categories"][category_name]["campaigns"]:
        raise HTTPException(status_code=404, detail="Campaign not found")

    category = Category(**data[source_name]["categories"][category_name])
    campaign = Campaign(**category.campaigns[campaign_name])

    total_campaign_weight = sum(c.w for c in category.campaigns.values()) - campaign.w + weight_update.w
    if total_campaign_weight != 100:
        raise HTTPException(status_code=400, detail="Total campaign weight must equal 100 within the category")

    campaign.w = weight_update.w
    data[source_name]["categories"][category_name]["campaigns"][campaign_name] = campaign.dict()
    return data[source_name]["categories"][category_name]["campaigns"][campaign_name]
