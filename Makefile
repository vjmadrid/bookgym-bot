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


# Os Configuration

ifeq ($(OS),Windows_NT)
    OS_DETECTED := Windows
else
    OS_DETECTED := $(shell uname)
endif

# General Configuration

ifeq ($(OS_DETECTED),Windows)
EXECUTION_DIRECTORY_BY_ENVIRONMENT := Scripts
else
EXECUTION_DIRECTORY_BY_ENVIRONMENT := bin
endif

.DEFAULT_GOAL := help

SHELL := /$(EXECUTION_DIRECTORY_BY_ENVIRONMENT)/bash
VIRTUAL_LOCAL_ENV_NAME := venv

EXECUTION_PATH := $(VIRTUAL_LOCAL_ENV_NAME)/$(EXECUTION_DIRECTORY_BY_ENVIRONMENT)

PYTHON := $(EXECUTION_PATH)/python
PIP := $(EXECUTION_PATH)/pip


# App Configuration

ENVIRONMENT := N/A
START_FILE := app.py
PORT := N/A



# Docker Configuration

DOCKER_PATH := $(shell which docker)
DOCKER_VERSION_NUMBER := $(shell docker --version)
DOCKER_PORT := 8081

IMAGE_NAME := acme/cbookgym-bot
CONTAINER_NAME := bookgym-bot

IMAGE_DATE := $(shell date -j "+%Y%m%d%H%M")
IMAGE_NAME_DATED := "${IMAGE_NAME}-$(IMAGE_DATE)"

DOCKER_FILE_NAME := Dockerfile.gunicorn

DOCKER_RUN_PARAMETER := -p ${DOCKER_PORT}:$(PORT) -e FLASK_ENV="${ENVIRONMENT}"


# Plugins Configuration

BLACK_PARAMETER_DEBUG := -v
BLACK_PARAMETER :=

PYLINT_PARAMETER_DEBUG := -j 0 --output-format=colorized
PYTLINT_PARAMETER := $(PYLINT_PARAMETER_DEBUG)

AUTOFLAKE_PARAMETER_DEBUG := 
AUTOFLAKE_PARAMETER := --remove-all-unused-imports --recursive --remove-unused-variables --in-place --exclude=__init__.py

PYTEST_PARAMETER_CONSOLE := -s
PYTEST_PARAMETER_SETUP := --setup-show

PYTEST_PARAMETER_DEBUG := $(PYTEST_PARAMETER_CONSOLE)
PYTEST_PARAMETER := -ra -vv $(PYTEST_PARAMETER_DEBUG)

ISORT_PARAMETER_DEBUG := 
ISORT_PARAMETER := --profile black


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
	@make generate-requirements-deps-full

generate-requirements-deps: ##Generate 'requirements.txt' file (With versions) in the Local Virtual Environment
	$(PIP) freeze | grep -v -- '^-e' > requirements.txt

generate-requirements-deps-full: ##Generate 'requirements-full.txt' file (With versions + test dependencies) in the Local Virtual Environment
	$(PIP) freeze | grep -v -- '^-e' > requirements-full.txt

reset-deps: ## Reset all requirements in the Local Virtual Environment in the Local Virtual Environment
	$(PIP) freeze | xargs pip uninstall -y

tree: ## Show dependency tree of packages
	$(EXECUTION_PATH)/pipdeptree

tree-json: ## Show dependency tree of packages json
	$(EXECUTION_PATH)/pipdeptree --json-tree

tree-graph: ## Show dependency tree of packages graph -> ./reports/dependencies.png
	$(EXECUTION_PATH)/pipdeptree --graph-output png > ./reports/dependencies.png





# *** FORMAT ***

