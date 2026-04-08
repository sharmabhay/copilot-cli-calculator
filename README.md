# 🧮 Calculator

A Python calculator app with a CLI and Streamlit web UI, built with [UV](https://docs.astral.sh/uv/).

## Features

- **Basic arithmetic** — add, subtract, multiply, divide, power, modulo, floor divide
- **Unary functions** — `sqrt`, `fact` (factorial)
- **Expression parsing** — e.g. `2 + 3`, `sqrt(16)`, `fact(5)`
- **Web UI** — Streamlit app with Basic, Advanced, and Expression tabs

## Quick Start

```bash
# Install dependencies
uv sync

# Run the CLI
uv run python -m calculator

# Run the web UI
uv run python -m streamlit run calculator/app.py
```

## Project Structure

```
calculator/
├── operations.py   # Pure math functions (no I/O)
├── parser.py       # Expression parsing (no I/O)
├── app.py          # Streamlit web UI
└── __main__.py     # CLI entry point (only module with I/O)
tests/
├── test_operations.py
├── test_parser.py
└── test_app.py
```

## Development

```bash
# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_operations.py::test_add

# Lint and format check
uv run ruff check . && uv run ruff format --check .

# Full pre-commit check
uv run ruff check . && uv run ruff format --check . && uv run pytest
```

## Conventions

- **UV** — always use `uv run` to execute commands; add deps with `uv add <package>`
- **Commits** — follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `test:`)
- **Errors** — raise `ValueError` with descriptive messages for invalid inputs
