
dev: setup
	. venv/bin/activate && watchfiles "python src/main.py"

start: setup
	. venv/bin/activate && python src/main.py

setup: 
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

venv: 
	python3 -m venv venv

lint: setup
	. venv/bin/activate && mypy src/main.py