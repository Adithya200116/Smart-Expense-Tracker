import os
import sys

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from src.main import app
from src.data import expenses

client = TestClient(app)


def setup_function():
    expenses.clear()


def test_add_expense():

    response = client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Expense added successfully"


def test_get_expenses():

    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_category():

    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Pizza",
            "amount": 500,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    response = client.get("/expenses/category/Food")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_total_expenses():

    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Movie",
            "amount": 300,
            "category": "Entertainment",
            "date": "2026-07-31"
        }
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 300


def test_delete_expense():

    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Book",
            "amount": 600,
            "category": "Education",
            "date": "2026-07-31"
        }
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Expense deleted successfully"