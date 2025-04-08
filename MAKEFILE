project:
	django-admin startproject $(name) $(dir)

server:
	python manage.py runserver

app:
	python manage.py startapp $(name)

mk:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell

flush:
	python manage.py flush

super:
	python manage.py createsuperuser 

pipu:
	pip install --upgrade pip

depnd:
	pip install django mysqlclient python-dotenv black psycopg2 pillow
	
rest:
	pip install djangorestframework djangorestframework-simplejwt django-filter dj-rest-auth django-allauth requests

deploy:
	pip install whitenoise gunicorn

require:
	pip freeze > requirements.txt

format:
	black $(dir)