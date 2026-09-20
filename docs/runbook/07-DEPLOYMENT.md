# Progetto Hangar — Deployment
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive il processo di rilascio (deployment) di **Progetto Hangar**, sia per il frontend sia per il backend.

Serve a:

- documentare come il codice passa dallo sviluppo alla produzione
- chiarire i flussi di deploy di frontend e backend
- rendere i rilasci ripetibili e verificabili
- ridurre il rischio di errori durante gli aggiornamenti
- permettere a un operatore o a una IA di rilasciare in sicurezza

Questo file non contiene segreti.  
Le credenziali e i token di deploy sono gestiti secondo `14-SECRETS-INVENTORY`.

---

## 2. Modello di deployment

Il progetto adotta un modello a due binari distinti.

- **Frontend**: deploy gestito tramite Cloudflare Pages, collegato al repository GitHub
- **Backend**: deploy sulla VPS controllata direttamente, con aggiornamento del codice e riavvio del servizio

Principio:

- frontend e backend hanno cicli di rilascio indipendenti
- un rilascio del frontend non richiede necessariamente un rilascio del backend, e viceversa

---

## 3. Repository e organizzazione

Repository:

- monorepo su GitHub

Contenuto logico:

- codice frontend
- codice backend
- documentazione / Runbook
- eventuali script operativi

Principi:

- il repository è la fonte primaria del codice
- i segreti non sono versionati
- i file di ambiente sono esclusi tramite `.gitignore`

Verifica esclusione file sensibili:

```bash
git check-ignore -v backend/.env
```

---

## 4. Strategia dei branch

Modello iniziale consigliato:

- branch principale stabile: `main`
- eventuali branch di lavoro per funzionalità: `feature/...`
- eventuale branch di integrazione se necessario in futuro

Principi:

- `main` deve restare sempre in stato rilasciabile
- le modifiche rilevanti passano da branch dedicati e poi vengono integrate
- evitare commit diretti rischiosi su `main` per modifiche complesse

Nota:

- non esistendo ancora staging, prestare attenzione ai rilasci diretti in produzione

---

## 5. Deploy del frontend

### 5.1 Flusso
1. modifica del codice frontend
2. commit e push sul branch collegato a Cloudflare Pages
3. build automatica su Cloudflare Pages
4. pubblicazione sul dominio

### 5.2 Configurazione build
Parametri tipici da documentare in Cloudflare Pages:

```text
Framework preset: Astro
Build command: npm run build
Build output directory: dist
Root directory: frontend
```

Nota:

- i valori esatti (soprattutto la directory di output e la root) vanno verificati e allineati alla configurazione reale del progetto

### 5.3 Variabili di ambiente frontend
Variabili non sensibili impostate nel pannello Cloudflare Pages:

```text
PUBLIC_API_BASE_URL=https://api.progettohangar.com
PUBLIC_STRIPE_PUBLISHABLE_KEY=<CHIAVE_PUBBLICA>
```

Regole:

- solo variabili non sensibili lato client
- tracciare comunque le chiavi pubbliche in `14-SECRETS-INVENTORY`

### 5.4 Verifica post-deploy frontend
- verificare che il sito sia raggiungibile
- verificare il caricamento delle pagine principali
- verificare la comunicazione con l'API
- verificare il flusso di avvio checkout

---

## 6. Deploy del backend

### 6.1 Flusso
1. modifica del codice backend
2. commit e push sul repository
3. accesso alla VPS via SSH
4. aggiornamento del codice sul server
5. aggiornamento delle dipendenze se necessario
6. riavvio del servizio backend
7. verifica post-deploy

### 6.2 Aggiornamento del codice sul server
Accesso al server:

```bash
ssh -p 134 pilota@<IP_O_HOST_VPS>
```

Aggiornamento del codice:

```bash
cd /percorso/backend
git pull origin main
```

### 6.3 Aggiornamento dipendenze
Solo se cambiano le dipendenze:

```bash
source /percorso/venv/bin/activate
pip install -r requirements.txt
```

### 6.4 Riavvio del servizio
```bash
sudo systemctl restart <nome-servizio>
sudo systemctl status <nome-servizio>
```

