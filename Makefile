#
# Makefile for Project Management
#

# Color Configuration

COLOR_OFF := \033[0m
COLOR_BLACK := \033[0;30m
COLOR_RED := \033[0;31m
COLOR_GREEN := \033[0;32m
COLOR_YELLOW := \033[0;33m
COLOR_BLUE := \033[0;34m
COLOR_PURPLE := \033[0;35m
COLOR_CYAN := \033[0;36m
COLOR_WHITE := \033[0;37m # Text Reset


# App Configuration

SHELL = /bin/bash
.DEFAULT_GOAL := help
VIRTUAL_LOCAL_ENV_NAME := venv
PYTHON := $(VIRTUAL_LOCAL_ENV_NAME)/bin/python
PIP := $(VIRTUAL_LOCAL_ENV_NAME)/bin/pip
START_FILE := app.py
CONTAINER_NAME := bookgym-bot



# Plugins Configuration

BLACK_PARAMETER_DEBUG := -v
BLACK_PARAMETER :=

PYLINT_PARAMETER_DEBUG := -j 0 --output-format=colorized
PYTLINT_PARAMETER := $(PYLINT_PARAMETER_DEBUG)

PYTEST_PARAMETER_CONSOLE := -s
PYTEST_PARAMETER_SETUP := --setup-show

PYTEST_PARAMETER_DEBUG := $(PYTEST_PARAMETER_CONSOLE)
PYTEST_PARAMETER := -ra -vv 


# *** CLEAN ***

clean-build: #Remove elements for build
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '.pytest_cache' -type d | xargs rm -fr
	@find . -name '*.pytest_cache' -type d | xargs rm -fr
	@find . -name '*.pyc' -type d | xargs rm -fr

clean-test: #Remove test and coverage artifacts
	@rm -fr .tox/
	@rm -fr .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache

clean-pyc: #Remove Python file artifacts
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-distribute: #Remove *.egg-info files and *.egg, build and dist directories
	@rm -vrf build/ 
	@rm -vrf dist/ 
	@rm -vrf ./*.tgz 
	@rm -vrf .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean : clean-build clean-pyc clean-test clean-distribute  ## Remove all build, test, coverage and distribute Python artifacts





# *** LOCAL VIRTUAL ENVIRONMENT  ***

init-venv: ##Prepare Local Virtual Environment with requirements.txt (With versions)
	@make create-venv
	@make upgrade-venv
	@make install-deps

init-dev-venv: ##Prepare Local Virtual Environment with dev-requirements.txt (No versions)
	@make create-venv
	@make upgrade-venv
	@make install-dev-deps

create-venv: #Create Virtual Environment
	python3 -m venv $(VIRTUAL_LOCAL_ENV_NAME)
	@make upgrade-venv

upgrade-venv: ##Upgrade Virtual Environment Pip
	$(PIP) install --upgrade pip setuptools wheel

remove-venv: ##Remove Local Virtual Environment
	@rm -rf ./$(VIRTUAL_LOCAL_ENV_NAME)

pip-list-venv: ##Pip list Local Virtual Environment
	$(PIP) list





# *** DEPENDENCIES ***

install-deps: ## Install dependencies 'requirements.txt' file in the Local Virtual Environment
	$(PIP) install -Ur requirements.txt

install-dev-deps: ##Install dependencies 'dev-requirements.txt' file in the Local Virtual Environment
	$(PIP) install -r dev-requirements.txt
	@make generate-requirements-deps

install-test-deps: ##Install dependencies 'test-requirements.txt'
	$(PIP) install -r test-requirements.txt
	@make generate-requirements-deps

generate-requirements-deps: ##Generate 'requirements.txt' file (With versions) in the Local Virtual Environment
	$(PIP) freeze | grep -v -- '^-e' > requirements.txt

reset-deps: ## Reset all requirements in the Local Virtual Environment in the Local Virtual Environment
	$(PIP) freeze | xargs pip uninstall -y

tree: ## Show dependency tree of packages
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pipdeptree

tree-json: ## Show dependency tree of packages json
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pipdeptree --json-tree

tree-graph: ## Show dependency tree of packages graph
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pipdeptree --graph-output png > dependencies.png





# *** FORMAT ***

format: ##Format Code with check lint and static code
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/black --version
	@echo -e "$(COLOR_CYAN)* Apply on 'src'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/black $(BLACK_PARAMETER) app.py
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/black $(BLACK_PARAMETER) src
	@echo -e "$(COLOR_CYAN)* Apply on 'tests'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/black $(BLACK_PARAMETER) tests

format-check: ##Check Format Code
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/black --version
	@echo -e "$(COLOR_CYAN)* Apply on 'src'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/black $(BLACK_PARAMETER) src --check
	@echo -e "$(COLOR_CYAN)* Apply on 'tests'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/black $(BLACK_PARAMETER) tests --check

lint-pylint: ##Lint Code with pylint on 'all'
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pylint --version
	@echo -e "$(COLOR_CYAN)* Apply on 'all'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pylint $(PYTLINT_PARAMETER) src configs tests

lint-pylint-src: ##Lint Code with pylint on 'src'
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pylint --version
	@echo -e "$(COLOR_CYAN)* Apply on 'src'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pylint $(PYTLINT_PARAMETER) src

lint-pylint-configs: ##Lint Code with pylint on 'configs'
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pylint --version
	@echo -e "$(COLOR_CYAN)* Apply on 'configs'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pylint $(PYTLINT_PARAMETER) configs

lint-pylint-tests: ##Lint Code with pylint on 'tests'
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pylint --version
	@echo -e "$(COLOR_CYAN)* Apply on 'tests'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pylint $(PYTLINT_PARAMETER) tests

lint-flake8: ##flake8 Lint Code
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/flake8 --version
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/flake8 src
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/flake8 configs
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/flake8 tests





# *** TEST ***

test: clean ##Run all tests of all types
	@echo -e "$(COLOR_CYAN)* Apply on 'all'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pytest $(PYTEST_PARAMETER) -v

test-unit: clean ##Runs all tests of the "unit" type
	@echo -e "$(COLOR_CYAN)* Apply on 'unit'$(COLOR_OFF)"
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pytest $(PYTEST_PARAMETER) -v tests/unit/

test-lint: ##Lint and static-check code
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pytest --cache-clear --flake8

test-coverage: ##Run tests with coverage
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/coverage --version
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/coverage erase
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/coverage run --include=src/* -m pytest -ra
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/coverage report -m
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/coverage html -d ./reports/coverage_html



# *** SECURITY ***

security-check: ## Check security code (with pyproject.toml config file)
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/bandit --version
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/bandit -r src

security-check-all: ## Check security ALL code (with pyproject.toml config file)
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/bandit --version
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/bandit -r .





# *** INSTALL / UNINSTALL ***

install: clean uninstall ##Install package local
	$(PYTHON) setup.py develop 

uninstall: ##Uninstall package local
	$(PYTHON) setup.py develop --uninstall





# *** DISTRIBUTE ***

dist-package-install: ##Distribute package install
	$(PIP) install -Ue .

dist-install: ##Distribute package install by setup.py
	$(PYTHON) setup.py install

dist-sdist: ##Distribute package mode local (folder : sdist)
	$(PYTHON) setup.py sdist

dist-wheel: ##Distribute package mode local (folder : sdist)
	$(PYTHON) setup.py bdist_wheel
	
dist: clean dist-sdist dist-wheel ##Distribute source and wheel package





# *** RUN  ***

run: ## Run Application
	PYTHONPATH=src $(PYTHON) $(START_FILE) --email=$(email) --password=$(password) --booking-goals=$(booking-goals) --box-name=$(box-name) --box-id=$(box-id) --days-in-advance=$(days-in-advance)



# *** DOCKER ***

docker-build: ##Build docker image for default architecture 
	docker build --no-cache	-t $(CONTAINER_NAME) .

docker-tests:
	docker exec $(CONTAINER_NAME) /bin/sh -c 'make tests'




# *** HELP ***


help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [target]"; \
	printf "%-40s %s\n" "target" "help" ; \
	printf "%-40s %s\n" "----------------------------------" "----------------------------------" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-40s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
	@echo "Check the Makefile to know exactly what each target is doing"


.PHONY: init test