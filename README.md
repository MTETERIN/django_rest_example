# django_rest_example

<h1 align="center">
	<img width="400" src="https://cdn.rawgit.com/sindresorhus/awesome/master/media/logo.svg" alt="Awesome">
</h1>

Django/DRF rest application example with PostgreSQL and RabbitMQ.

Create virtualenv

    cd /var/envs && mkvirtualenv --python=/usr/bin/python3 django_rest_example


Install requirements for a project.

    cd /var/www/django_rest_example && pip install -r requirements/local.txt

Make migrations and migrate

    python manage.py makemigrations
    python manage.py migrate

Request example

    response = requests.get(
        url="http://127.0.0.1:8000/api/v0/api-key/",
        headers={
            "Api-Key": "<YOUR_API_KEY>",
        },
    )