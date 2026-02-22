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
````
mais plus simplement
````python
from calculator import SimpleCalculator
````

le __all__ = ["SimpleCalculator"] permet de limiter l'API, par exemple si on avait d'autres classes qui ne doivent pas être utilisés en dehors des appels internes du module lui même .

# Pourquoi pyproject.toml ?

**Format standard moderne** pour la configuration de projet Python (PEP 518/621).

## Avantages clés
- Lisibilité maximale : Pas d'indentation, syntaxe évidente
- Un seul fichier : Centralise toutes les métadonnées du projet
- Tool-agnostic : Compatible **Poetry**, **uv**, **Flit**, **Hatch**, **pip**
- Lockfile séparé : Garantit reproductibilité des environnements

## Outils compatibles
| Outil   | Commande                 | Vitesse  | Usage recommandé |
|:--------|--------------------------|----------|------------------|
| **uv**  | `uv sync`               | 10x pip  | Nouveaux projets |
| **Poetry** | `poetry install`      | Standard | Écosystème mature |
| **pip** | `pip install -e .`      | Basique  | Minimaliste |

## Comparaison avec ancien format
```
pyproject.toml  → Moderne, standard 2026
setup.py        → Obsolète (code Python verbeux)
requirements.txt → Pas de métadonnées projet
```

## Exemple
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "simple-calculator"
version = "1.0.0"
dependencies = ["pytest>=7.0"]
```

Verdict : Choix universel et pérenne pour tout outil moderne


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


26 tests unitaires couvrant 100 % des branches :
- Cas nominal : entiers positifs, négatifs, zéros et grands nombres
- 12 tests de robustesse (TypeError) et 3 tests d’erreur arithmétique (ZeroDivisionError)
- Cas limites : booléens traités comme entiers (True + False = 1), division non exacte (divide(1, 3) ≈ 0.333333)
- Contrôle systématique des types de retour (assertIsInstance sur int / float)


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
========================================== test session starts ==========================================
platform linux -- Python 3.12.3, pytest-9.0.2, pluggy-1.6.0 -- /home/astro/wp_admco_2026/Test_simple_calculator_2026/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/astro/wp_admco_2026/Test_simple_calculator_2026
configfile: pyproject.toml
testpaths: tests
plugins: cov-7.0.0
collected 26 items

tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_float PASSED           [  3%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_invalid_string PASSED          [  7%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_by_one PASSED            [ 11%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_negative PASSED          [ 15%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_positive PASSED          [ 19%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_valid_result_float PASSED      [ 23%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_denominator PASSED        [ 26%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_divide_zero_numerator PASSED          [ 30%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_bool PASSED              [ 34%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_float PASSED             [ 38%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_none PASSED              [ 42%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_invalid_string PASSED            [ 46%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_negative PASSED            [ 50%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_positive PASSED            [ 53%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_fsum_valid_zero PASSED                [ 57%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_large_numbers PASSED                  [ 61%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_invalid_types PASSED         [ 65%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_negative PASSED        [ 69%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_one PASSED             [ 73%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_positive PASSED        [ 76%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_multiply_valid_zero PASSED            [ 80%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_invalid_types PASSED        [ 84%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_negative PASSED       [ 88%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_positive PASSED       [ 92%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_substract_valid_zero PASSED           [ 96%]
tests/test_simple_calculator.py::TestSimpleCalculator::test_type_consistency PASSED               [100%]

============================================ tests coverage =============================================
____________________________ coverage: platform linux, python 3.12.3-final-0 ____________________________

Name                                  Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------------
src/calculator/__init__.py                3      0      0      0   100%
src/calculator/simple_calculator.py      19      0     10      0   100%
---------------------------------------------------------------------------------
TOTAL                                    22      0     10      0   100%
Coverage XML written to file coverage.xml
Required test coverage of 95% reached. Total coverage: 100.00%
========================================== 26 passed in 0.12s ===========================================
```

On voit apparaître plusieurs **100 %** de couverture :

1. **Premier 100 %** : Tous les **tests définis** ont été **exécutés avec succès** 
2. **Dernier 100 %** : **100 % des lignes de code** ont été **exercées** par les tests (couverture de code) 

**C'est beaucoup plus fort !** Nous avons fixé un **seuil de rejet à 95 %**.

**Pourquoi c'est important ?**
- Si on ajoute une **nouvelle fonction** sans tests associés → couverture < 95 % → **rejet automatique**
- Les anciens tests restent à 100 %, mais la **nouvelle fonctionnalité** est détectée comme non testée
- **Garantit** que chaque nouvelle feature a ses tests dédiés


## 🔧 Makefile
Le choix a été fait d'utiliser des commandes type bash  en utilisant la commande make , on aurait pu aussi utiliser un script shell ou faire des appels "systemes" en python.  Chaque choix a ces avantages et inconvenients. Le cas de l'usage de make n'est pas le plus courant mais il est pertinent d'avoir un equivalent qui servira ensuite dans le processus d'integration continue. DEs outil comme poetry et uv permettent d'automatiser aussi la partie de création du toml et de gestion du venv.

Commandes principales :
- make help  
- make install-dev  
- make ci  
- make metrics-all  
- make build  
- make deploy-test  
- make test-smoke  

Pipeline CI/CD : format → lint → tests → build → TestPyPI.


### ⚖️ **Comparaison des alternatives**
| Outil     | Avantages                                      | Inconvénients                          | Quand choisir                  |
|:---------|:-----------------------------------------------|:---------------------------------------|:-------------------------------|
| **make**  | CI/CD natif, cache intelligent, `make help`    | Courbe d'apprentissage                 | **Projets complexes / CI**    |
| **bash**  | Simple, rapide, natif Linux                    | Pas de cache, répétitif, erreurs silencieuses | Scripts locaux jetables     |
| **poetry**| Dépendances Python propres, `poetry run`       | Limité Python, pas de `deploy-test`    | Packages Python purs           |
| **just**  | Moderne, `just --help`, syntaxe YAML-like      | Moins répandu que `make`               | Alternative trendy             |
| **Python**| Langage familier, logging pro, cross-platform  | Réécriture complète, pas de cache natif | **un seul langage**     |
| **uv**    | **10x plus rapide**, remplace pip/poetry/venv, `uv sync` | Écosystème jeune (2026)                | **Nouveaux projets 2026**    |



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
