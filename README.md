# django_rest_example
Django/DRF rest application example.

Create virtualenv

    cd /var/envs && mkvirtualenv --python=/usr/bin/python3 django_rest_example


Install requirements for a project.

    cd /var/www/django_rest_example && pip install -r requirements/local.txt

Make migrations and migrate

    python manage.py makemigrations
    python manage.py migrate
