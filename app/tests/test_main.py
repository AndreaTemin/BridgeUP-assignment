import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.data import data

INITIAL_DATA = data

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_data():
    # Before each test, reset the data to the initial state
    from app.data import data
    data.clear()
    data.update(INITIAL_DATA)
    

def test_get_weights():
    response = client.get("/client/1/weights")
    assert response.status_code == 200
    assert response.json() == INITIAL_DATA

def test_update_source_weight():
    response = client.put("/client/1/weights/source/source-b", json={"w": 80})
    assert response.status_code == 200
    assert response.json()["w"] == 80

    # check if the sum of 