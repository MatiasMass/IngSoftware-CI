from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":  "FastAPI is working"}


def test_get_products():
    response = client.get("/api/products/")
    assert response.status_code == 200
    assert response.json() == {
        "Status": "Success",
        "Results": 2,
        "Products":     [
            {
                "id": 1,
                "name": "Product 1",
                "description": "This is the description for product 1",
                "price": 100,
                "image": "https://picsum.photos/200/300"
            },
            {
                "id": 2,
                "name": "Product 2",
                "description": "This is the description for product 2",
                "price": 200,
                "image": "https://picsum.photos/200/300"
            },
        ],
    }


def test_get_product():
    response = client.get("/api/products/1")
    assert response.status_code == 200
    assert response.json() == {
        "Status": "Success",
        "Product":     {
            "id": 1,
            "name": "Product 1",
            "description": "This is the description for product 1",
            "price": 100,
            "image": "https://picsum.photos/200/300"
        },
    }


def test_get_product_not_found():
    response = client.get(
        "/api/products/4"
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No Product with this id: `4` found"

    }
