# 🛍️ E-commerce Product API (Django + DRF)

This project is a **RESTful API** for managing products in an e-commerce platform.  
It allows users to **register, authenticate, and manage products (CRUD)**, while supporting **search, filtering, and pagination**.  
Built with **Django + Django REST Framework**, and connected to **PostgreSQL**.  

---

## 🚀 Features

- **User Management**
  - Register with username, email, and password
  - Login to obtain a **DRF Token**
  - Only authenticated users can create/update/delete products
  - Admins can manage all users and categories

- **Product Management**
  - Fields: Name, Description, Price, Category, Stock Quantity, Image URL, Created Date
  - Validation: price > 0, stock ≥ 0, name required
  - Products linked to categories & owners (users)

- **Category Management**
  - Create, update, delete categories (admin only)
  - Products assigned to categories

- **Search & Filtering**
  - Search by product name or category
  - Filter by:
    - Category
    - Price range (`price_min`, `price_max`)
    - Stock availability (`in_stock=true/false`)
  - Ordering by price, date, or name

- **Pagination**
  - Page-based pagination (`?page=2`)
  - Configurable in settings

- **Authentication**
  - Uses **DRF Token Authentication**
  - Tokens are obtained at login and passed in headers:
    ```
    Authorization: Token your_token_here
    ```

- **Deployment Ready**
  - Works with **PostgreSQL**
  - Deployable on **Heroku** or **Render**

---

## 🗂️ Tech Stack

- **Backend**: Django, Django REST Framework  
- **Auth**: DRF Token Authentication  
- **Database**: PostgreSQL (production), SQLite (development)  
- **Deployment**: Heroku / Render  
- **Other**: Django Filters, Pillow, Decouple, Whitenoise, Gunicorn  

---

## 📊 ERD (Entity Relationship Diagram)

**Relationships**:
- `User 1—* Product` (owner)
- `Category 1—* Product`

---

## 🔑 API Endpoints

### Auth
| Method | Endpoint            | Description |
|--------|---------------------|-------------|
| POST   | `/api/auth/register/` | Register a new user |
| POST   | `/api/auth/login/`    | Login and obtain token |
| POST   | `/api/auth/logout/`   | Logout and invalidate token |

### Users
| Method | Endpoint         | Description |
|--------|------------------|-------------|
| GET    | `/api/users/`    | List all users (admin only) |
| GET    | `/api/users/{id}/` | Get user details (self or admin) |
| PUT    | `/api/users/{id}/` | Update user info |
| DELETE | `/api/users/{id}/` | Delete user (admin only) |

### Categories
| Method | Endpoint             | Description |
|--------|----------------------|-------------|
| GET    | `/api/categories/`   | List categories |
| POST   | `/api/categories/`   | Create category (admin only) |
| PUT    | `/api/categories/{id}/` | Update category (admin only) |
| DELETE | `/api/categories/{id}/` | Delete category (admin only) |

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
