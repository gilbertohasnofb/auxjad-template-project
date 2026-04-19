.PHONY: black-check black-reformat flake8 isort-check isort-reformat pydocstyle check reformat

black-check:
	@. .venv/bin/activate && python3 -m black . --check

black-reformat:
	@. .venv/bin/activate && python3 -m black .

flake8:
	@. .venv/bin/activate && python3 -m flake8

isort-check:
	@. .venv/bin/activate && python3 -m isort --check-only --diff .

isort-reformat:
	@. .venv/bin/activate && python3 -m isort .

pydocstyle:
	@. .venv/bin/activate && python3 -m pydocstyle

check:
	$(MAKE) black-check
	$(MAKE) flake8
	$(MAKE) isort-check
	$(MAKE) pydocstyle

reformat:
	$(MAKE) black-reformat
	$(MAKE) isort-reformat