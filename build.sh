#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

DJANGO_SUPERUSER_USERNAME=dharm \
DJANGO_SUPERUSER_EMAIL=acostalandarey@gmail.com \
DJANGO_SUPERUSER_PASSWORD=SuperUserPass1984 \
python manage.py createsuperuser --noinput