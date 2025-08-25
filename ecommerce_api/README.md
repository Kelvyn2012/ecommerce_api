# 🛍️ E-commerce Product API (Django + DRF)

This project is a **RESTful API** for managing products on an e-commerce platform.  
It allows users to **register, authenticate, and manage products (CRUD)**, while supporting **search, filtering, and pagination**.  
Built with **Django + Django REST Framework**, and deployable to **Heroku or PythonAnywhere**.  

---

## 🚀 Features

- **User Management (CRUD)**
  - Register with username, email, password
  - JWT Authentication (Login/Logout via tokens)
  - Only authenticated users can create/update/delete products
  - Admin can manage all users

- **Product Management (CRUD)**
  - Name, Description, Price, Category, Stock Quantity, Image URL, Created Date
  - Validation for required fields (price > 0, stock ≥ 0, name required)
  - Products linked to categories & owners (users)

- **Search & Filtering**
  - Search by product name or category (partial matches allowed)
  - Filter by:
    - Category (slug)
    - Price range (`price_min`, `price_max`)
    - Stock availability (`in_stock=true/false`)
  - Ordering by price, date, or name

- **Pagination**
  - Page-based pagination (`?page=2`)
  - Configurable in settings

- **Authentication**
  - JWT (access & refresh tokens) using `djangorestframework-simplejwt`

- **Deployment Ready**
  - Configured for **Heroku** (Gunicorn, Whitenoise, Postgres support)
  - Can also run on **PythonAnywhere**

---

## 🗂️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: JWT (SimpleJWT)
- **Database**: SQLite (dev), Postgres (prod-ready)
- **Deployment**: Heroku / PythonAnywhere
- **Other**: Django Filters, Pillow, Decouple, Whitenoise, Gunicorn

---

## 📊 ERD (Entity Relationship Diagram)

