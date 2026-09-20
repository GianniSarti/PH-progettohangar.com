# ph-progettohangar.com

Monorepo del sito Progetto Hangar. Repository privato, in fase di scaffolding:
nessun contenuto reale.

## Struttura

| Cartella    | Contenuto                                                        |
|-------------|------------------------------------------------------------------|
| `frontend/` | Astro + isole React + Tailwind (build su Cloudflare Pages)       |
| `backend/`  | FastAPI (esecuzione su VPS)                                      |
| `docs/`     | Documentazione di progetto (segnaposto)                          |

`frontend/` e `backend/` sono indipendenti: non c'è un workspace npm condiviso.

## Requisiti

- Node 22 (vedi `frontend/.nvmrc`; Astro richiede Node ≥ 22.12.0)
- Python 3.12 (vedi `backend/.python-version`)

## Frontend

```bash
cd frontend
npm ci
npm run dev      # sviluppo
npm run build    # output statico in frontend/dist/
```

Lingue: italiano su `/` (default), spagnolo su `/es/`, inglese su `/en/`.
I testi stanno in `frontend/src/i18n/*.json`; le chiavi mancanti in `es` ed `en`
ricadono sull'italiano.

## Backend

```bash
cd backend
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # poi compilare i valori; .env non va mai committato
uvicorn app.main:app --reload
```

Verifica: `GET http://127.0.0.1:8000/health` risponde `{"status":"ok"}`.

## Sicurezza

Nessun segreto va committato. Le variabili d'ambiente reali stanno solo in `.env`
(ignorato da git) o nella configurazione dell'ambiente di deploy.
