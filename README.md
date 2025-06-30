# 🧠 Devbox Platform – Backend Assignment

This project implements a simple backend RESTful API service using **Django + Django REST Framework**. It provides:

- Token-based login
- Mock user profile
- API usage tracking (GET and POST)
- Swagger API documentation
- Simulated Kafka-style event logging

---

## 📦 Tech Stack

- Python 3.11+
- Django 5.x
- Django REST Framework
- DRF-YASG (Swagger UI)
- Token Authentication

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
    git clone https://github.com/yourusername/devbox-api.git
    cd devbox-api
```

### 2. **Create virtual environment**
```bash
python -m venv env
```

### 3. **Activate virtual environment**
- Windows:
```cmd
.\venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

### 4. **Install dependencies**
```bash
pip install -r requirements.txt
```
### 5. Apply Migrations ---- (if needed)

```bash
python manage.py migrate
```

### 6. Create Superuser (for Admin Access) ---- (if needed)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server ---- (if only run than just skip 5th and 6th and run this )

```bash
python manage.py runserver
```

## Access the Application
- Visit: http://localhost:8000
- Visit: http://127.0.0.1:8000/api/login/
- Default admin credentials:
  - Username: admin
  - Password: admin


## Project Structure
```
devbox_api/
├── api/
│   ├── __init__.py
│   ├── __pycache__
│   ├── migrations
│   ├── static
│   ├── templates
│   ├── admin.py
│   ├── apps.py
│   ├── mock_data.py
│   ├── models.py
│   ├── test.py
│   ├── urls.py
│   ├── views.py
│   ├── serializers.py
├── devbox_api/
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── requirements.txt
├── manage.py
└── README.md
``` 