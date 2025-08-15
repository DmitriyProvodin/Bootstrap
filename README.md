# MyShop (PostgreSQL, модели, фикстуры, команда)

Продолжение учебного проекта. Подключён PostgreSQL, модели Category и Product, админка, фикстуры, кастомная команда, медиа.

## Быстрый старт
```bash
cd myshop_pg
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

# укажи свои данные подключения в .env
python manage.py migrate
python manage.py createsuperuser  # создать суперпользователя
python manage.py load_test_data   # загрузить фикстуры
python manage.py runserver
```

Открой:
- http://127.0.0.1:8000/ — Главная (печатает последние 5 продуктов в консоль)
- http://127.0.0.1:8000/admin/ — Админка
- http://127.0.0.1:8000/contacts/ — Контакты

## Скриншоты
Скриншоты для задания 5 сохраняйте в папке `screenshots/` в корне репозитория.
