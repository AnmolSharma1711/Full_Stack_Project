#!/bin/bash
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py createsuperuser --username admin --email admin@example.com --noinput 2>/dev/null || true

echo "Build completed successfully!"
