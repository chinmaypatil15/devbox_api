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

2. **Create virtual environment**
```bash
python -m venv venv
```

3. **Activate virtual environment**
- Windows:
```cmd
.\venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Initialize database**
```bash
python init_db.py
```

6. **Run the application**
```bash
python app.py
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