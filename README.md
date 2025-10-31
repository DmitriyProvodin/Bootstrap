LMS project (final) - minimal clean package for submission.

Setup:
1. copy .env_template -> .env and set DB credentials
2. python -m venv .venv
3. activate env
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py create_groups
8. runserver

Notes:
- JWT: /api/auth/token/ and /api/auth/token/refresh/
- Register: POST /api/users/register/
- Courses: /api/courses/courses/
- Lessons: /api/courses/lessons/
- Payments: /api/users/payments/
