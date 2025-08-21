
# myshop

Учебный Django-проект с PostgreSQL и приложением `catalog` (модели Category и Product).

## Развёртывание
```
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
cp .env_template .env  # заполните переменные
python manage.py migrate
python manage.py createsuperuser
python manage.py load_test_data
python manage.py runserver
```
Админка: http://127.0.0.1:8000/admin/
