.PHONY: run dev install clean

run:
	poetry run fastapi dev main.py

dev:
	poetry run fastapi dev main.py

install:
	poetry install

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
