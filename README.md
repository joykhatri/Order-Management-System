# Order-Management-System
Develop a **REST API** using **Django Rest Framework (DRF)** and **MySQL** that manages **users**, **products**, and **orders** with proper relationships and data fetching using joins / nested **serializers**.

## 🚀 Setup Instructions

### 1. Create and activate a virtual environment
```bash
python -m venv .venv
```

### 2. Activate virtual environment.
```bash
Windows:
.venv\Scripts\activate

Linux / macOS:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django djangorestframework
pip install mysqlclient
pip install djangorestframework-simplejwt
```

### 4. Create Django project and apps
```bash
django-admin startproject project .
django-admin startapp customers
django-admin startapp orders
django-admin startapp products
```

### 5. Configure INSTALLED_APPS in project/settings.py
```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
    'customers',
    'orders',
    'products',
]
```

### 6. Configure MySQL Database in settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',   # Or your DB IP
        'PORT': '3306',
    }
}
```

### 6. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the server
```bash
python manage.py runserver
```

## 📦 API Endpoints

### Customers
| Method | Endpoint               | Description          | Payload Example                                                              |
| ------ | ---------------------- | -------------------- | ---------------------------------------------------------------------------- |
| POST   | `/api/customers/`      | Create a customer    | `{ "name": "John Doe", "email": "john@example.com", "phone": "1234567890" }` |
| GET    | `/api/customers/`      | List all customers   | -                                                                            |
| GET    | `/api/customers/{id}/` | Get customer details | -                                                                            |
| PUT    | `/api/customers/{id}/` | Update customer      | `{ "name": "Jane Doe", "email": "jane@example.com", "phone": "0987654321" }` |
| DELETE | `/api/customers/{id}/` | Delete customer      | -                                                                            |


### Products
| Method | Endpoint              | Description       | Payload Example                                           |
| ------ | --------------------- | ----------------- | --------------------------------------------------------- |
| POST   | `/api/products/`      | Create a product  | `{ "name": "Samsung TV", "price": 80000.45, "stock": 3 }` |
| GET    | `/api/products/`      | List all products | -                                                         |
| PUT    | `/api/products/{id}/` | Update product    | `{ "name": "LG TV", "price": 75000.00, "stock": 5 }`      |
| DELETE | `/api/products/{id}/` | Delete product    | -                                                         |

### Orders
| Method | Endpoint            | Description             | Payload Example                                                                                             |
| ------ | ------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| POST   | `/api/orders/`      | Create order with items | `{ "customer_id": 1, "items": [ { "product_id": 2, "quantity": 3 }, { "product_id": 4, "quantity": 1 } ] }` |
| GET    | `/api/orders/`      | List all orders         | -                                                                                                           |
| GET    | `/api/orders/{id}/` | Get order details       | -                                                                                                           |
| PATCH  | `/api/orders/{id}/` | Update order status     | `{ "status": "shipped" }`                                                                                   |

