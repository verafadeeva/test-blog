all: poetry poetry-sh migration run

poetry:
	poetry install --no-root

poetry-sh:
	poetry shell

migration: poetry-sh
	./manage.py migrate

run: migration
	./manage.py runserver