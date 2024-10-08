import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.data import data

INITIAL_DATA = data.copy()

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_data():
    # Before each test, reset the data to the initial state
    data.clear()
    data.update(INITIAL_DATA)
    

def test_get_weights():
    response = client.get("/client/test/weights")
    assert response.status_code == 200
    assert response.json() == INITIAL_DATA


# Source update
def test_update_source_weight():
    response = client.put("/client/test/weights/source/source-b", json={"w": 80})
    assert response.status_code == 200
    assert response.json()["w"] == 80
    
    # check sum of sources
    assert sum(source['w'] for source in data.values()) <= 100   

def test_update_source_weight_out_of_range_weight():
    # Weight above 100
    response = client.put("/client/test/weights/source/source-b", json={"w": 101})
    assert response.status_code == 400
    assert response.json()["detail"] == "Weight must be between 0 and 100"
  
    # Weight below 0
    response = client.put("/client/test/weights/source/source-b", json={"w": -1})
    assert response.status_code == 400
    assert response.json()["detail"] == "Weight must be between 0 and 100"
    
def test_update_source_weight_source_not_found():
    response = client.put("/client/test/weights/source/source-z", json={"w": 80})
    assert response.status_code == 404
    assert response.json()["detail"] == "Source not found"

def test_update_source_weight_exceeds_total():
    response = client.put("/client/test/weights/source/source-a", json={"w": 90})
    assert response.status_code == 400
    assert response.json()["detail"] == "Total source weight cannot exceed 100"
    

# Category update 
def test_update_category_weight():
    response = client.put("/client/test/weights/source/source-b/category/kitchen-tools", json={"w": 20})
    assert response.status_code == 200
    assert response.json()["w"] == 20

    # check sum of categories
    source = data["source-b"]["categories"]
    assert sum(category['w'] for category in source.values()) <= 100
    

def test_update_category_weight_out_of_range_weight():
    # Weight above 100
    response = client.put("/client/test/weights/source/source-b/category/kitchen-tools", json={"w": 101})
    assert response.status_code == 400
    assert response.json()["detail"] == "Weight must be between 0 and 100"

    # Weight below 0
    response = client.put("/client/test/weights/source/source-b/category/kitchen-tools", json={"w": -1})
    assert response.status_code == 400
    assert response.json()["detail"] == "Weight must be between 0 and 100"

def test_update_category_weight_source_not_found():
    response = client.put("/client/test/weights/source/source-b/category/kitchen-bulls", json={"w": 80})
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"


def test_update_category_weight_exceeds_total():
    response = client.put("/client/test/weights/source/source-b/category/kitchen-tools", json={"w": 90})
    assert response.status_code == 400
    assert response.json()["detail"] == "Total category weight exceeds 100 within the source: source-b"
    

# Campaign update
def test_update_campaign_weight():
    response = client.put("/client/test/weights/source/source-b/category/kitchen-tools/campaign/electric-garlic-chopper", json={"w": 100})
    assert response.status_code == 200
    assert response.json()["w"] == 100

    # check sum of campaigns
    category = data["source-b"]["categories"]["kitchen-tools"]["campaigns"]
    assert sum(campaign['w'] for campaign in category.values()) == 100

def test_update_campagin_weight_out_of_range_weight():
    # Weight above 100
    response = client.put("/client/test/weights/source/source-b/category/kitchen-tools/campaign/electric-garlic-chopper", json={"w": 101})
    assert response.status_code == 400
    assert response.json()["detail"] == "Weight must be between 0 and 100"

    # Weight below 0
    response = client.put("/client/test/weights/source/source-b/category/kitchen-tools/campaign/electric-garlic-chopper", json={"w": -1})
    assert response.status_code == 400
    assert response.json()["detail"] == "Weight must be between 0 and 100"

def test_update_campagin_weight_source_not_found():
    response = client.put("/client/test/weights/source/source-b/category/kitchen-tools/campaign/not-a-campaign", json={"w": 80})
    assert response.status_code == 404
    assert response.json()["detail"] == "Campaign not found"

def test_update_campaign_weight_does_not_equal_100():
    response = client.put("/client/test/weights/source/source-b/category/gadgets/campaign/smartphone-stand", json={"w": 40})
    assert response.status_code == 400
    assert response.json()["detail"] == "Total campaign weight must equal 100 within the category"
