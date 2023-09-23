SHELL := /bin/bash
PYTHON := python
ARGS=$(filter-out $@,$(MAKECMDGOALS))

prepare:
	pip install -r requirements.txt

run:
	$(PYTHON) main.py $(input_file)

test:
	$(PYTHON) -m unittest discover -s models/tests controllers/tests views/tests -p 'test_*.py'

test-with-coverage:
	coverage run -m unittest discover -s models/tests controllers/tests views/tests -p 'test_*.py'
	coverage report -m

build-docker:
	docker build -t credit-simulator .

run-docker:
	docker run -i credit-simulator