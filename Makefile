all: poetry poetry-sh migration

poetry:
	poetry install

poetry-sh:
	poetry shell

migration:
	./manage.py migrate