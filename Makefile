.PHONY: run install clean

run:
	poetry run uvicorn main:app --reload

install:
	poetry install

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
