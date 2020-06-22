#!/bin/bash

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata db_populate.json
python manage.py test
python manage.py runserver 127.0.0.1:8000