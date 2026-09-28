<div align="center">

# 💰 Smart Expense Tracker API

### FastAPI Backend for Personal Expense Management

**A clean RESTful API for recording, filtering, summarizing and managing personal expenses.**

`Python` • `FastAPI` • `Pydantic` • `Pytest` • `Uvicorn` • `OpenAPI`

</div>

---

## 🚀 Overview

**Smart Expense Tracker API** is a RESTful backend application built with **FastAPI** for managing personal expenses.

The API allows users to add, retrieve, filter, summarize and delete expense records while providing automatically generated **Swagger/OpenAPI documentation** for exploring and testing endpoints.

The project focuses on clean API design, request/response validation, service separation and automated testing.

---

## ✨ Features

➕ **Add Expenses** — Create and store new expense records

📋 **View Expenses** — Retrieve all recorded expenses

🔎 **Category Filtering** — Filter expenses by category

💰 **Expense Summary** — Calculate total spending

📊 **Category Summary** — Calculate spending totals by category

🗑️ **Delete Expenses** — Remove existing expense records

🧪 **Automated Testing** — API tests using Pytest

📖 **Interactive API Documentation** — Swagger UI and ReDoc generated automatically by FastAPI

---

## 🏗️ Architecture

```text
                Client / API Consumer
                         │
                         ▼
                ┌─────────────────┐
                │     FastAPI     │
                │   REST Routes   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Pydantic     │
                │ Data Validation │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Expense Service │
                │ Business Logic  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ In-Memory Data  │
                │     Store       │
                └─────────────────┘
```

---

## 📁 Project Structure

```text
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

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| Programming | Python 3 |
| API Framework | FastAPI |
| Data Validation | Pydantic |
| API Server | Uvicorn |
| Testing | Pytest |
| Documentation | Swagger / OpenAPI / ReDoc |
| Storage | In-memory |

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Adithya200116/Smart-Expense-Tracker.git
cd Smart-Expense-Tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate it on Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the API

```bash
uvicorn src.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Once the server is running, FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to explore and test the available API endpoints directly from the browser.

---

## 🧪 Testing

Run the automated tests with:

```bash
python -m pytest
```

The test suite is located inside:

```text
tests/
└── test_api.py
```

---

## 🔄 API Workflow

```text
Create Expense
      │
      ▼
Validate Request
      │
      ▼
Store Expense
      │
      ├──────────────► View Expenses
      │
      ├──────────────► Filter by Category
      │
      ├──────────────► Calculate Totals
      │
      └──────────────► Delete Expense
```

---

## 🎯 What This Project Demonstrates

This project demonstrates practical experience with:

- REST API development
- FastAPI application architecture
- Pydantic data validation
- Separation of API and business logic
- CRUD-style backend operations
- Automated API testing
- Swagger/OpenAPI documentation
- Python backend development

---

## 📝 Current Storage

The application currently uses **in-memory storage**, which keeps the project lightweight and requires no external database.

Because the data is stored in memory, restarting the server clears the stored expense records.

A persistent database can be integrated as a future enhancement.

---

<div align="center">

### 💰 Simple Expenses. Clean APIs. Structured Backend.

**Built by Adithya M Kaushik**

</div>
