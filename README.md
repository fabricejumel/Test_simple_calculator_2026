# TestSimpleCalculator_2026_FJ version GITHUB  

Projet de Mini‑calculatrice Python (+, −, ×, ÷) utilisée pour démonstration de packaging moderne PyPI, couverture de tests complète et CI/CD professionnelle.  
Auteur : Fabrice JUMEL (CPE Lyon) 
— License : Unlicense 

Requirements: 

— Python ≥ 3.10
— Make > 4.0

## 🚀 Installation pour développement

```bash
git clone https://github.com/fabricejumel/Test_simple_calculator_2026.git
cd Test_simple_calculator_2026
python3 -m venv .venv 
source .venv/bin/activate
pip install -e .[test]
```

### Test rapide en python

````python
from calculator import SimpleCalculator
calc = SimpleCalculator()
print(calc.fsum(2, 3))        # 5
print(calc.divide(10, 2))     # 5.0
````
ou en bash
````bash
python -c "\
from calculator import SimpleCalculator; \
c = SimpleCalculator(); \
assert c.fsum(1, 1) == 2, 'Add échoue'; \
print('✅ Imports & fonctions OK')"
````


## 📁 Structure du projet
```bash
TestSimpleCalculator_2026_FJ_GITHUB/
├──.github/
│   └──workflows
│      └──main.yml
├── makefile
├── README.md
├── pyproject.toml
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── simple_calculator.py
└── tests/
    └── test_simple_calculator.py
```
L'element centrale est la classe SimpleCalculator, on notera l'usage des docstrings pour les commentaires. L'utilisation de la gestion des erreurs et la verification des types. 

```python
import calculator
#exemple pour le module
help(calculator)
#exemple pour la classe
help (calculator.SimpleCalculator)
#exemple pour une fonction
help (calculator.SimpleCalculator.divide)
```

````text
+------------------------------+
|    SimpleCalculator          |
+------------------------------+
| + fsum(a:int,b:int):int      |
| + substract(a:int,b:int):int |
| + multiply(a:int,b:int):int  |
| + divide(a:int,b:int):float  |
+------------------------------+
````

```python
class SimpleCalculator:
    """Calculatrice simple (+, -, *, /) avec validation entrées."""

    def fsum(self, int_a: int, int_b: int) -> int:
        """Additionne deux entiers.
        
        Args:
            int_a: Premier entier.
            int_b: Deuxième entier.
        
        Returns:
            Somme des deux entiers.
        
        Raises:
            TypeError: Si paramètres non entiers.
        
        Examples:
            >>> calc = SimpleCalculator()
            >>> calc.fsum(2, 3)
            5
            >>> calc.fsum(2.5, 3)
            Traceback: TypeError: Parameters must be integers
        """
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise TypeError(
                f"Parameters must be integers, got {type(int_a).__name__}, {type(int_b).__name__}"
            )
        return int_a + int_b

    def substract(self, int_a: int, int_b: int) -> int:
        """Soustrait int_b de int_a.
        
        Raises:
            TypeError: Si paramètres non entiers.
        """
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise TypeError(
                f"Parameters must be integers, got {type(int_a).__name__}, {type(int_b).__name__}"
            )
        return int_a - int_b

    def multiply(self, int_a: int, int_b: int) -> int:
        """Multiplie deux entiers.
        
        Raises:
            TypeError: Si paramètres non entiers.
        """
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise TypeError(
                f"Parameters must be integers, got {type(int_a).__name__}, {type(int_b).__name__}"
            )
        return int_a * int_b

    def divide(self, int_a: int, int_b: int) -> float:
        """Divise int_a par int_b.
        
        Raises:
            TypeError: Si paramètres non entiers.
            ZeroDivisionError: Si int_b == 0.
        """
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise TypeError(
                f"Parameters must be integers, got {type(int_a).__name__}, {type(int_b).__name__}"
            )
        if int_b == 0:
            raise ZeroDivisionError("Division par zéro impossible")
        return int_a / int_b
```

Pour transformer ce code en un package distribuable en  python (pip ) en utilisant les standards actuelles. On a crée la strcuture suivante :

```bash
├── pyproject.toml
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── simple_calculator.py
```
avec 

````python
"""calculator__init__.py


Author: Fabrice Jumel
License: Unlicense
"""

from .simple_calculator import SimpleCalculator

__version__ = "0.0.11"
__all__ = ["SimpleCalculator"]

````
Cela permet de ne pas écrire ensuite 
````python
from calculator.simple_calculator import SimpleCalculator
````python
mais plus simplement
````python
from calculator import SimpleCalculator
````

le __all__ = ["SimpleCalculator"] permet de limiter l'API, par exemple si on avait d'autres classes qui ne doivent pas être utilisés en dehors des appels internes du module lui même .

````python
"""pyproject.toml"""

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "TestSimpleCalculator_2026_FJ_GITHUB"
version = "0.0.11"
authors = [{name = "Fabrice Jumel"}]
description = "Simple calculator for packaging demo"
readme= "README.md"
license = {text = "Unlicense"}
requires-python = ">=3.10"

[project.optional-dependencies]
test = ["pytest>=7.0", "pytest-cov", "pylint", "black", "radon","build","twine"]

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
````




## 🧪 Tests unitaires (100% coverage)

[Test](tests/test_simple_calculator.py)


26 tests unittest couvrant 100% des branches :
- Cas valides : positifs, négatifs, zéros, grands nombres  
- 12× TypeError, 3× ZeroDivisionError  
- Edge cases : True + False = 1, divide(1,3)=0.333  
- Vérification des types (assertIsInstance)

Commande :

```bash
pytest
```
ou 
```bash
python -m pytest
```
ou des variantes , nous avons dans notre cas fait ce choix :

```bash
python -m pytest -v \
                --cov=src/calculator \
                --cov-branch \
                --cov-report=term-missing \
                --cov-report=xml \
                --cov-fail-under=95
```
que l'on peut lancer avec une commande make

```bash
make test
```

## 🔧 Makefile
Le choix a été fait d'utiliser des commandes type bash  en utilisant la commande make , on aurait pu aussi utiliser un script shell ou faire des appels "systemes" en python.  Chaque choix a ces avantages et inconvenients. Le cas de l'usage de make n'est pas le plus courant mais il est pertinent d'avoir un equiavlent qui servira ensuite dans le processus d'integration continue

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

## 📦 PyPI (test)
Usage direct pour l'installation

pip install -i https://test.pypi.org/simple/ TestSimpleCalculator_2026_FJ_GITHUB


Projet pédagogique CPE Lyon — Packaging, tests, CI/CD, métriques.  
Fabrice JUMEL — Février 2026
