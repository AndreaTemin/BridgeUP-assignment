from fastapi import APIRouter
from app.models import WeightUpdate

# from app.models import WeightUpdate
from app.services import (
    get_weights_service,
    update_source_weight_service,
    update_category_weight_service,
    update_campaign_weight_service
)

router = APIRouter()

@router.get("/client/{client_id}/weights")
def get_weights(client_id: str):
    return get_weights_service(client_id)

@router.put("/client/{client_id}/weights/source/{source_name}")
def update_source_weight(client_id: str, source_name: str, weight_update: WeightUpdate):
    print("something in the way it moves")
    return update_source_weight_service(client_id, source_name, weight_update)

@router.put("/client/{client_id}/weights/source/{source_name}/category/{category_name}")
def update_category_weight(client_id: str, source_name: str, category_name: str, weight_update: WeightUpdate):
    return update_category_weight_service(client_id, source_name, category_name, weight_update)

@router.put("/client/{client_id}/weights/source/{source_name}/category/{category_name}/campaign/{campaign_name}")
def update_campaign_weight(client_id: str, source_name: str, category_name: str, campaign_name: str, weight_update: WeightUpdate):
    return update_campaign_weight_service(client_id, source_name, category_name, campaign_name, weight_update)