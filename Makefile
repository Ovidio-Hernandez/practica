.PHONY: test lint run

test:
	uv run pytest -v

lint:
	uv run ruff format .
	uv run ruff check .

run:
	uv run python -i -c "from practica.modelos import *"