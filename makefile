.PHONY: install install-dev format-check lint test clean

help:
	@echo "Installation:"
	@echo "  make install      - Installation production"
	@echo "  make install-dev  - Installation développement"
	@echo "  make uninstall    - Désinstalle package"
	@echo ""
	@echo "Commandes Développement: (nécessite l'installtion en mode développement)"
	@echo "  make test         - Lance tests"
	@echo "  make lint         - Vérifie qualité"
	@echo "  make format       - Vérifie formatage code"
	@echo "  make format       - Formate code"
	@echo "  make ci           - Pipeline complet"
	@echo "  make metrics-all  - Test de maintenibilité/complexité"
	@echo ""
	@echo "Nettoyage:"
	@echo "  make clean        - Suppression fichiers temporaires"

##################################################
# INSTALLATION / DESINSTALLATION
##################################################
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


##################################################
# REFORMATAGE
##################################################
format-check: 
	python -m black --check src/ tests/
format: 
	python -m black src/ tests/

##################################################
# Qualité du code
##################################################

lint: 
	python -m pylint -v src/ 


##################################################
# MÉTRIQUES RADON (LECTURE, MAINTENABILITE)
##################################################

complexity:
	@echo "📊 Complexité cyclomatique (McCabe):"
	@radon cc -s -a src/ tests/
	@echo ""

maintainability:
	@echo "🔧 Index de maintenabilité:"
	@radon mi -s src/ tests/
	@echo ""

metrics:
	@echo "📏 Métriques brutes (LOC):"
	@radon raw -s src/ tests/
	@echo ""

halstead:
	@echo "🧮 Métriques Halstead:"
	@radon hal src/ tests/
	@echo ""

metrics-all:
	@echo "════════════════════════════════════════════════════════════"
	@echo "📈 ANALYSE COMPLÈTE MÉTRIQUES CODE"
	@echo "════════════════════════════════════════════════════════════"
	@echo ""
	@$(MAKE) complexity
	@$(MAKE) maintainability
	@$(MAKE) metrics
	@$(MAKE) halstead
	@echo "════════════════════════════════════════════════════════════"
	@echo "✅ Analyse métriques terminée"
	@echo "════════════════════════════════════════════════════════════"




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

