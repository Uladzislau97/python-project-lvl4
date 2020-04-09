install:
	@poetry install

dev:
	python root/manage.py runserver 3000

lint:
	@poetry run flake8 root

migrate:
	python root/manage.py migrate