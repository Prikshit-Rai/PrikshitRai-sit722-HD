import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        context.close()

def test_create_item(browser_context):
    page = browser_context.new_page()
    page.goto("http://localhost:8086/docs")
    # Simulate API call via Swagger UI or make actual HTTP requests
    response = page.request.post("/items/", json={"name": "Laptop", "quantity": 10})
    assert response.status == 200