format: ##Format Code with check lint and static code
	@echo -e ""
	@echo -e "$(COLOR_GREEN)black execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(EXECUTION_PATH)/black --version
	@echo -e "$(COLOR_CYAN)* Apply black on '$(START_FILE)'$(COLOR_OFF)"
	$(EXECUTION_PATH)/black $(BLACK_PARAMETER) $(START_FILE) 
	@echo -e "$(COLOR_CYAN)* Apply black on 'src'$(COLOR_OFF)"
	$(EXECUTION_PATH)/black $(BLACK_PARAMETER) src
	@echo -e "$(COLOR_CYAN)* Apply black on 'configs'$(COLOR_OFF)"
	$(EXECUTION_PATH)/black $(BLACK_PARAMETER) configs
	@echo -e "$(COLOR_CYAN)* Apply black on 'tests'$(COLOR_OFF)"
	$(EXECUTION_PATH)/black $(BLACK_PARAMETER) tests

	@echo -e "\n$(COLOR_GREEN)autoflake execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)Use direct configuration$(COLOR_OFF)"
	$(EXECUTION_PATH)/autoflake --version
	@echo -e "$(COLOR_CYAN)* Apply autoflake on '$(START_FILE)'$(COLOR_OFF)"
	$(EXECUTION_PATH)/autoflake $(AUTOFLAKE_PARAMETER) $(START_FILE)
	@echo -e "$(COLOR_CYAN)* Apply autoflake on 'src'$(COLOR_OFF)"
	$(EXECUTION_PATH)/autoflake $(AUTOFLAKE_PARAMETER) ./src
	@echo -e "$(COLOR_CYAN)* Apply autoflake on 'configs'$(COLOR_OFF)"
	$(EXECUTION_PATH)/autoflake $(AUTOFLAKE_PARAMETER) ./configs
	@echo -e "$(COLOR_CYAN)* Apply autoflake on 'tests'$(COLOR_OFF)"
	$(EXECUTION_PATH)/autoflake $(AUTOFLAKE_PARAMETER) ./tests

	@echo -e "\n$(COLOR_GREEN)isort execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)* Apply isort on '$(START_FILE)'$(COLOR_OFF)"
	$(EXECUTION_PATH)/isort $(ISORT_PARAMETER) $(START_FILE)
	@echo -e "$(COLOR_CYAN)* Apply isort on 'all'$(COLOR_OFF)"
	$(EXECUTION_PATH)/isort $(ISORT_PARAMETER) .
	@echo -e "\n"



format-check: ##Check Format Code
	@echo -e ""
	@echo -e "$(COLOR_GREEN)black execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(EXECUTION_PATH)/black --version
	@echo -e "$(COLOR_CYAN)* Apply on 'src'$(COLOR_OFF)"
	$(EXECUTION_PATH)/black $(BLACK_PARAMETER) src --check
	@echo -e "$(COLOR_CYAN)* Apply on 'configs'$(COLOR_OFF)"
	$(EXECUTION_PATH)/black $(BLACK_PARAMETER) configs --check
	@echo -e "$(COLOR_CYAN)* Apply on 'tests'$(COLOR_OFF)"
	$(EXECUTION_PATH)/black $(BLACK_PARAMETER) tests --check
	@echo -e "\n"

lint-pylint: ##Lint Code with pylint on 'all'
	@echo -e ""
	@echo -e "$(COLOR_GREEN)pylint execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(EXECUTION_PATH)/pylint --version
	@echo -e "$(COLOR_CYAN)* Apply on 'all'$(COLOR_OFF)"
	$(EXECUTION_PATH)/pylint $(PYTLINT_PARAMETER) src configs tests
	@echo -e "\n"

lint-pylint-src: ##Lint Code with pylint on 'src'
	@echo -e ""
	@echo -e "$(COLOR_GREEN)pylint execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(EXECUTION_PATH)/pylint --version
	@echo -e "$(COLOR_CYAN)* Apply on 'src'$(COLOR_OFF)"
	$(EXECUTION_PATH)/pylint $(PYTLINT_PARAMETER) src
	@echo -e "\n"

lint-pylint-configs: ##Lint Code with pylint on 'configs'
	@echo -e ""
	@echo -e "$(COLOR_GREEN)pylint execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(EXECUTION_PATH)/pylint --version
	@echo -e "$(COLOR_CYAN)* Apply on 'configs'$(COLOR_OFF)"
	$(EXECUTION_PATH)/pylint $(PYTLINT_PARAMETER) configs
	@echo -e "\n"

lint-pylint-tests: ##Lint Code with pylint on 'tests'
	@echo -e ""
	@echo -e "$(COLOR_GREEN)pylint execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)Use configuration via a file -> pyproject.toml$(COLOR_OFF)"
	$(EXECUTION_PATH)/pylint --version
	@echo -e "$(COLOR_CYAN)* Apply on 'tests'$(COLOR_OFF)"
	$(EXECUTION_PATH)/pylint $(PYTLINT_PARAMETER) tests
	@echo -e "\n"

lint-flake8: ##flake8 Lint Code
	@echo -e ""
	@echo -e "$(COLOR_GREEN)flake8 execution ...$(COLOR_OFF)"
	$(EXECUTION_PATH)/flake8 --version
	$(EXECUTION_PATH)/flake8 $(START_FILE)
	$(EXECUTION_PATH)/flake8 src
	$(EXECUTION_PATH)/flake8 configs
	$(EXECUTION_PATH)/flake8 tests





# *** TEST ***

test: clean ##Run all tests of all types
	@echo -e ""
	@echo -e "$(COLOR_GREEN)pytest execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)* Apply on 'all'$(COLOR_OFF)"
	$(EXECUTION_PATH)/pytest $(PYTEST_PARAMETER) -v

