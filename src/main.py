from fastapi import FastAPI, HTTPException
from src.models import Expense
from src.expense_service import (
    add_expense,
    get_all_expenses,
    get_expenses_by_category,
    get_total_expenses,
    get_total_by_category,
    delete_expense,
)

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A REST API to manage personal expenses",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Welcome to Smart Expense Tracker API"}


@app.post("/expenses")
def create_expense(expense: Expense):
    return add_expense(expense)


@app.get("/expenses")
def view_expenses():
    return get_all_expenses()


@app.get("/expenses/category/{category}")
def filter_by_category(category: str):
    return get_expenses_by_category(category)


@app.get("/expenses/total")
def total_expenses():
    return get_total_expenses()


@app.get("/expenses/total/{category}")
def total_by_category(category: str):
    return get_total_by_category(category)


@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int):
    result = delete_expense(expense_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"message": "Expense deleted successfully"}