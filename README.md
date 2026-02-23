# TestSimpleCalculator_2026_FJ version GITHUB   

Projet de Mini‑calculatrice Python (+, −, ×, ÷) utilisée pour démonstration de packaging moderne PyPI, couverture de tests complète et CI/CD professionnelle.  
Auteur : Fabrice JUMEL (CPE Lyon) 
— License : Unlicense 

Requirements: 

— Python ≥ 3.10
— Make > 4.0


## Installation pour développement

```bash
git clone https://github.com/fabricejumel/Test_simple_calculator_2026.git
cd Test_simple_calculator_2026
python3 -m venv .venv 
source .venv/bin/activate
pip install -e .[test]
```
## Pour info,  finalité, déploiment sur PyPI (on se limitera à la version test de Pypi)

Usage direct pour l'installation
```bash
pip install -i https://test.pypi.org/simple/ TestSimpleCalculator_2026_FJ_GITHUB
```
## Pour info, autre installation possible directmeent à partir de github

```bash
pip install git+https://github.com/fabricejumel/Test_simple_calculator_2026.git@main#egg=TestSimpleCalculator_2026_FJ_GITHUB
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

## Comparaison avec les anciens formats
```
pyproject.toml  → Moderne, standard 2026
setup.py        → Obsolète (code Python verbeux)
requirements.txt → Pas de métadonnées projet
```

## pyproject.toml de notre package
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

### Structure et choix techniques :
**Configuration moderne** (PEP 518/621) compatible **setuptools + tous outils**.

| **Section** | **Rôle** | **Choix justifiés** |
|:------------|----------|---------------------|
| `[build-system]` | Backend build | `setuptools` = standard, mature |
| `[project]` | Métadonnées PyPI | Complet : version, auteur, license, Python min |
| `requires-python = ">=3.10"` | Compatibilité | Aligne CI (3.10/3.12) |
| `[project.optional-dependencies.test]` | Dev deps | `test=` groupe → `pip install -e '.[test]'` |
| `[tool.setuptools.packages.find]` | Scan auto | `src/` layout → moderne |
| `[tool.pytest.ini_options]` | Config pytest | `testpaths=tests`, `pythonpath=src` |



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

# Autres types de tests (non retenus)

Pyramide classique des tests logiciels :

| Type              | Objectif                              | Pourquoi NON nécessaire ici ?                    |
|-------------------|---------------------------------------|-------------------------------------------------|
| **Intégration**   | Vérifier interactions modules/services | 1 classe, 0 dépendance externe                 |
| **Système**   | Tester flux complet applicatif        | Calculatrice = 4 méthodes isolées               |
| **Performance**   | Charge, stress, endurance             | Opérations O(1), pas d'I/O réseau/BD           |
| **Sécurité**      | Vulnérabilités, injections            | Calculs mathématiques purs                      |
| **API/Contract**  | Contrats entre services               | Usage librairie interne uniquement                |




## 🔧 Makefile
Le choix a été fait d'utiliser des commandes type bash  en utilisant la commande make , on aurait pu aussi utiliser un script shell ou faire des appels "systemes" en python.  Chaque choix a ces avantages et inconvenients. Le cas de l'usage de make n'est pas le plus courant mais il est pertinent d'avoir un equivalent qui servira ensuite dans le processus d'integration continue. DEs outil comme poetry et uv permettent d'automatiser aussi la partie de création du toml et de gestion du venv.

[makefile](makefile)

Commandes principales :
- make help  
- make install-dev  
- make ci  
- make metrics-all  
- make build  
- make deploy-test  
- make test-smoke  



### ⚖️ **Comparaison des alternatives**
| Outil     | Avantages                                      | Inconvénients                          | Quand choisir                  |
|:---------|:-----------------------------------------------|:---------------------------------------|:-------------------------------|
| **make**  | CI/CD natif, cache intelligent, `make help`    | Courbe d'apprentissage                 | **Projets complexes / CI**    |
| **bash**  | Simple, rapide, natif Linux                    | Pas de cache, répétitif, erreurs silencieuses | Scripts locaux jetables     |
| **poetry**| Dépendances Python propres, `poetry run`       | Limité Python, pas de `deploy-test`    | Packages Python purs           |
| **just**  | Moderne, `just --help`, syntaxe YAML-like      | Moins répandu que `make`               | Alternative trendy             |
| **Python**| Langage familier, logging pro, cross-platform  | Réécriture complète, pas de cache natif | **un seul langage**     |
| **uv**    | **10x plus rapide**, remplace pip/poetry/venv, `uv sync` | Écosystème jeune (2026)                | **Nouveaux projets 2026**    |




## 📊 Métriques suppllémentaires à  titre  indicatives


## 1. Complexité cyclomatique (McCabe)
- Mesure : nombre de chemins possibles dans une fonction (if, for, while, etc.)
- Observation : toutes les fonctions/classes sont en A (≤4)
- Interprétation : code simple, facile à tester, faible risque de bugs
- Message pédagogique : "Un bon code n’est pas intelligent, il est simple."

## 2. Indice de maintenabilité (MI)
- Mesure : score global basé sur complexité, taille, Halstead et commentaires
- Observation : code principal 72 (bon), tests 50 (normal)
- Interprétation : code compréhensible et modifiable dans le temps
- Message pédagogique : "Le code doit rester maintenable même dans 6 mois."

## 3. LOC (lignes de code)
- Mesure : taille du code, proportion de code réel vs commentaires
- Observation : ~150 lignes de code réel, ~18% documentation
- Interprétation : code de taille adaptée, bonne lisibilité, tests majoritaires
- Message pédagogique : "La qualité n’est pas liée à la taille, mais un code court est plus maîtrisable."

## 4. Métriques Halstead
- Mesure : vocabulaire, volume, difficulté, effort mental, bugs estimés
- Observation : effort faible, bugs estimés < 0.1
- Interprétation : faible charge cognitive, code facile à comprendre
- Message pédagogique : "Halstead mesure la 'charge mentale' pour comprendre le code."

## 5. Choix global des métriques
- Axes couverts :
  - Structure logique → Complexité cyclomatique
  - Maintenabilité globale → MI
  - Taille et lisibilité → LOC
  - Charge cognitive → Halstead
- Conclusion : code simple, maintenable, lisible, peu complexe, avec tests nombreux

Le détail: 
````bash
make metrics-all
════════════════════════════════════════════════════════════
📈 ANALYSE COMPLÈTE MÉTRIQUES CODE
════════════════════════════════════════════════════════════

make[1]: Entering directory '/home/astro/wp_admco_2026/Test_simple_calculator_2026'
📊 Complexité cyclomatique (McCabe):
src/calculator/simple_calculator.py
    C 10:0 SimpleCalculator - A (4)
    M 63:4 SimpleCalculator.divide - A (4)
    M 13:4 SimpleCalculator.fsum - A (3)
    M 39:4 SimpleCalculator.substract - A (3)
    M 51:4 SimpleCalculator.multiply - A (3)
tests/test_simple_calculator.py
    C 10:0 TestSimpleCalculator - A (2)
    M 13:4 TestSimpleCalculator.setUp - A (1)
    M 18:4 TestSimpleCalculator.test_fsum_valid_positive - A (1)
    M 24:4 TestSimpleCalculator.test_fsum_valid_negative - A (1)
    M 30:4 TestSimpleCalculator.test_fsum_valid_zero - A (1)
    M 36:4 TestSimpleCalculator.test_fsum_invalid_float - A (1)
    M 45:4 TestSimpleCalculator.test_fsum_invalid_string - A (1)
    M 54:4 TestSimpleCalculator.test_fsum_invalid_none - A (1)
    M 61:4 TestSimpleCalculator.test_fsum_invalid_bool - A (1)
    M 70:4 TestSimpleCalculator.test_substract_valid_positive - A (1)
    M 76:4 TestSimpleCalculator.test_substract_valid_negative - A (1)
    M 82:4 TestSimpleCalculator.test_substract_valid_zero - A (1)
    M 88:4 TestSimpleCalculator.test_substract_invalid_types - A (1)
    M 96:4 TestSimpleCalculator.test_multiply_valid_positive - A (1)
    M 102:4 TestSimpleCalculator.test_multiply_valid_negative - A (1)
    M 108:4 TestSimpleCalculator.test_multiply_valid_zero - A (1)
    M 114:4 TestSimpleCalculator.test_multiply_valid_one - A (1)
    M 120:4 TestSimpleCalculator.test_multiply_invalid_types - A (1)
    M 128:4 TestSimpleCalculator.test_divide_valid_positive - A (1)
    M 134:4 TestSimpleCalculator.test_divide_valid_result_float - A (1)
    M 140:4 TestSimpleCalculator.test_divide_valid_negative - A (1)
    M 146:4 TestSimpleCalculator.test_divide_valid_by_one - A (1)
    M 151:4 TestSimpleCalculator.test_divide_zero_denominator - A (1)
    M 160:4 TestSimpleCalculator.test_divide_zero_numerator - A (1)
    M 165:4 TestSimpleCalculator.test_divide_invalid_float - A (1)
    M 172:4 TestSimpleCalculator.test_divide_invalid_string - A (1)
    M 180:4 TestSimpleCalculator.test_large_numbers - A (1)
    M 186:4 TestSimpleCalculator.test_type_consistency - A (1)

33 blocks (classes, functions, methods) analyzed.
Average complexity: A (1.393939393939394)

make[1]: Leaving directory '/home/astro/wp_admco_2026/Test_simple_calculator_2026'
make[1]: Entering directory '/home/astro/wp_admco_2026/Test_simple_calculator_2026'
🔧 Index de maintenabilité:
src/calculator/__init__.py - A (100.00)
src/calculator/simple_calculator.py - A (72.60)
tests/test_simple_calculator.py - A (50.06)

make[1]: Leaving directory '/home/astro/wp_admco_2026/Test_simple_calculator_2026'
make[1]: Entering directory '/home/astro/wp_admco_2026/Test_simple_calculator_2026'
📏 Métriques brutes (LOC):
src/calculator/__init__.py
    LOC: 11
    LLOC: 4
    SLOC: 3
    Comments: 0
    Single comments: 0
    Multi: 4
    Blank: 4
    - Comment Stats
        (C % L): 0%
        (C % S): 0%
        (C + M % L): 36%
src/calculator/simple_calculator.py
    LOC: 76
    LLOC: 25
    SLOC: 27
    Comments: 2
    Single comments: 3
    Multi: 32
    Blank: 14
    - Comment Stats
        (C % L): 3%
        (C % S): 7%
        (C + M % L): 45%
tests/test_simple_calculator.py
    LOC: 198
    LLOC: 152
    SLOC: 123
    Comments: 11
    Single comments: 38
    Multi: 3
    Blank: 34
    - Comment Stats
        (C % L): 6%
        (C % S): 9%
        (C + M % L): 7%
** Total **
    LOC: 285
    LLOC: 181
    SLOC: 153
    Comments: 13
    Single comments: 41
    Multi: 39
    Blank: 52
    - Comment Stats
        (C % L): 5%
        (C % S): 8%
        (C + M % L): 18%

make[1]: Leaving directory '/home/astro/wp_admco_2026/Test_simple_calculator_2026'
make[1]: Entering directory '/home/astro/wp_admco_2026/Test_simple_calculator_2026'
🧮 Métriques Halstead:
src/calculator/__init__.py:
    h1: 0
    h2: 0
    N1: 0
    N2: 0
    vocabulary: 0
    length: 0
    calculated_length: 0
    volume: 0
    difficulty: 0
    effort: 0
    time: 0.0
    bugs: 0.0
src/calculator/simple_calculator.py:
    h1: 7
    h2: 25
    N1: 17
    N2: 26
    vocabulary: 32
    length: 43
    calculated_length: 135.74788919877133
    volume: 215.0
    difficulty: 3.64
    effort: 782.6
    time: 43.47777777777778
    bugs: 0.07166666666666667
tests/test_simple_calculator.py:
    h1: 3
    h2: 23
    N1: 30
    N2: 32
    vocabulary: 26
    length: 62
    calculated_length: 108.79681249147477
    volume: 291.42726252474773
    difficulty: 2.0869565217391304
    effort: 608.196026138604
    time: 33.78866811881133
    bugs: 0.09714242084158257

make[1]: Leaving directory '/home/astro/wp_admco_2026/Test_simple_calculator_2026'
════════════════════════════════════════════════════════════
✅ Analyse métriques terminée
════════════════════════════════════════════════════════════
````
## Intégration Continue (CI)

L'intégration continue (CI) est une pratique qui consiste à automatiser le processus de construction, de tests et de validation du code à chaque modification.  

### Objectifs principaux
- Détecter rapidement les erreurs : chaque commit déclenche automatiquement les tests, ce qui évite que du code cassé soit intégré dans la branche principale.
- Assurer la qualité : l'analyse statique (linting, métriques, couverture de tests, etc.) est effectuée automatiquement.
- Standardiser le processus : tous les développeurs utilisent le même pipeline de vérification.
- Documenter et versionner les résultats : rapports de tests et métriques générés et archivés.

### Pipeline manuel avec Make
Avant de configurer le CI automatique, il est possible de **simuler l’enchaînement des tâches à la main** :

```bash
make lint
make test
make build
make deploy-test 
```
on peut tester aussi les métriques additionnelles :
```bash
make metrics-all
```
si on veut conditionner le lancement d'une étape par la réussite de précédente :

```bash
make lint && make test && make build && make deploy-test
```

> Chaque étape génère un rapport détaillé qui peut être consulté pour valider le code.

### Pipeline CI GitHub
Le CI GitHub automatise ces mêmes étapes à chaque commit ou pull request :

1. **Détection de modification** : push sur la branche principale (hors juste modification du README.md) ou ouverture d'une Pull Request.
2. **Exécution des jobs** définis dans [.github/workflows/main.yml](.github/workflows/main.yml) :
   - Installation des dépendances 
   - Vérification du style et linting (test en //  en python 3.10 et 3.12)
   - Exécution des tests unitaires (`make test`) (test en //  en python 3.10 et 3.12)
   - Analyse des métriques (`make metrics-all`)

3. **Résultats** : chaque job indique `success` ou `failure` dans GitHub, avec liens vers les logs détaillés.
5. **Artefacts** : on peut recuperer sur github  les builds du projets générés pendant la phase de ci/cd
   
> Le CI garantit que le code intégré respecte les standards définis et reste fonctionnel automatiquement, sans intervention manuelle.

# Améliorations possibles
   - gestion automatique des versions des fichiers et du package
   - utilisation de poetry et ou uv
   - generation d'un rapport de test comme artefact
   - utilisation des logs (logging) dans le code

# TODO 
- [] explication sur les token pypi et usage dans Github aciton
- [] rajouter les logs
- [] rajouter peut etre explications pep8 pep20 dans pylint
- [] rajouter 100% de test dans le log avant la couverture par cov


Projet pédagogique CPE Lyon — Packaging, tests, CI/CD, métriques.  
Fabrice JUMEL — Février 2026
