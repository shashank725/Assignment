#!/usr/bin/env bash

# exit on error
set -o errexit
# cd chatroom

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py collectstatic --no-input