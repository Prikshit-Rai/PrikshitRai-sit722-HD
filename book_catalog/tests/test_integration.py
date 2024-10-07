from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={"title": "Test Book", "author": "Author", "year": 2024})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Author"

def test_get_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
