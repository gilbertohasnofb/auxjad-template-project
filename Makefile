.PHONY: black-check black-reformat flake8 isort-check isort-reformat pydocstyle check reformat

# Formatting and linting
black-check:
	python3 -m black . --check
black-reformat:
	python3 -m black .
flake8:
	python3 -m flake8
isort-check:
	python3 -m isort --check-only --diff .
isort-reformat:
	python3 -m isort .
pydocstyle:
	python3 -m pydocstyle
check:
	$(MAKE) black-check
	$(MAKE) flake8
	$(MAKE) isort-check
	$(MAKE) pydocstyle
reformat:
	$(MAKE) black-reformat
	$(MAKE) isort-reformat