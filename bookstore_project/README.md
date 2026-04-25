# Bookstore 

> A production-ready Django REST Framework backend powering the Online Bookstore — handling authentication, book inventory, orders, cart management, and payments.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Models](#models)
- [Configuration Notes](#configuration-notes)

---

## Overview

This backend exposes a RESTful API for the Online Bookstore platform. It handles the full lifecycle of a bookstore application — user registration and login, browsing and managing books, building a cart, placing orders, and processing payments via Stripe.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 4.x |
| API | Django REST Framework |
| Language | Python 3.11+ |
| Database | PostgreSQL (SQLite for development) |
| Authentication | JWT via `djangorestframework-simplejwt` |
| Payments | Stripe API |
| CORS | `django-cors-headers` |
| Environment | `python-decouple` / `.env` |

---

## Project Structure

```
bookstore_project/
│
├── bookstore_project/          # Core Django config
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── store/                      # Main application
│   ├── migrations/             # Database migrations
│   ├── models.py               # Data models
│   ├── serializers.py          # DRF serializers
│   ├── views.py                # API views
│   ├── urls.py                 # App-level URL routing
│   ├── admin.py                # Django admin registration
│   └── apps.py
│
├── manage.py
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL (or SQLite for local dev)
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your_username/bookstore_project.git
cd bookstore_project
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        
venv\Scripts\activate          
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

```bash
cp .env.example .env

```

**5. Apply migrations**

```bash
python manage.py migrate
```

**6. Create a superuser**

```bash
python manage.py createsuperuser
```

**7. Run the development server**

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## Environment Variables

Create a `.env` file in the project root. Never commit this file.

```env
# Django
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL)
DB_NAME=bookstore_db
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432


# JWT
ACCESS_TOKEN_LIFETIME_MINUTES=60
REFRESH_TOKEN_LIFETIME_DAYS=7
```

See `.env.example` for a full template.

---

## API Endpoints

### Auth

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Login and receive JWT tokens |
| `POST` | `/api/auth/logout/` | Invalidate refresh token |
| `POST` | `/api/auth/token/refresh/` | Refresh access token |

### Books

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/books/` | List all books |
| `GET` | `/api/books/{id}/` | Retrieve a single book |
| `POST` | `/api/books/` | Create a book _(admin only)_ |
| `PUT` | `/api/books/{id}/` | Update a book _(admin only)_ |
| `DELETE` | `/api/books/{id}/` | Delete a book _(admin only)_ |

### Cart

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/cart/` | View current cart |
| `POST` | `/api/cart/add/` | Add a book to the cart |
| `DELETE` | `/api/cart/{id}/` | Remove an item from the cart |

### Orders

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/orders/` | List all orders for the user |
| `POST` | `/api/orders/` | Create a new order |
| `PUT` | `/api/orders/{id}/` | Update an order |
| `DELETE` | `/api/orders/{id}/` | Cancel an order |

### Checkout & Payments

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/checkout/` | Process checkout |
| `POST` | `/api/payments/` | Initiate Stripe payment |

---

## Authentication

This project uses **JWT (JSON Web Tokens)** via `djangorestframework-simplejwt`.

**Flow:**

1. Client sends credentials to `/api/auth/login/`
2. Server returns `access` and `refresh` tokens
3. Client includes the access token in the `Authorization` header for protected requests:

```http
Authorization: Bearer <access_token>
```

4. When the access token expires, use the refresh token at `/api/auth/token/refresh/` to obtain a new one.

---

## Models

| Model | Description |
|---|---|
| `User` | Extended Django user model |
| `Book` | Book catalog entry (title, author, price, stock) |
| `Order` | A placed order linked to a user |
| `OrderItem` | Individual line item within an order |
| `Cart` | Active shopping cart per user (one-to-one) |
| `CartItem` | A book added to the cart with quantity |
| `Checkout` | Checkout session linking cart to order |
| `Payment` | Stripe payment record for an order |
| `OrderTracking` | Status tracking for order fulfillment |

---

## Configuration Notes

**Database**
The project defaults to SQLite for local development. Switch to PostgreSQL for staging/production by updating the `DATABASES` block in `settings.py` using environment variables.

**CORS**
`CORS_ALLOW_ALL_ORIGINS = True` is set for development only. In production, replace this with:

```python
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
]
```

**Stripe**
Test payments use Stripe test keys (`sk_test_...`). Switch to live keys (`sk_live_...`) only in a production environment with HTTPS enforced.

**Static & Media Files**
Configure `STATIC_ROOT` and `MEDIA_ROOT` and run `python manage.py collectstatic` before deploying to production.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.