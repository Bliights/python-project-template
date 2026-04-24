# Python Project Template

A modern, clean, and efficient boilerplate for starting new Python projects with reliable tooling and best practices baked in from the start. This template integrates:

- ⚡ ```uv``` for fast dependency management
- 🧹 ```Ruff``` for linting and formatting
- 🪝 ```pre-commit``` hooks for automated code quality and automatic requirements generation
- 📋 ```pytest``` for testing
- 🧰 A full set of ```Makefile``` commands for easy project workflow

and ensures:

- 🔧 Code is automatically formatted
- 🚫 Bad code never reaches the repository (thanks to pre-commit)
- 📦 Dependencies are clean, reproducible, and always up-to-date
- 🧑‍💻 You focus on building — not configuring tools

## Getting Started

### 1. Install dependencies
Install all required libraries in a virtual environment and enable ```pre-commit``` hooks:
```bash
$ make install
```

### 2. Managing Dependencies
Add Python packages with ```uv```, and when you want to upgrade everything (lockfile + env) you can just run this command:
```bash
$ make upgrade
```

### 3. Code quality
To validate and enforce code quality (linting, formatting, etc.) across the entire project, run all ```pre-commit``` checks:
```bash
$ make pre-commit
```
You can also use the dedicated ```Makefile``` commands for more granular control:
```bash
$ make lint     # Check style and static analysis with Ruff
$ make format   # Format code with Ruff
$ make fix      # Auto-fix issues detected by Ruff
```
Together, these commands ensure your codebase remains clean, consistent, and free of common errors, while enforcing project-wide standards.

### 4. Running Tests
Execute the entire test suite using ```pytest```:
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