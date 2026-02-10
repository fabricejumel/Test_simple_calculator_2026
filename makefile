.PHONY: install install-dev format-check lint test clean

help:
	@echo "Installation:"
	@echo "  make install      - Installation production"
	@echo "  make install-dev  - Installation développement"
	@echo "  make uninstall    - Désinstalle package"
	@echo ""
	@echo "Commandes Développement:" (nécessite l'installtion en mode développement)
	@echo "  make test         - Lance tests"
	@echo "  make lint         - Vérifie qualité"
	@echo "  make format       - Formate code"
	@echo "  make ci           - Pipeline complet"
	@echo ""
	@echo "Nettoyage:"
	@echo "  make clean        - Suppression fichiers temporaires"

install:
	@echo "📦 Installation production..."
	pip install --upgrade pip
	pip install .
	@echo "✅ Package installé"

uninstall:
	@echo "🗑️  Désinstallation package..."
	pip uninstall -y TestSimpleCalculator_2026_FJ
	@echo "✅ Package désinstallé"

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

