.DEFAULT_GOAL := default_target

PIP := pip install -r

PROJECT_NAME := python_rabbitmq_streams
PYTHON_VERSION := 3.11.9
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

# Environment setup
.pip:
	pip uninstall -y typing
	pip install --upgrade pip

setup: .pip
	$(PIP) requirements.txt

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv local $(PYTHON_VERSION)
	-python -m venv venv


create-venv: .create-venv setup

code-convention:
	flake8
	pycodestyle


activate-venv:
	.\venv\Scripts\activate

containers-up:
	docker-compose up
