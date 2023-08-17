python manage.py collectstatic --noinput
python manage.py migrate
gunicorn tamedrift.wsgi