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


**Relationships**:
- `User 1—* Product` (owner)
- `Category 1—* Product`

---

## 🔑 API Endpoints

### Auth
| Method | Endpoint              | Description |
|--------|-----------------------|-------------|
| POST   | `/api/auth/token/`    | Login (get JWT token) |
| POST   | `/api/auth/token/refresh/` | Refresh JWT token |

### Users
| Method | Endpoint         | Description |
|--------|------------------|-------------|
| POST   | `/api/users/`    | Register a new user |
| GET    | `/api/users/`    | List all users (admin only) |
| GET    | `/api/users/{id}/` | Get user details (self or admin) |
| PUT    | `/api/users/{id}/` | Update user info |
| DELETE | `/api/users/{id}/` | Delete user (admin only) |

### Categories
| Method | Endpoint             | Description |
|--------|----------------------|-------------|
| GET    | `/api/categories/`   | List categories |
| POST   | `/api/categories/`   | Create category |
| PUT    | `/api/categories/{slug}/` | Update category |
| DELETE | `/api/categories/{slug}/` | Delete category |

### Products
| Method | Endpoint                 | Description |
|--------|--------------------------|-------------|
| GET    | `/api/products/`         | List products (supports pagination, search, filters) |
| POST   | `/api/products/`         | Create product (auth required) |
| GET    | `/api/products/{id}/`    | Get product details |
| PUT    | `/api/products/{id}/`    | Update product (owner only) |
| DELETE | `/api/products/{id}/`    | Delete product (owner only) |

### Search & Filters
- `GET /api/products/?search=phone` → search by name/category  
- `GET /api/products/?category=electronics`  
- `GET /api/products/?price_min=100&price_max=500`  
- `GET /api/products/?in_stock=true`  
- `GET /api/products/?ordering=-price`  

---

## ⚙️ Setup & Installation

Clone repo:
```bash
git clone https://github.com/yourusername/ecommerce_api.git
cd ecommerce_api
