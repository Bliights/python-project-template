# Python Project Template

A modern, clean, and efficient boilerplate for starting new Python projects with reliable tooling and best practices baked in from the start. This template integrates:

- ⚡ `uv` for fast dependency management
- 🧹 `Ruff` for linting and formatting
- 🔎 `ty` for static type checking
- 🪝 `pre-commit` for automated code-quality checks
- 🚀 `pre-push` hooks for final validation before pushing
- 📋 `pytest` for testing
- 🧰 A complete set of `Makefile` commands for a simple and consistent workflow

and ensures:

- 🔧 Code is automatically formatted
- 🔎 Type errors are detected with ty
- 🚫 Bad code never reaches the repository (thanks to pre-commit)
- 🧪 Tests are run before pushing
- 📦 Dependencies are clean, reproducible, and always up-to-date
- 🧑‍💻 You focus on building — not configuring tools

## Getting Started

### 1. Install dependencies
Install all required libraries in a virtual environment and configure the Git `pre-commit` and `pre-push` hooks:
```bash
$ make install
```

### 2. Managing Dependencies
Add Python packages with `uv`, and when you want to upgrade everything (lockfile, environment, and `pre-commit`/`pre-push` hooks) you can just run this command:
```bash
$ make upgrade
```

### 3. Code quality
To validate and enforce code quality (linting, formatting, etc.) across the entire project, use the dedicated `pre-commit` and `pre-push` checks:
```bash
$ make pre-commit
$ make pre-push
```
- `pre-commit` runs the fast checks used during development, such as linting, formatting, type checking, and secret detection.

- `pre-push` runs the final validation checks before pushing, including the test suite and dependency consistency checks.

You can also use the dedicated `Makefile` commands for more granular control:
```bash
$ make lint         # Check style and static analysis with Ruff
$ make format       # Format code with Ruff
$ make fix          # Auto-fix issues detected by Ruff
$ make type-check   # Run static type checking with ty
```
Together, these commands ensure your codebase remains clean, consistent, and free of common errors, while enforcing project-wide standards.

### 4. Running Tests
Execute the entire test suite using `pytest`:
```bash
$ make test
```

### 5. Reusing the project as a package
If you want to use the project as a package in another project, you can install it directly from the repository using its URL. For example, using this repository:
```bash
$ uv add git+https://github.com/Bliights/python-project-template
```
or
```bash
$ pip install git+https://github.com/Bliights/python-project-template
```