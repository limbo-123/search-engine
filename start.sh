#!/bin/bash
source ./start/bin/activate
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell -c "from django.contrib.auth.models import User; \
                           User.objects.create_superuser('aanand',
                           'admin1@example.com', '1234')"
python3 manage.py runserver 0.0.0.0:8080
