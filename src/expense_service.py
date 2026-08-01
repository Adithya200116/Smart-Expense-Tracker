from fastapi import HTTPException
from src.data import expenses


def add_expense(expense):
    for item in expenses:
        if item.id == expense.id:
            raise HTTPException(
                status_code=400,
                detail="Expense with this ID already exists."
            )

    expenses.append(expense)
    return {
        "message": "Expense added successfully",
        "expense": expense
    }


def get_all_expenses():
    return expenses


def get_expenses_by_category(category: str):
    return [
        expense
        for expense in expenses
        if expense.category.lower() == category.lower()
    ]


def get_total_expenses():
    total = sum(expense.amount for expense in expenses)

    return {
        "total": total
    }


def get_total_by_category(category: str):
    total = sum(
        expense.amount
        for expense in expenses
        if expense.category.lower() == category.lower()
    )

    return {
        "category": category,
        "total": total
    }


def delete_expense(expense_id: int):
    for index, expense in enumerate(expenses):
        if expense.id == expense_id:
            expenses.pop(index)
            return True

    return None