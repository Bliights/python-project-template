# -------------- Install dependencies --------------
install:
	@echo Install the dependencies with uv and pre commit...
	$ uv sync
	$ uv run pre-commit install	

update:
	@echo Updating all dependencies of the environment...
	$ uv lock --upgrade
	$ uv sync

# ------------------ Formating ---------------------
lint:
	@echo Check with ruff...
	$ uv run ruff check .

format:
	@echo Format with Ruff...
	$ uv run ruff format .

fix:
	@echo Fix with Ruff...
	$ uv run ruff check --fix .

# ------------------- Pre-commit -------------------
pre-commit:
	@echo Run pre-commit...
	$ uv run pre-commit run --all-files

# ---------------------- Test ----------------------
test:
	@echo Running tests with pytest...
	uv run pytest -v

# -------------------- Scripts ---------------------
test-script:
	uv run python -m src.scripts.test