install:
	pip install -r requirements.txt

dev:
	python root/manage.py runserver 3000

lint:
	flake8 root

migrate:
	python root/manage.py migrate