### 6.5 Verifica post-deploy backend
```bash
# health locale
curl -I http://127.0.0.1:8000/health

# health pubblica
curl -I https://api.progettohangar.com/health
```

Esito atteso:

- servizio attivo
- health locale e pubblica positive
- nessun errore nei log recenti

Controllo log recenti:

```bash
sudo journalctl -u <nome-servizio> -e
```

---

## 7. Ordine dei rilasci in caso di modifiche coordinate

Quando una modifica coinvolge sia frontend sia backend:

1. rilasciare prima il backend (nuovi endpoint o contratti API)
2. verificare che il backend sia stabile e retrocompatibile
3. rilasciare poi il frontend che usa le nuove funzionalità
4. verificare l'integrazione end-to-end

Principio:

- evitare che il frontend chiami funzionalità non ancora disponibili sul backend
- privilegiare modifiche backend retrocompatibili quando possibile

---

## 8. Rollback

### 8.1 Rollback frontend
- Cloudflare Pages conserva le versioni dei deploy
- in caso di problema, ripristinare un deploy precedente dal pannello

### 8.2 Rollback backend
- tornare a un commit stabile precedente
- riavviare il servizio

Esempio di rollback backend:

```bash
cd /percorso/backend
git log --oneline
git checkout <commit-stabile>
sudo systemctl restart <nome-servizio>
```

Nota:

- valutare l'impatto su eventuali migrazioni dati
- documentare ogni rollback nel changelog

---

## 9. Checklist di rilascio

Checklist sintetica da seguire ad ogni rilascio.

Pre-rilascio:

- [ ] codice testato in locale
- [ ] nessun segreto incluso nel commit
- [ ] dipendenze aggiornate e coerenti
- [ ] modifiche documentate

Rilascio:

- [ ] backend aggiornato (se necessario)
- [ ] servizio backend riavviato e verificato
- [ ] frontend pubblicato (se necessario)

Post-rilascio:

- [ ] health check positivi
- [ ] flusso di acquisto verificato
- [ ] log privi di errori critici
- [ ] changelog aggiornato

---

## 10. Superfici critiche del deployment

Punti di attenzione:

- rilascio diretto in produzione senza staging
- disallineamento tra contratto API backend e frontend
- inclusione accidentale di segreti nei commit
- mancato riavvio del servizio dopo aggiornamento
- assenza di verifica post-deploy

Mitigazioni:

- checklist di rilascio
- attenzione alla retrocompatibilità
- verifica post-deploy sistematica
- controllo dei file ignorati da Git

---

## 11. Automazione futura (opzionale)

Possibili evoluzioni:

- pipeline CI/CD per test automatici
- deploy automatizzato del backend su push
- introduzione di un ambiente di staging
- controlli automatici di qualità e sicurezza

Stato:

- non implementate
- da valutare quando il progetto cresce

Principio:

- introdurre automazione solo quando aggiunge affidabilità reale

---

## 12. Assunzioni correnti

Assunzioni valide alla stesura:

- monorepo su GitHub come fonte primaria
- frontend su Cloudflare Pages con deploy da repository
- backend aggiornato manualmente via SSH sulla VPS
- non esiste ancora staging
- esiste un solo ambiente di produzione

Se queste assunzioni cambiano, aggiornare il documento.

---

## 13. Attività aperte

Attività da completare:

- confermare la configurazione reale di build su Cloudflare Pages
- documentare percorsi reali del backend sul server
- confermare nome del servizio di sistema
- valutare introduzione di staging e CI/CD
- consolidare la strategia dei branch

---

## 14. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione dei flussi di rilascio
- incompleto nei valori puntuali (percorsi, nomi servizio, config build)
- da aggiornare quando i flussi sono consolidati

Dipendenze correlate:

- `04-VPS-E-HARDENING`
- `05-FRONTEND`
- `06-BACKEND`
- `08-NGINX-E-HTTPS`

---

## 15. Changelog

### v0.1
- documentato il modello di deployment a due binari
- descritti i flussi di rilascio di frontend e backend
- definite checklist, rollback e verifiche post-deploy
- registrate superfici critiche e attività aperte
