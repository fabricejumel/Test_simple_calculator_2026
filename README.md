# Calculator - Framework Test Complet

> Projet pédagogique Administation des Codes  2026 - Découverte écosystème test Python vers CI/CD

## 🎯 Objectifs Pédagogiques

Ce projet démontre un **framework de test complet** utilisable en industrie :

- ✅ **Tests unitaires** (pytest)
- ✅ **Couverture code** (100% branches)
- ✅ **Qualité code** (pylint, black)
- ✅ **Performance** (benchmarks, profiling)
- ✅ **CI/CD** (GitLab pipelines)
- ✅ **Automation** (Makefile)

## 📚 Installation

\`\`\`bash
# Clone projet
git clone https://gitlab.com/admco/calculator.git
cd calculator

# Setup environnement
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Installe dépendances
make install
\`\`\`

## 🚀 Commandes Rapides

\`\`\`bash
# Aide
make help

# Tests basiques
make test

# Pipeline complet
make all
\`\`\`

## 📖 Parcours Apprentissage

### Niveau 1 : Tests Basiques

\`\`\`bash
make test       # Lance tests
make cov-html   # Voir couverture
\`\`\`

**Concepts** : Tests unitaires, assertions, coverage

---

### Niveau 2 : Qualité Code

\`\`\`bash
make format     # Formate code
make lint       # Vérifie qualité
make all        # Pipeline complet
\`\`\`

**Concepts** : PEP8, linting, formatage automatique

---

### Niveau 3 : Performance (Optionnel)

\`\`\`bash
make perf       # Durée tests
make bench      # Benchmarks
make profile    # Profiling CPU
\`\`\`

**Concepts** : Optimisation, profiling, comparaison algo

---

## 🛠️ Outils Inclus

| Outil | Usage | Obligatoire ? |
|-------|-------|---------------|
| **pytest** | Tests unitaires | ✅ Oui |
| **pytest-cov** | Couverture code | ✅ Oui |
| **pylint** | Analyse qualité | ✅ Oui |
| **black** | Formatage auto | ✅ Oui |
| **pytest-benchmark** | Benchmarks | ⚠️ Optionnel |
| **pytest-profiling** | Profiling CPU | ⚠️ Optionnel |
| **pytest-memray** | Profiling mémoire | ⚠️ Optionnel |

## 📊 Standards Qualité

- ✅ Coverage ≥ 95% (branches)
- ✅ Pylint score ≥ 9.0
- ✅ Formatage black (line 100)
- ✅ Python ≥ 3.10

## 🎓 Ressources

- [Documentation pytest](https://docs.pytest.org/)
- [Guide coverage](https://coverage.readthedocs.io/)
- [PEP8 Style Guide](https://pep8.org/)

## 👥 Contribution

Ce framework est un **exemple pédagogique**. Les élèves peuvent :
- Utiliser seulement les outils de base (pytest, pylint)
- Expérimenter avec outils avancés (benchmark, profiling)
- Personnaliser selon besoins projet
\`\`\`

---

## Usage Pédagogique

### TP Niveau 1 (Débutant)

**Consigne** :
> Utilisez seulement `make test` et `make cov-html`

**Élève découvre** :
- Tests passent/échouent
- Coverage montre lignes testées
- Vert/rouge HTML

---

### TP Niveau 2 (Intermédiaire)

**Consigne** :
> Pipeline complet : `make all`

**Élève découvre** :
- Black formate automatiquement
- Pylint signale problèmes qualité
- Pipeline = enchaînement outils

---

### TP Niveau 3 (Avancé)

**Consigne** :
> Comparez 2 algorithmes avec `make bench`

**Élève découvre** :
- Mesure performance
- Compare versions
- Justifie choix algo

---

## Résumé

**Framework complet = OUI pour pédagogie** ✅

**Avantages** :
- ✅ Découverte écosystème complet
- ✅ Expérimentation guidée
- ✅ Standards industrie
- ✅ Portfolio professionnel
- ✅ Scalabilité apprentissage

**Structure** :
