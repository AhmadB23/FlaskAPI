# E-Commerce Book Store - Flask REST API

A comprehensive RESTful backend for an E-Commerce Book Store built with Flask. This project provides secure APIs for user registration, browsing books, managing shopping carts, order processing, and admin management.

## 🚀 Features

- **User Management**: Registration, login, JWT-based authentication
- **Book Catalog**: Browse, filter, and search books by category, author, and price
- **Shopping Cart**: Add, update, remove items with real-time stock validation
- **Order Management**: Secure checkout process with stock locking and transaction handling
- **Admin Panel**: Manage books, authors, categories, and order fulfillment
- **Reviews**: Users can rate and review books
- **Security**: Password hashing, JWT tokens, role-based access control (RBAC)

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Framework**: Flask
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: Flask-JWT-Extended, Bcrypt
- **Migrations**: Flask-Migrate
- **Development**: VS Code, Git

## 📋 Prerequisites

- Python 3.10 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Postman (for API testing)

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AhmadB23/FlaskAPI.git
cd FlaskAPI
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL Database

```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE flaskapi_db;

# Exit
\q
```

### 5. Configure Environment Variables

Update `.env` file with your database credentials:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/flaskapi_db
SECRET_KEY=your-secret-key-change-in-production
JWT_SECRET_KEY=jwt-secret-key-change-in-production
```

### 6. Initialize Database Migrations

```bash
# Initialize migrations
flask db init

# Create migration
flask db migrate -m "Initial schema"

# Apply to database
flask db upgrade
```

### 7. Run the Application

```bash
python run.py
```

The API will be available at: `http://localhost:5000`

## 📚 API Documentation

Complete API documentation available in [`API_DOCUMENTATION.md`](./API_DOCUMENTATION.md)

### Quick API Overview

| Endpoint | Method | Description | Auth |
|----------|--------|-------------|------|
| `/api/v1/auth/register` | POST | Register new user | No |
| `/api/v1/auth/login` | POST | Login user | No |
| `/api/v1/books` | GET | Browse books | No |
| `/api/v1/books/{id}` | GET | Get book details | No |
| `/api/v1/cart` | GET | View cart | Yes |
| `/api/v1/cart/items` | POST | Add to cart | Yes |
| `/api/v1/orders/checkout` | POST | Checkout | Yes |
| `/api/v1/orders` | GET | View orders | Yes |
| `/api/v1/admin/orders` | GET | Admin view all orders | Admin |
| `/api/v1/books` | POST | Create book | Admin |

## 🗂️ Project Structure

```
FlaskAPI/
├── app/
│   ├── __init__.py              # App factory, extensions init
│   ├── models/                  # Database models
│   │   ├── __init__.py
│   │   ├── BaseModel.py         # Base model with common fields
│   │   ├── User.py
│   │   ├── Book.py
│   │   ├── Author.py
│   │   ├── Category.py
│   │   ├── CartItem.py
│   │   ├── OrderDetails.py
│   │   ├── OrderItem.py
│   │   └── Review.py
│   ├── routes/                  # API endpoints
│   │   ├── AuthRoutes.py
│   │   ├── UserRoutes.py
│   │   ├── BookRoutes.py
│   │   ├── AuthorRoutes.py
│   │   ├── CategoryRoutes.py
│   │   ├── CartRoutes.py
│   │   └── OrderRoutes.py
│   ├── services/                # Business logic
│   │   ├── UserService.py
│   │   ├── BookService.py
│   │   ├── AuthorService.py
│   │   ├── CategoryService.py
│   │   ├── CartService.py
│   │   └── OrderService.py
│   └── utils/
│       └── enums.py
├── config/                      # Environment configs
│   ├── development.py
│   ├── production.py
│   └── testing.py
├── migrations/                  # Database migrations
├── tests/                       # Unit tests
├── .env                         # Environment variables
├── .gitignore
├── requirements.txt
├── run.py                       # Application entry point
├── README.md
├── API_DOCUMENTATION.md         # Complete API docs
├── SETUP_GUIDE.md              # Setup instructions
├── MIGRATION_JWT_GUIDE.md      # Migrations & JWT guide
└── QUICKSTART.md               # Quick start guide
```

## 🔐 Security Features

- ✅ **JWT Authentication**: Secure token-based authentication
- ✅ **Password Hashing**: Bcrypt for secure password storage
- ✅ **Role-Based Access Control**: Admin vs regular user permissions
- ✅ **Input Validation**: Comprehensive request validation
- ✅ **SQL Injection Protection**: SQLAlchemy ORM with parameterized queries
- ✅ **Stock Validation**: Prevent negative stock scenarios
- ✅ **Transaction Handling**: Database transactions for order processing
- ✅ **Row Locking**: Prevent race conditions on stock updates

## 🧪 Testing with Postman

### 1. Import Collection

See [`API_DOCUMENTATION.md`](./API_DOCUMENTATION.md) for complete endpoint details.

### 2. Setup Environment Variables

- `base_url`: `http://localhost:5000`
- `access_token`: (auto-populated after login)

### 3. Test Flow

1. **Register**: `POST /api/v1/auth/register`
2. **Login**: `POST /api/v1/auth/login` (save token)
3. **Browse Books**: `GET /api/v1/books`
4. **Add to Cart**: `POST /api/v1/cart/items`
5. **Checkout**: `POST /api/v1/orders/checkout`
6. **View Orders**: `GET /api/v1/orders`

## 👥 User Roles

- **Customer (role = 0)**: Browse books, manage cart, place orders, add reviews
- **Admin (role >= 1)**: All customer permissions + manage books, authors, categories, and order fulfillment

## 📊 Database Schema

### Core Entities
- **User**: User accounts with authentication
- **Book**: Book catalog with stock management
- **Author**: Book authors
- **Category**: Book categories
- **CartItem**: Shopping cart items
- **OrderDetails**: Order information
- **OrderItem**: Individual items in an order
- **Review**: Book reviews and ratings

All models inherit from `BaseModel` with common fields:
- `id` (UUID)
- `created_at`, `updated_at`
- `is_deleted`, `deleted_at` (soft delete)
- `created_by`, `role`, `is_active`

## 🚧 Development

### Run Migrations

```bash
# After model changes
flask db migrate -m "Description of changes"
flask db upgrade
```

### View Database in pgAdmin

1. Open pgAdmin
2. Register server: `localhost:5432`
3. Database: `flaskapi_db`
4. Navigate to Tables

## 📖 Additional Documentation

- [`SETUP_GUIDE.md`](./SETUP_GUIDE.md) - PostgreSQL and Postman setup
- [`MIGRATION_JWT_GUIDE.md`](./MIGRATION_JWT_GUIDE.md) - Database migrations and JWT authentication
- [`QUICKSTART.md`](./QUICKSTART.md) - Quick start instructions
- [`API_DOCUMENTATION.md`](./API_DOCUMENTATION.md) - Complete API reference

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**AhmadB23**

## 🙏 Acknowledgments

- Flask framework and extensions
- SQLAlchemy ORM
- PostgreSQL database
- JWT authentication library
