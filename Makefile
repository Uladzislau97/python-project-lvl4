install:
	@poetry install

run:
	python root/manage.py runserver 3000

lint:
	@poetry run flake8 root