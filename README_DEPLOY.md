# Deployment package

Files included:
- Dockerfile
- docker-compose.yml
- nginx.conf
- .env.example
- .github/workflows/ci.yaml

## How to use
1. Copy files into your repository root.
2. Fill `.env` based on `.env.example`.
3. Ensure `Dockerfile` and `docker-compose.yml` match your project layout (project folder is `project`).
4. On server, clone repo to `~/app/project`, put `.env` there.
5. Run `docker compose up -d --build`.

## GitHub Actions
Commit `.github/workflows/ci.yaml` to trigger CI for branch `develop`.
