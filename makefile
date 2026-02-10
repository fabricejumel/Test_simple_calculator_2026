.PHONY: install install-dev format-check lint test clean


install:
	@echo "📦 Installation production..."
	pip install --upgrade pip
	pip install .
	@echo "✅ Package installé"

# Développement (éditable, avec outils test)
install-dev:
	@echo "📦 Installation développement..."
	pip install --upgrade pip
	pip install -e .[test]
	@echo "✅ Package éditable + outils dev installés"


format-check: 
	python -m black --check src/ tests/

lint: 
	python -m pylint -v src/ tests/

test: 
	python -m pytest -v \
		--cov=src/calculator \
		--cov-branch \
		--cov-report=term-missing \
		--cov-report=xml \
		--cov-fail-under=95

ci: format-check lint test
	@echo "✅ Pipeline CI OK"

clean:
	rm -rf .pytest_cache .coverage coverage.xml htmlcov/ 

