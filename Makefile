.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")


.PHONY: help
help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: show
show:             ## Show the current environment.
	@echo "Current environment:"
	@echo "Running using $(ENV_PREFIX)"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site


.PHONY: virtualenv
virtualenv:       ## Create a virtual environment.
	@echo "creating virtualenv ..."
	@rm -rf .venv
	@python3 -m venv .venv
	@./.venv/bin/pip install -U pip
	@./.venv/bin/pip install -e .[test]
	@echo
	@echo "!!! Please run 'source .venv/bin/activate' to enable the environment !!!"


.PHONY: install
install:          ## Install the project in dev mode.
	@echo "Don't forget to run 'make virtualenv' if you got errors."
	$(ENV_PREFIX)pip install -e .[test]


.PHONY: install_ipykernel
install_ipykernel:  ## Install the current venv as an ipython kernel
	$(ENV_PREFIX)python -m ipykernel install --name threebee_venv --user
	@echo "Installed ipython kernel threebees_venv"


.PHONY: fmt
fmt:              ## Format code using black & isort.
	$(ENV_PREFIX)isort threebee/
	$(ENV_PREFIX)black -l 79 threebee/
	$(ENV_PREFIX)black -l 79 tests/


.PHONY: test
test:         ## Run tests and generate coverage report.
	$(ENV_PREFIX)pytest -v --cov-config .coveragerc --cov=threebee -l --tb=short --maxfail=1 tests/
	$(ENV_PREFIX)coverage xml
	$(ENV_PREFIX)coverage html


.PHONY: clean
clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build



# This project has been generated from rochacbruno/python-project-template
# __author__ = 'rochacbruno'
# __repo__ = https://github.com/rochacbruno/python-project-template
# __sponsor__ = https://github.com/sponsors/rochacbruno/
