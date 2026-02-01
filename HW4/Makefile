PIP := venv/bin/pip
PYTHON3 := venv/bin/python3
TESTS := venv/bin/pytest -v ./test_controllers.py

.PHONY: clear venv install_requirements run test

clear:
	rm -rf venv
	rm -rf __pycache__
	rm -rf *.pyc

venv:
	python3 -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} server.py

test:
	${TESTS}

all: venv install_requirements