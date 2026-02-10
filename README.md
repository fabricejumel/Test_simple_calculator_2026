# Calculator

[![GitLab CI](https://gitlab.com/user/calculator/badges/main/pipeline.svg)](https://gitlab.com/user/calculator/-/pipelines)
[![GitHub Actions](https://github.com/user/calculator/actions/workflows/ci.yml/badge.svg)](https://github.com/user/calculator/actions)
[![Coverage](https://codecov.io/gh/user/calculator/branch/main/graph/badge.svg)](https://codecov.io/gh/user/calculator)

> Calculatrice simple - CI/CD multi-plateforme (GitLab + GitHub)

## 🚀 CI/CD

Ce projet utilise **double CI/CD** :

- ✅ **GitLab CI** (`.gitlab-ci.yml`)
- ✅ **GitHub Actions** (`.github/workflows/ci.yml`)

Les 2 pipelines exécutent :
1. Format check (black)
2. Lint (pylint ≥9.0)
3. Tests (pytest coverage ≥95%)

## 📦 Dépôts

- GitLab: https://gitlab.com/user/calculator
- GitHub: https://github.com/user/calculator

## 🛠️ Installation

\`\`\`bash
# Clone (GitLab ou GitHub)
git clone https://gitlab.com/user/calculator.git
# ou
git clone https://github.com/user/calculator.git

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
