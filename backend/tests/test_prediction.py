import pytest

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_prediction_success(client):
    payload = {
        "carpet_area_sqft": 1000.0,
        "floor_num": 3,
        "bathroom": 2,
        "balcony": 1,
        "location_grouped": "Thane West",
        "furnishing": "Semi-Furnished",
        "transaction": "Resale",
        "ownership": "Freehold",
        "facing": "East"
    }
    response = client.post("/predict", json=payload)
    data = response.json()
    
    assert response.status_code == 200
    assert "predicted_price" in data