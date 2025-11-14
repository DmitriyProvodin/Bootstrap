LMS Complete Final

Setup:
1. copy .env_template -> .env and set DB/Redis/Stripe
2. python -m venv .venv
3. activate env
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py loaddata fixtures/demo_data.json
8. python manage.py create_groups
9. Start redis
10. celery -A config.celery_app worker -l info
11. celery -A config.celery_app beat -l info
12. python manage.py runserver

Docs: /api/docs/
