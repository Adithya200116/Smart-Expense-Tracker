````markdown
# Smart Expense Tracker API

## Overview

Smart Expense Tracker API is a RESTful web service built using FastAPI to manage personal expenses. The application stores expense data in memory and provides endpoints to add, retrieve, filter, summarize, and delete expenses.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Interactive Swagger/OpenAPI documentation

---

## Project Structure

```
smart-expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── data.py
│   └── expense_service.py
│
└── tests/
    └── test_api.py
```

---

## Installation

Clone the repository.

```bash
git clone <your-github-repository-url>
cd smart-expense-tracker
```

Create a virtual environment.

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Server

Run the application using:

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

## Running Tests

## Run Tests

```bash
python -m pytest
```

## Technologies Used

- Python 3
- FastAPI
- Pydantic
- Pytest
- Uvicorn

---

## Notes

- Data is stored in memory.
- Restarting the server clears all stored expenses.
- No external database is required.
````
