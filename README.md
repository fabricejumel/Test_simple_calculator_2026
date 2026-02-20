# TestSimpleCalculator_2026_FJ version GITHUB  

Projet de Mini‑calculatrice Python (+, −, ×, ÷) utilisée pour démonstration de packaging moderne PyPI, couverture de tests complète et CI/CD professionnelle.  
Auteur : Fabrice JUMEL (CPE Lyon) — License : Unlicense — Python ≥ 3.10

## 🚀 Installation pour développement

```bash
git clone https://github.com/fabricejumel/Test_simple_calculator_2026.git
cd Test_simple_calculator_2026
python3 -m venv .venv 
source .venv/bin/activate
pip install -e .[test]
```

### Test rapide
from calculator import SimpleCalculator
calc = SimpleCalculator()
print(calc.fsum(2, 3))        # 5
print(calc.divide(10, 2))     # 5.0

## 📁 Structure du projet

TestSimpleCalculator_2026_FJ_GITHUB/
├── pyproject.toml
├── Makefile
├── README.md
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── simple_calculator.py
└── tests/
    └── test_simple_calculator.py

## 🧮 Fonctionnalités

Classe SimpleCalculator (~60 LOC) :
- fsum(a, b) → addition  
- substract(a, b) → soustraction  
- multiply(a, b) → multiplication  
- divide(a, b) → division (ZeroDivisionError si /0)

Caractéristiques :
- Type hints stricts (int obligatoire)
- Exceptions : TypeError, ZeroDivisionError
- Docstrings avec doctests
- divide() renvoie un float

## 🧪 Tests unitaires (100% coverage)

26 tests unittest couvrant 100% des branches :
- Cas valides : positifs, négatifs, zéros, grands nombres  
- 12× TypeError, 3× ZeroDivisionError  
- Edge cases : True + False = 1, divide(1,3)=0.333  
- Vérification des types (assertIsInstance)

Commande :
make test

## 🔧 Makefile (20+ commandes utiles)

Commandes principales :
- make help  
- make install-dev  
- make ci  
- make metrics-all  
- make build  
- make deploy-test  
- make test-smoke  

Pipeline CI/CD : format → lint → tests → build → TestPyPI.

## 📊 Métriques

Couverture branches : 100%  
Cyclomatique : ≤ 8  
Maintenabilité MI : 100/100  
Halstead Volume : ~150  
LOC production : 60  
Tests : 26 méthodes  

## 🔄 Usage avancé

Doctests :
python -m doctest src/calculator/simple_calculator.py

Benchmark :
pytest --benchmark-only

Installation TestPyPI :
make install-test

## 🤝 Contribution

1. Fork  
2. make install-dev  
3. make ci  
4. Pull Request  

## 📦 PyPI

TestPyPI :
pip install -i https://test.pypi.org/simple/ TestSimpleCalculator_2026_FJ_GITHUB

Production :
make deploy-prod

Projet pédagogique CPE Lyon — Packaging, tests, CI/CD, métriques.  
Fabrice JUMEL — Février 2026
