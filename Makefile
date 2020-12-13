SHELL:=/bin/bash

.DEFAULT_GOAL := lint

.PHONY: lint
lint:
	mypy plex_default_settings
	flake8 plex_default_settings setup.py

.PHONY: deps
deps: compile-deps
	pip-sync requirements-test.txt
	pip install -e .

compile-deps: requirements-test.in
	pip-compile --output-file requirements-test.txt setup.py requirements-test.in --no-emit-index-url

.PHONY:
update-tools:
	pip install --upgrade wheel
	pip install --upgrade twine
	pip install --upgrade pip
	pip install --upgrade pip-tools
	pip install --upgrade setuptools
