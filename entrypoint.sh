#!/bin/sh
set -e

echo "Waiting for database..."

: "${DB_HOST:=ticket_db}"
: "${DB_PORT:=5432}"
: "${DB_USER:=postgres}"

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

>&2 echo "Postgres is up - continuing"

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3