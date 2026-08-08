.PHONY: install update lint format fix type-check pre-commit pre-push test test-script

# ---------------- Install dependencies ----------------
install:
	@echo "Installing dependencies and Git hooks..."
	uv sync
	uv run pre-commit install

update:
	@echo "Updating dependencies and pre-commit hooks..."
	uv lock --upgrade
	uv sync
	uv run pre-commit autoupdate

# --------------------- Formatting ----------------------
lint:
	@echo "Checking code with Ruff..."
	uv run ruff check .

format:
	@echo "Formatting code with Ruff..."
	uv run ruff format .

fix:
	@echo "Fixing code with Ruff..."
	uv run ruff check --fix .

# -------------------- Type checking --------------------
type-check:
	@echo "Checking types with ty..."
	uv run ty check

# --------------------- Pre-commit ----------------------
pre-commit:
	@echo "Running all pre-commit checks..."
	uv run pre-commit run --all-files --hook-stage pre-commit

# ---------------------- Pre-push -----------------------
pre-push:
	@echo "Running all pre-push checks..."
	uv run pre-commit run --all-files --hook-stage pre-push

# ------------------------ Tests ------------------------
test:
	@echo "Running tests with pytest..."
	uv run pytest -v

# ----------------------- Scripts -----------------------
test-script:
	uv run python -m src.scripts.test