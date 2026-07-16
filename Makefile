.PHONY: install run test format lint clean

install:
	pip install -r requirements-dev.txt

run:
	python -m src.main

test:
	pytest

format:
	black src tests
	isort src tests

lint:
	flake8 src tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +