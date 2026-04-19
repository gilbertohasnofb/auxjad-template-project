PYTHON := .venv/bin/python

.PHONY: black-check black-reformat check flake8 isort-check isort-reformat pydocstyle reformat setup

# Setup
.venv/.installed: title/requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r title/requirements.txt
	touch .venv/.installed
setup: .venv/.installed

# Formatting and linting
black-check: setup
	$(PYTHON) -m black . --check
black-reformat: setup
	$(PYTHON) -m black .
flake8: setup
	$(PYTHON) -m flake8
isort-check: setup
	$(PYTHON) -m isort --check-only --diff .
isort-reformat: setup
	$(PYTHON) -m isort .
pydocstyle: setup
	$(PYTHON) -m pydocstyle
check: black-check flake8 isort-check pydocstyle
reformat: black-reformat isort-reformat
