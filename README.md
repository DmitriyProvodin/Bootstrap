# MyShop Final Project

## Запуск

1. pip install -r requirements.txt
2. cp .env_template .env  # отредактировать, если нужно
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py load_test_data
7. python manage.py runserver

## Работа с пользователями

- Регистрация: /users/register/ (письмо печатается в консоли)
- Вход: /users/login/ (email + пароль)
- Выход: /users/logout/
- CRUD продуктов (создание/редактирование/удаление) доступен только авторизованным пользователям
