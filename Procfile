release: python manage.py migrate --run-syncdb  --settings=Ahorcadov2.settings.production
web: gunicorn Ahorcadov2.wsgi --log-file -gst