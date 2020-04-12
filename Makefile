install:
	pip install -r requirements.txt

run:
	python root/manage.py runserver 8000

lint:
	flake8 root

migrate:
	python root/manage.py migrate

check-deploy:
	python root/manage.py check --deploy

logs:
	heroku logs --tail

deploy:
	git push -f heroku