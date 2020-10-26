install:
	pip install -e .['dev']

flask:
	export FLASK_ENV=development
	export FLASK_APP=mysite/app.py
	flask run
