LMS DRF project - final

Quick start:
1. copy .env_template to .env and adjust POSTGRES credentials
2. python -m venv .venv
3. source .venv/bin/activate
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

API endpoints:
- /api/courses/
- /api/lessons/
- /api/lessons/<pk>/
- /api/users/profiles/<pk>/
- /api/users/payments/?course=1&method=cash&ordering=-paid_at

Notes:
- .gitignore present
- migrations for users and courses included
- management command users:create_payments to populate sample payments
