FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY . .

RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Ждем базу если нужно\n\
if [ -n "$DB_HOST" ]; then\n\
    echo "Waiting for database..."\n\
    while ! nc -z $DB_HOST $DB_PORT; do\n\
      sleep 0.1\n\
    done\n\
    echo "Database started"\n\
fi\n\
\n\
# Выполняем миграции\n\
python manage.py migrate --noinput\n\
\n\
# Собираем статику в /app/collected_static\n\
python manage.py collectstatic --noinput\n\
\n\
# Копируем статику Django в общий volume\n\
if [ -d "/app/collected_static" ]; then\n\
    echo "Copying Django static files to volume..."\n\
    cp -r /app/collected_static/. /backend_static/ 2>/dev/null || true\n\
fi\n\
\n\
# Создаем директорию для медиа, если не существует\n\
mkdir -p /app/media\n\
\n\
# Запускаем gunicorn\n\
exec gunicorn kittygram_backend.wsgi:application --bind 0.0.0.0:8000 --workers=3\n\
' > /app/docker-entrypoint.sh

RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]