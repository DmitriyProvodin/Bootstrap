# MyShop (учебный проект)

Интернет-магазин на Django. Проект содержит 4 страницы (Главная, Каталог, Категория, Контакты), стилизованные с помощью Bootstrap.

## Установка и запуск
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте:
- http://127.0.0.1:8000/ — Главная
- http://127.0.0.1:8000/catalog/ — Каталог
- http://127.0.0.1:8000/category/ — Категория
- http://127.0.0.1:8000/contacts/ — Контакты

## Стек
- Python 3.10+
- Django 4.2+
- Bootstrap 5 (CDN)

## GitFlow
- main
- develop
- feature/homework-XX → PR в develop
