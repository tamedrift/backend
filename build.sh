#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install --without dev,scripts

python manage.py collectstatic --no-input
python manage.py migrate