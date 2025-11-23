# Платформа онлайн-обучения — запуск через Docker

## 📦 Требования
- Docker
- Docker Compose

## ⚙️ Установка

1. Скопируйте шаблон окружения:

```bash
cp .env.example .env
```

2. Заполните необходимые переменные.

3. Соберите и запустите весь проект:

```bash
docker-compose up --build
```

## 🧩 Сервисы

| Сервис | Порт | Проверка |
|--------|------|-----------|
| Backend (Django) | 8000 | http://localhost:8000 |
| PostgreSQL | 5432 | docker exec -it postgres psql -U postgres |
| Redis | 6379 | redis-cli ping |
| Celery | — | docker logs celery |
| Celery Beat | — | docker logs celery_beat |

## 🛑 Остановка контейнеров

```bash
docker-compose down
```
