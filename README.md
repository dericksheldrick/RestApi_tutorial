# 🍹 Drinks API (Flask + SQLAlchemy)

A simple RESTful API built with **Flask**, **SQLAlchemy**, and **Flask-Migrate** for managing a drinks menu.  
This API allows you to **Create, Read, Update, and Delete (CRUD)** drink entries in a SQLite database.

---

##  Features
- **View all drinks**
- **View a single drink by ID**
- **Add a new drink**
- **Update an existing drink**
- **Delete a drink**
- Uses **SQLite** for storage
- Flask-Migrate for easy database migrations

---

## 🛠 Tech Stack
- Flask – Python micro web framework
- Flask-SQLAlchemy – ORM for database interactions
- Flask-Migrate – Database migrations
- SQLite – Lightweight database

---

## 📂 Project Structure
```
api/
│── application.py 
│── instance/drinks.db
|── Migration
│── requirements.txt
|── seed.py

└── README.md 
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/drinks-api.git
cd drinks-api
```
### 2️⃣ Create a virtual environment
```bash
python -m venv venv
Activate it:
```

Windows:

```bash
venv\Scripts\activate
```
Mac/Linux:

```bash
source venv/bin/activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Set up the database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
---
### 📡 API Endpoints
| Method | Endpoint        | Description        | Example Request Body |
|--------|-----------------|--------------------|----------------------|
| GET    | `/`              | Welcome message    | — |
| GET    | `/drinks`        | Get all drinks     | — |
| GET    | `/drinks/<id>`   | Get a drink by ID  | — |
| POST   | `/drinks`        | Add a new drink    | `{ "name": "Coke", "price": 1.5, "description": "Refreshing cola" }` |
| PUT    | `/drinks/<id>`   | Update a drink     | `{ "name": "Pepsi", "price": 1.8, "description": "New taste" }` |
| DELETE | `/drinks/<id>`   | Delete a drink     | — |
