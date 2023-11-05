all: poetry poetry-sh migration run

poetry:
	poetry install --no-root

poetry-sh:
	poetry shell

migration:
	./manage.py migrate

run:
	./manage.py runserver