test-unit: clean ##Runs all tests of the "unit" type
	@echo -e ""
	@echo -e "$(COLOR_GREEN)pytest execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)* Apply on 'unit'$(COLOR_OFF)"
	$(EXECUTION_PATH)/pytest $(PYTEST_PARAMETER) -v tests/unit/

test-lint: ##Lint and static-check code
	@echo -e ""
	@echo -e "$(COLOR_GREEN)pytest + flake8 execution ...$(COLOR_OFF)"
	$(EXECUTION_PATH)/pytest --cache-clear --flake8

test-coverage: ##Run tests with coverage
	@echo -e ""
	@echo -e "$(COLOR_GREEN)coverage execution ...$(COLOR_OFF)"
	$(EXECUTION_PATH)/coverage --version
	$(EXECUTION_PATH)/coverage erase
	$(EXECUTION_PATH)/coverage run --include=src/* -m pytest -ra
	$(EXECUTION_PATH)/coverage report -m
	$(EXECUTION_PATH)/coverage html -d ./reports/coverage_html

test-lab: clean ##TEST LAB (Run specifict test)
	@echo -e ""
	@echo -e "$(COLOR_GREEN)pytest execution ...$(COLOR_OFF)"
	@echo -e "$(COLOR_CYAN)* Apply on 'all'$(COLOR_OFF)"
	$(EXECUTION_PATH)/pytest $(PYTEST_PARAMETER) -v ./tests/unit/mongodb/test_simple_mongodb_connection_settings.py
	#$(EXECUTION_PATH)/pytest $(PYTEST_PARAMETER) -v ./tests/unit/common/util/folder/test_folder_util.py





# *** SECURITY ***

security-bandit-check: ## Check security code (with pyproject.toml config file)
	@echo -e ""
	@echo -e "$(COLOR_GREEN)bandit execution ...$(COLOR_OFF)"
	$(EXECUTION_PATH)/bandit --version
	@echo -e "$(COLOR_CYAN)* Apply on 'src'$(COLOR_OFF)"
	$(EXECUTION_PATH)/bandit -r src

security-bandit-check-all: ## Check security ALL code (with pyproject.toml config file)
	@echo -e ""
	@echo -e "$(COLOR_GREEN)bandit execution ...$(COLOR_OFF)"
	$(EXECUTION_PATH)/bandit --version
	@echo -e "$(COLOR_CYAN)* Apply on 'ALL'$(COLOR_OFF)"
	$(EXECUTION_PATH)/bandit -r .

security-safety-check: ## Check security code with safety (local)
	@echo -e "\n$(COLOR_GREEN)safety execution ...$(COLOR_OFF)"
	$(EXECUTION_PATH)/safety check

security-safety-dev-requirements-check: ## Check security code with safety (dev-requirements.txt)
	@echo -e "\n$(COLOR_GREEN)safety execution ...$(COLOR_OFF)"
	$(EXECUTION_PATH)/safety check -r dev-requirements.txt

security-safety-requirements-check: ## Check security code with safety (requirements.txt)
	@echo -e "\n$(COLOR_GREEN)safety execution ...$(COLOR_OFF)"
	$(EXECUTION_PATH)/safety check -r requirements.txt





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

docker-clean: ##Execute docker clean
	PARAM=$$(docker ps -q) && docker kill $$PARAM

docker-build: ##Build docker image (default Dockerfile -> Only Flask)
	docker build --no-cache	-t $(IMAGE_NAME) .

docker-build-gunicorn: ##Build docker image ('Dockerfile.gunicorn' Dockerfile -> Flask + Gunicorn)
	docker build --no-cache	-t $(IMAGE_NAME) -f Dockerfile.gunicorn .

docker-build-param: ##Build docker image with Dockerfile parameter
	docker build -t $(IMAGE_NAME) -f $(DOCKER_FILE_NAME) .

docker-run: ##Execute docker image for default architecture
	@echo -e ""
	@echo -e "Environment : $(COLOR_GREEN)$(ENVIRONMENT)$(COLOR_OFF)"
	@echo -e "Port : $(COLOR_GREEN)$(DOCKER_PORT)$(COLOR_OFF)"
	docker run --name $(CONTAINER_NAME) $(DOCKER_RUN_PARAMETER) -d $(IMAGE_NAME)

docker-stop: ##Execute docker stop
	ID=$$(docker ps -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker stop $$ID

docker-logs: ##Execute docker logs
	ID=$$(docker ps -a -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker logs $$ID

docker-ssh: ##Execute docker image with ssh
	ID=$$(docker ps -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker exec -it $$ID bash

docker-push: ##Push docker image
	docker tag $(IMAGE_NAME) $(IMAGE_NAME_DATED)
	docker push $(IMAGE_NAME)
	docker push $(IMAGE_NAME_DATED)

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