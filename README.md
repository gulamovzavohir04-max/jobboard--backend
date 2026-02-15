# JobBoard API (Django REST)

REST API for a Job Board platform built with Django and Django REST Framework.

## Features
- JWT Authentication (SimpleJWT): access & refresh tokens
- User registration endpoint
- Jobs API endpoints (protected)
- Django Admin panel

## Tech Stack
- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite (dev)

## API Endpoints

### Auth
- `POST /api/token/` — get access & refresh token
- `POST /api/token/refresh/` — refresh access token

### Accounts
- `POST /api/accounts/register/` — create a new user

### Jobs (JWT required)
- `GET /api/jobs/` — list jobs
- `POST /api/jobs/` — create job

## Run Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
