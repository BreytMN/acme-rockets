PROJECT = acme-rockets
PYTHON_VERSION = 3.12

.PHONY: all help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

python: ## Install and config python
	@sudo apt update
	@sudo apt update && sudo apt upgrade -y
	@sudo apt install software-properties-common -y
	@sudo add-apt-repository ppa:deadsnakes/ppa
	@sudo apt install python-is-python3
	@sudo apt install python$(PYTHON_VERSION)
	@sudo apt install python$(PYTHON_VERSION)-venv
	@python$(PYTHON_VERSION) -m ensurepip
	@sudo update-alternatives --install /usr/bin/python python /usr/bin/python$(PYTHON_VERSION) $(subst .,,$(PYTHON_VERSION))

venv: ## Create virtual env
	@rm -rf .venv/ && python -m venv .venv && . .venv/bin/activate; \
	pip install --upgrade pip; \
	pip install uv; \
	uv pip install \
		-r requirements.txt \
		-r requirements_dev.txt \
		-r requirements_test.txt; \
	pre-commit install; \
	tailwindcss_install;

server-venv: ## Start server with venv in watch mode - any change in *.py and *.html files will trigger server reload
	@. .venv/bin/activate; \
	uvicorn app.main:app --reload --reload-include *.html;

server-docker: ## Start server with docker
	@docker rm -f $(PROJECT) || true; \
	docker compose up --build;

server: server-venv

test: ## Run unit tests
	@. .venv/bin/activate; \
	clear && python -m pytest \
		--cov-report=term-missing \
		--cov=app tests;