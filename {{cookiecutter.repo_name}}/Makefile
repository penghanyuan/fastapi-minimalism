# Makefile
SHELL = /bin/bash

.PHONY: help
help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


# Styling
.PHONY: style
style:
	black .
	flake8
	python3 -m isort .

.PHONY: clean clean-pyc clean-build clean-pytest
clean: clean-build clean-pyc clean-pytest ## remove all build, test, coverage, and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-pytest: ## remove pytest artifacts
	rm -fr .pytest_cache
	rm -f .coverage
	
# dev
.PHONY: dev
dev:
	python3 -m venv .venv
	source .venv/bin/activate && pip install -e ".[dev]"

.PHONY: git-init
git-init:
	git init -b main
	pre-commit install

.PHONY: pre-commit
pre-commit:
	pre-commit run --all-files

