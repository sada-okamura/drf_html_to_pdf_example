#!/bin/sh

python manage.py migrate
/usr/local/bin/python3 manage.py runserver "0.0.0.0:8000"
