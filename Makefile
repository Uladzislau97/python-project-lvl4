install:
	@poetry install

run-dev:
	@poetry run python manage.py runserver

run-wsgi:
	export DJANGO_SETTINGS_MODULE=config.settings
	@poetry run gunicorn config.wsgi

migrate:
	@poetry run python manage.py migrate

lint:
	@poetry run flake8 config

check-deploy:
	@poetry run python manage.py check --deploy

setup-requirements:
	@poetry run pip freeze > requirements.txt

deploy: setup-requirements
	git push -f heroku

logs:
	heroku logs --tail