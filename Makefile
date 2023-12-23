
dev: setup
	poetry run watchfiles "python rick_morty_py/main.py"

start: setup
	poetry run start

setup: 
	poetry install

lint: setup
	poetry run mypy rick_morty_py