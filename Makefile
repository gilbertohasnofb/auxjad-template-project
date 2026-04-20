PYTHON := .venv/bin/python

.PHONY: black-check black-reformat clean check flake8 isort-check isort-reformat pydocstyle \
		reformat setup

# Setup
.venv/.installed: title/requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r title/requirements.txt
	touch .venv/.installed
setup: .venv/.installed

# Formatting and linting
black-check:
	$(PYTHON) -m black . --check
black-reformat:
	$(PYTHON) -m black .
flake8:
	$(PYTHON) -m flake8
isort-check:
	$(PYTHON) -m isort --check-only --diff .
isort-reformat:
	$(PYTHON) -m isort .
pydocstyle:
	$(PYTHON) -m pydocstyle
check: black-check flake8 isort-check pydocstyle
reformat: black-reformat isort-reformat

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete && find . -type d -name "__pycache__" -delete