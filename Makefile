SHELL:=/bin/bash

.DEFAULT_GOAL := lint

.PHONY: clean
clean:
	rm -rf build/ dist/ *.egg-info/

.PHONY: lint
lint:
	mypy plex_default_settings
	flake8 plex_default_settings setup.py

.PHONY: build
build: clean
	python setup.py sdist bdist_wheel

.PHONY: publish
publish:
	twine upload dist/*

.PHONY: deps
deps: requirements-test.txt
	pip-sync requirements-test.txt
	pip install -e .

requirements-test.txt: requirements-test.in setup.py
	pip-compile --output-file requirements-test.txt setup.py requirements-test.in --no-emit-index-url

.PHONY:
update-tools:
	pip install --upgrade wheel
	pip install --upgrade twine
	pip install --upgrade pip
	pip install --upgrade pip-tools
	pip install --upgrade setuptools
