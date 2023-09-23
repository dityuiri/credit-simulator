PYTHON=python
ARGS=$(filter-out $@,$(MAKECMDGOALS))

prepare:
	pip install -r requirements.txt

run:
	$(PYTHON) main.py

run-with-args:
	$(PYTHON) main.py $(ARGS)

test:
	$(PYTHON) -m unittest discover -s models/tests -p 'test_*.py' -s controllers/tests -p 'test_*.py' -s views/tests -p 'test_*.py'

test-with-coverage:
	coverage run -m unittest discover -s models/tests -p 'test_*.py' -s controllers/tests -p 'test_*.py' -s views/tests -p 'test_*.py'
	coverage report -m

