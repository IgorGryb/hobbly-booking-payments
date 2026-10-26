PYTHON ?= python3

.PHONY: setup test reproduce docs validate clean

setup:
	$(PYTHON) -c 'import sys; assert sys.version_info >= (3, 10); print(sys.version)'

test:
	PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -v

reproduce:
	PYTHONPATH=src $(PYTHON) scripts/reproduce.py

docs:
	$(PYTHON) scripts/validate_docs.py

validate: test reproduce docs

.PHONY: management-review
management-review: test
	PYTHONPATH=src $(PYTHON) scripts/review_decision_model.py

clean:
	$(PYTHON) -c 'from pathlib import Path; [(p.unlink()) for p in Path("artifacts").glob("*.json") if p.name != "README.json"]'
