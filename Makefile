install:
	@poetry install

docker-install:
	docker-compose run django sh -c "make install"

.env:
	@test ! -f .env && cp .env.example .env

makemigrations:
	@poetry run python manage.py makemigrations

docker-makemigrations:
	docker-compose run django sh -c "make makemigrations"

production-makemigrations:
	heroku run python manage.py makemigrations

migrate:
	@poetry run python manage.py migrate

docker-migrate:
	docker-compose run django sh -c "make migrate"

production-migrate:
	heroku run python manage.py migrate

start: migrate
	@poetry run python manage.py runserver 0.0.0.0:8000

docker-start:
	docker-compose up

setup: migrate
	@poetry run python manage.py createsuperuser

docker-setup:
	docker-compose run django sh -c "make setup"

production-setup: production-migrate
	heroku run python manage.py createsuperuser

shell:
	@poetry run python manage.py shell

docker-shell:
	docker-compose run django sh -c "make shell"

production-shell:
	heroku run python manage.py shell

collectstatic:
	@poetry run python manage.py collectstatic --noinput

docker-collectstatic:
	docker-compose run django sh -c "make collectstatic"

production-collectstatic:
	heroku run python manage.py collectstatic --noinput

lint:
	@poetry run flake8 config

test:
	@poetry run python manage.py test

docker-test:
	docker-compose run django sh -c "make test"

check: lint test

coverage:
	@poetry run coverage run --source='.' manage.py test
	@poetry run coverage xml

check-deploy:
	@poetry run python manage.py check --deploy

setup-requirements:
	@poetry run pip freeze > requirements.txt

deploy: setup-requirements production-migrate production-collectstatic
	git push heroku master

logs:
	heroku logs --tail