poetry: poetry-inst
	poetry shell

poetry-inst:
	poetry install --no-root

migration:
	./manage.py migrate

run: migration
	./manage.py runserver