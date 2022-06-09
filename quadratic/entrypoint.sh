#!/usr/bin/env bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn quadratic.wsgi:application --bind 0:8000
