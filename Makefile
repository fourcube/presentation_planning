run:
	python manage.py runserver

migrate_all:
	python manage.py makemigrations
	python manage.py makemigrations create
	python manage.py migrate
	python manage.py migrate create
