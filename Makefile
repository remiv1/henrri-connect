PYTHON       = python

.PHONY: all clean build publish help test

# ———— Help ————

help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all     - Run all tests"
	@echo "  clean   - Remove generated files"
	@echo "  build   - Build the package"
	@echo "  publish - Publish the package to PyPI"
	@echo "  test    - Run unit tests"
	@echo "  help    - Show this help message"

# ———— Main Targets ————

all: test build build-verify publish clean

test:
	@echo "—–--–—–--–— Running Tests —–--–—–--–—"
	$(PYTHON) -m pytest tests

build:
	@echo "—–--–—–--–— Build —–--–—–--–—"
	$(PYTHON) -m build
	@echo "Package built successfully."
	@echo "You can find the distribution files in the 'dist' directory."
	@echo "You can verify the build using 'make build-verify'."

build-verify:
	@echo "—–--–—–--–— Build Verification —–--–—–--–—"
	$(PYTHON) -m twine check dist/*
	@echo "Build verification successful. All distribution files are valid."
	@echo "You can now publish the package to PyPI using 'make publish'."

publish:
	@echo "—–--–—–--–— Publish —–--–—–--–—"
	@echo "Confirm that you want to publish the package to PyPI. This action is irreversible."
	@read -p "Are you sure you want to publish? (y/n) " && [ $$REPLY = y ] || { echo "Publish canceled."; exit 1; }
	$(PYTHON) -m twine upload dist/*
	@echo "Package published successfully."
	@echo "You can verify the published package on PyPI."

clean:
	@echo "—–--–—–--–— Clean —–--–—–--–—"
	@echo "WARNING... this will remove all build artifacts and distribution files."
	@echo "Make sure you have backed up any important files before proceeding."
	rm -rf dist/ build/ src/*.egg-info
	@echo "Delete all cached files and directories."
	find . -type d \( -name '__pycache__' -o -name '.mypy_cache' -o -name '.pytest_cache' \) -exec rm -rf {} +
	@echo "Clean completed. All generated and cached files have been removed."