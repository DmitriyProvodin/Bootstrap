# Habit Tracker — Deployment (Docker + GitHub Actions)

Эти файлы помогают автоматически запускать проект через Docker и деплоить на удалённый сервер.

## Что включено
- `Dockerfile` — образ для Django-проекта.
- `docker-compose.yml` — сервисы: backend, db(Postgres), redis, celery, celery-beat.
- `.env.example` — шаблон переменных окружения.
- `.github/workflows/ci-deploy.yml` — CI: тесты + деплой (ssh -> git pull -> docker compose up).

## Как использовать локально
1. Скопируйте `.env.example` в `.env` и заполните значения.
2. Соберите и запустите:
   ```bash
   docker compose build
   docker compose up -d
   ```
3. Проверьте:
   - Backend: http://localhost:8000
   - Postgres: localhost:5432
   - Redis: localhost:6379

## Настройка удалённого сервера
1. На сервере установите Docker и Docker Compose.
2. Клонируйте репозиторий в `~/app/project`.
3. Настройте SSH-доступ (ключи).
4. Заполните `.env` на сервере (или используйте Secrets и CI, если собираете образы).
5. Убедитесь, что сервер может выполнять `docker compose up -d --build`.

## GitHub Actions Secrets (обязательно)
- `SSH_PRIVATE_KEY` — приватный ключ для доступа к серверу (без пароля).
- `SSH_HOST` — IP или домен сервера.
- `SSH_USER` — пользователь (например, ubuntu).
- `SSH_PORT` — SSH порт (22 по умолчанию).

## Примечания
- Workflow выполняет `pytest` — убедитесь, что тесты настроены в проекте.
- Деплой выполняется только для веток `develop` и `main`.
