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

test:
	@poetry run python manage.py test

coverage:
	@poetry run coverage run --source='.' manage.py test
	@poetry run coverage report

check-deploy:
	@poetry run python manage.py check --deploy

setup-requirements:
	@poetry run pip freeze > requirements.txt

deploy: setup-requirements
	git push heroku master

logs:
	heroku logs --tail