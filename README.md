# Calculator

> Calculatrice simple - CI/CD multi-plateforme (GitLab + GitHub)

## 🚀 CI/CD

### ☁️ CI/CD Automatique

**GitHub Actions** & **GitLab CI** → Tests auto + deploy TestPyPI (`main`) / PyPI (`tag`).

#### Configuration Tokens PyPI (Obligatoire)

**1. Générez tokens** :
- [PyPI](https://pypi.org/manage/account/token/) → `PYPI_TOKEN`
- [TestPyPI](https://test.pypi.org/manage/account/token/) → `TESTPYPI_TOKEN`
- **Scope** : Project `TestSimpleCalculator_2026_FJ` > Entire index

**2. GitHub Secrets** (Repo > Settings > Secrets and variables > Actions Secrets → New repository secret) : 
TEST_PYPI_TOKEN # TestPyPI token
PYPI_TOKEN # PyPI token (prod)
Pour github , on pourrait proceder a l'associer des comptes pypi et github pour rendre tout cela transparent 

**3. GitLab Variables** (Project > Settings > CI/CD > Variables) :
TESTPYPI_TOKEN # TestPyPI (Protected/Masked)
PYPI_TOKEN # PyPI (Protected/Masked)

Ce projet utilise **double CI/CD** :

- ✅ **GitLab CI** (`.gitlab-ci.yml`)
- ✅ **GitHub Actions** (`.github/workflows/ci.yml`)

Les 2 pipelines exécutent :
1. Format check (black)
2. Lint (pylint ≥9.0)
3. Tests (pytest coverage ≥95%)



## 🛠️ Installation

\`\`\`bash
# Clone (GitLab ou GitHub)
git clone https://gitlab.com//fabricejumel/Test_simple_calculator_2026.git // TODO
# ou
git clone https://github.com/fabricejumel/Test_simple_calculator_2026.git

cd calculator
make install
\`\`\`

## 🧪 Tests

\`\`\`bash
make test    # Tests
make lint    # Qualité
make all     # Pipeline complet
\`\`\`
\`\`\`

---

## Différences Subtiles

### Cache

**GitLab** :
```yaml
cache:
  paths:
    - .venv/
