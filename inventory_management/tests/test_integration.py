from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Laptop", "quantity": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["quantity"] == 10

def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
