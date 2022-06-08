#!/usr/bin/env bash
python manage.py migrate
gunicorn quadratic.wsgi:application --bind 0:8000
