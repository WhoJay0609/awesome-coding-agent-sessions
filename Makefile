PYTHON ?= python3

.PHONY: render check

render:
	$(PYTHON) scripts/render_readme.py

check:
	$(PYTHON) scripts/validate_catalog.py
	$(PYTHON) scripts/render_readme.py --check
	$(PYTHON) -m unittest discover -s tests -v
