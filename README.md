# Calculator

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
