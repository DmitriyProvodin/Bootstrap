FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*             && pip install --upgrade pip             && pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
CMD ["gunicorn","project.wsgi:application","--bind","0.0.0.0:8000","--workers","3"]
