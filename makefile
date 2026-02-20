.PHONY: help install install-dev uninstall format complexity maintenability format-check lint test halstead clean setup-pypirc smoke-test metrics-all build

help:
	@echo "Installation:"
	@echo "  make install      - Installation production"
	@echo "  make test-smoke   - Lance un test simple en environnement production"
	@echo "  make install-dev  - Installation développement"
	@echo "  make uninstall    - Désinstalle package"

	@echo ""
	@echo "Commandes Développement: (nécessite l'installtion en mode développement)"
	@echo "  make test         - Lance tests"
	@echo "  make lint         - Vérifie qualité"
	@echo "  make format-check - Vérifie formatage code"
	@echo "  make format       - Formate code"
	@echo "  make ci           - Pipeline complet"
	@echo "  make metrics-all  - Test de maintenibilité/complexité"
	@echo ""
	@echo "Packaging & Publication:"
	@echo "  make build           - Construit le package (wheel + sdist)"
	@echo "  setup-pypirc          - Creation du .pypirc en vue de la publicaiton sur PyPi ou PyPi test"
	@echo "  make deploy-test     - Publie sur TestPyPI"
	@echo "  make deploy          - Publie sur PyPI"
	@echo ""
	@echo "Nettoyage:"
	@echo "  make clean           - Suppression fichiers temporaires"
	@echo "  make clean-build     - Suppression dossiers build/dist"

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


##################################################
# TEST, pytest, CI , smoke test
##################################################

test: 
	python -m pytest -v \
		--cov=src/calculator \
		--cov-branch \
		--cov-report=term-missing \
		--cov-report=xml \
		--cov-fail-under=95

ci: format-check lint test
	@echo "✅ Pipeline CI OK"



test-smoke: install  # Dépend de make install
	@echo "🧪 Smoke test installation prod..."
	python -c "
from $(PACKAGE_MODULE) import $(MAIN_FUNC)  # e.g. calculator, add
assert $(MAIN_FUNC)(1,1) == 2
	print('✅ Imports & fonctions OK')
	"
	@echo "🎉 Smoke test passé !"

##################################################
# BUILD & DEPLOY
##################################################

# Nettoyage des builds
clean-build:
	rm -rf build/ dist/ *.egg-info

# Construction du paquet (sdist + wheel)
build: clean-build
	@echo "📦 Construction du package..."
	python -m build
	@echo "✅ Package construit dans dist/"

setup-pypirc:
	@echo "🔑 Configuration .pypirc pour PyPI/TestPyPI"
	@printf "Choisissez (1=TestPyPI, 2=PyPI): "; read choix; \
	if [ "$$choix" = "1" ]; then \
	  server="testpypi"; \
	else \
	  server="pypi"; \
	fi; \
	printf "Token $$server (pypi-A... ): "; \
	stty -echo; read token; stty echo; printf "\n"; \
	printf "[distutils]\nindex-servers =\n    %s\n\n[%s]\nusername = __token__\npassword = %s\n" \
	    "$$server" "$$server" "$$token" > ~/.pypirc; \
	echo "✅ .pypirc créé pour $$server !"



# Upload sur TestPyPI
deploy-test: build
	@echo "🚀 Déploiement sur TestPyPI..."
	python -m twine upload --repository testpypi dist/*
	@echo "✅ Déployé sur TestPyPI"

# Upload sur PyPI (production)
deploy: build
	@echo "🚀 Déploiement sur PyPI..."
	python -m twine upload dist/*
	@echo "✅ Déployé sur PyPI"

# Installation depuis TestPyPI (utile pour tester)
install-test:
	@echo "📥 Installation depuis TestPyPI..."
	pip install --index-url https://test.pypi.org/simple/ \
		--extra-index-url https://pypi.org/simple \
		TestSimpleCalculator_2026_FJ

clean:
	rm -rf .pytest_cache .coverage coverage.xml htmlcov/ 

