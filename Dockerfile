FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8032

VOLUME /app/db.sqlite3

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

