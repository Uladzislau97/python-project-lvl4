install:
	@poetry install

.env:
	@test ! -f .env && cp .env.example .env

migrate:
	@poetry run python manage.py migrate

start: migrate
	@poetry run python manage.py runserver 0.0.0.0:8000

setup: migrate
	@echo Create a super user
	@poetry run python manage.py createsuperuser

shell:
	@poetry run python manage.py shell

collectstatic:
	@poetry run python manage.py collectstatic --no-inputs

lint:
	@poetry run flake8 config

test:
	@poetry run python manage.py test

check: lint test

coverage:
	@poetry run coverage run --source='.' manage.py test
	@poetry run coverage xml

check-deploy:
	@poetry run python manage.py check --deploy

setup-requirements:
	@poetry run pip freeze > requirements.txt

deploy: setup-requirements
	git push heroku master

logs:
	heroku logs --tail