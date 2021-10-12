#!/bin/bash
set -eu

echo "Syncing the Database"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py ensuresuperuser --no-input
python3 manage.py collectstatic --no-input
python3 manage.py loaddata initial_data.json

echo "Running tests"
pytest

echo "Starting server"
gunicorn backend.wsgi -w 3 --bind 0.0.0.0:8000 --reload