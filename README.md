# Passage

Module réduit de SchoolLogs : enregistrement des passages d'élèves aux points de
contrôle d'un établissement, fonctionnement hors ligne, détection d'anomalies,
messages aux parents et synthèse quotidienne.

> Projet en cours de réalisation (test technique). Ce README sera complété au fil
> du travail : choix techniques, comptes de test, sécurité, mode dégradé et limites.

## Stack

- **Backend** : FastAPI, SQLAlchemy 2, Alembic, PostgreSQL 16. Dépendances verrouillées avec [uv](https://docs.astral.sh/uv/) (`backend/uv.lock`).
- **Frontend** : React + TypeScript (Vite), tests Vitest. Dépendances verrouillées avec npm (`frontend/package-lock.json`).
- **CI** : GitHub Actions (`.github/workflows/tests.yml`) à chaque envoi.

## Démarrage local

```bash
cp .env.example .env          # puis renseigner POSTGRES_PASSWORD, DATABASE_URL, SECRET_KEY
docker compose up -d db       # PostgreSQL

cd backend
uv sync                       # installe les dépendances verrouillées
uv run uvicorn app.main:app --reload

cd ../frontend
npm ci
npm run dev
```

## Tests

```bash
cd backend && uv run pytest     # le test PostgreSQL s'exécute si DATABASE_URL est défini
cd frontend && npm test
```
