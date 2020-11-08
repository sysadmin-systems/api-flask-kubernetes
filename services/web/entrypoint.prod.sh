#!/bin/sh

#python manage.py run -h 0.0.0.0
gunicorn --bind 0.0.0.0:5000 manage:app