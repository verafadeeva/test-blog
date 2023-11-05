all: poetry migration run

poetry:
	poetry install --no-root

migration:
	./manage.py migrate

run:
	./manage.py runserver