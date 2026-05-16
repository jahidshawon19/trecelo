#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser from environment variables if it doesn't exist
python manage.py shell -c "
from django.contrib.auth.models import User
username = '$DJANGO_SUPERUSER_USERNAME'
password = '$DJANGO_SUPERUSER_PASSWORD'
if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password, email='')
        print(f'Superuser \"{username}\" created.')
    else:
        print(f'Superuser \"{username}\" already exists, skipping.')
else:
    print('DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD not set, skipping.')
"
