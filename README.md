Habits Tracker

Setup:
1. copy .env_template -> .env and set credentials
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. Run Redis
6. celery -A config.celery_app worker -l info
7. celery -A config.celery_app beat -l info
8. runserver
Docs: /api/docs/
