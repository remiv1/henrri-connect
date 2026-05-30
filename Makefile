PYTHON       = python

# Extraction automatique depuis pyproject.toml
VERSION      := $(shell grep '^version' pyproject.toml | head -1 | sed 's/version = "\(.*\)"/\1/')
RELEASE      := $(shell echo "$(VERSION)" | cut -d. -f1,2)

DOCS_SRC     = docs/source
DOCS_BUILD   = docs

.PHONY: all clean build publish help test docs docs-init docs-clean docs-serve

# ———— Help ————

help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all          - Tests, build, vérification, publication et nettoyage"
	@echo "  test         - Exécute les tests unitaires"
	@echo "  build        - Construit le paquet"
	@echo "  build-verify - Vérifie le paquet construit"
	@echo "  publish      - Publie le paquet sur PyPI"
	@echo "  clean        - Supprime les artefacts de build"
	@echo "  docs-init    - Initialise Sphinx (si non présent)"
	@echo "  docs         - Génère la documentation HTML"
	@echo "  docs-serve   - Génère et sert la documentation sur :8080"
	@echo "  docs-clean   - Supprime le répertoire de build de la documentation"
	@echo "  help         - Affiche ce message"
	@echo ""
	@echo "Version détectée : $(VERSION)  (release : $(RELEASE))"

# ———— Documentation ————

docs-init:
	@echo "—–--–—–--–— Documentation Initialization —–--–—–--–—"
	@if [ ! -f $(DOCS_SRC)/conf.py ]; then \
		sphinx-quickstart $(DOCS_SRC) \
			--no-sep \
			--project henrri-connect \
			--author "Rémi Verschuur" \
			-v $(VERSION) \
			--release $(RELEASE) \
			--language fr \
			--ext-autodoc \
			--quiet; \
		echo "  conf.py et index.rst générés dans $(DOCS_SRC)/"; \
	else \
		echo "  $(DOCS_SRC)/conf.py déjà présent — rien à faire."; \
	fi

docs:
	@echo "—–--–—–--–— Generating Documentation (v$(VERSION)) —–--–—–--–—"
	sphinx-build -b html $(DOCS_SRC) $(DOCS_BUILD)
	touch $(DOCS_BUILD)/.nojekyll
	@echo ""
	@echo "  Documentation générée dans $(DOCS_BUILD)/index.html"

docs-clean:
	@echo "—–--–—–--–— Clean Documentation —–--–—–--–—"
	find docs/ -maxdepth 1 ! -name 'source' ! -name '.' -exec rm -rf {} +
	@echo "  docs/ nettoyé (docs/source/ conservé)."

docs-serve: docs
	$(PYTHON) -m http.server 8080 --directory $(DOCS_BUILD)


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
