LMS_final_project

Setup:
1. copy .env_template -> .env and set DB credentials (Postgres)
2. python -m venv .venv
3. activate env
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py create_groups
8. runserver

Docs: /api/docs/
Stripe payment endpoint: POST /api/users/payment/ (returns payment_url)
