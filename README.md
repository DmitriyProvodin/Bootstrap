LMS DRF project - fixed version

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

Notes:
- .gitignore present
- migrations for users and courses included
