LMS DRF project

Run:
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

Endpoints:
/api/courses/ (ViewSet)
/api/lessons/ (ListCreate)
/api/lessons/<pk>/ (RetrieveUpdateDestroy)
