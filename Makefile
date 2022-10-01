.PHONY: help docs
.DEFAULT_GOAL := help

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Removing cached python compiled files
	find . -name \*pyc  | xargs  rm -fv
	find . -name \*pyo | xargs  rm -fv
	find . -name \*~  | xargs  rm -fv
	find . -name __pycache__  | xargs  rm -rfv

install: ## Install dependencies for local dev environment
	pip install -r requirements/local.txt

lint: ## Run code linters
	autoflake --remove-all-unused-imports --remove-unused-variables  --ignore-init-module-imports -r easy_api
	black --check easy_api
	isort --check easy_api
	flake8
	mypy easy_api

fmt format: ## Run code formatters
	autoflake --in-place --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports  -r easy_api
	isort easy_api
	black easy_api

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=easy_api --cov-report term

test-cov-full: ## Run tests with coverage term-missing
	pytest --cov=easy_api --cov-report term-missing

bump:
	bumpversion patch

bump-feat:
	bumpversion feat

bump-major:
	bumpversion major

bump-build:
	bumpversion build
