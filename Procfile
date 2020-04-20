release: python manage.py migrate --run-syncdb
web: gunicorn Ahorcadov2.wsgi --env DJANGO_SETTINGS_MODULE=Ahorcadov2.settings.production --timeout 600 --log-file -