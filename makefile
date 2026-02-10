.PHONY: install format-check lint test clean

install:
	pip install --upgrade pip
	pip install -e .[test]

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
	rm -rf .pytest_cache .coverage htmlcov/

