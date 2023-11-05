all: poetry poetrysh migration

poetry:
	poetry install

poetrysh:
	poetry shell

migration:
	./manage.py migrate