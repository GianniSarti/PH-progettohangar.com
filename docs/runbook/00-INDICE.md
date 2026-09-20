# Progetto Hangar — Runbook Infrastrutturale
Versione: 0.1  
Stato: Bozza iniziale  
Lingua: Italiano  
Formato: Markdown per GitHub  
Scopo: documentazione tecnica, operativa e replicabile per gestione, ripristino e continuità del progetto Progetto Hangar.

---

## 1. Obiettivo del Runbook

Questo Runbook descrive in modo strutturato l'infrastruttura, le dipendenze, le procedure operative e le misure di sicurezza del progetto **Progetto Hangar**.

È pensato per:

- mantenere una memoria tecnica affidabile del progetto
- permettere a un operatore umano o a una IA di comprendere rapidamente lo stato del sistema
- rendere replicabile l'infrastruttura
- ridurre il rischio operativo in caso di:
  - reinstallazione del computer principale
  - perdita di accesso locale
  - sostituzione VPS
  - migrazione provider
  - manutenzione straordinaria
  - incidente di sicurezza
- creare una base ordinata prima dello sviluppo pieno del sito e delle automazioni applicative

---

## 2. Principi di redazione

Questo Runbook segue i seguenti principi:

- **chiarezza prima di tutto**
- **ordine gerarchico**
- **ripetibilità**
- **minimo spazio per ambiguità**
- **preferenza per istruzioni operative verificabili**
- **separazione netta tra fatti, ipotesi, decisioni e attività future**
- **ottimizzazione per lettura da parte di IA e operatori tecnici**

Regole redazionali:

- un file = un argomento principale
- usare titoli stabili e numerati
- evitare narrativa superflua
- esplicitare sempre:
  - stato attuale
  - obiettivo
  - prerequisiti
  - rischi
  - passaggi operativi
  - output atteso
- non inserire segreti in chiaro
- usare placeholder per credenziali, token, chiavi e identificativi sensibili

---

## 3. Struttura del Runbook

Ordine consigliato dei file:

### Sezione 00 — Indice e orientamento
- `00-INDICE.md`
- `01-PANORAMICA.md`

### Sezione 02 — Inventario infrastruttura
- `02-INFRASTRUTTURA.md`
- `03-DNS-E-DOMINI.md`
- `04-VPS-E-HARDENING.md`

### Sezione 03 — Applicazioni e deploy
- `05-FRONTEND.md`
- `06-BACKEND.md`
- `07-DEPLOYMENT.md`
- `08-NGINX-E-HTTPS.md`

### Sezione 04 — Dati, servizi e integrazioni
- `09-DATABASE.md`
- `10-EMAIL.md`
- `11-STRIPE-MOR.md`
- `12-TRANSAZIONI-E-WEBHOOK.md`

### Sezione 05 — Sicurezza e continuità operativa
- `13-ACCESSI-E-IDENTITA.md`
- `14-SECRETS-INVENTORY.md`
- `15-BACKUP-E-RECOVERY.md`
- `16-MONITORAGGIO-E-MANUTENZIONE.md`
- `17-INCIDENT-RESPONSE.md`

### Sezione 06 — Contenuti, compliance e prodotto
- `18-PRODOTTI-E-SKU.md`
- `19-DISCLAIMER-E-COMPLIANCE.md`
- `20-I18N.md`

### Sezione 07 — Asset visivi e brand
- `21-BRAND-ASSETS.md`
- `22-IMMAGINI-PRODOTTO.md`

### Sezione 08 — Appendici
- `90-GLOSSARIO.md`
- `91-DECISIONI-ARCHITETTURALI.md`
- `99-CHANGELOG.md`

---

## 4. Stato attuale del progetto

Stato sintetico già confermato:

- brand definito: **Progetto Hangar**
- focus: boutique artigianale di Expert Advisor MT5
- tema visivo: aeronautico / biplano, elegante, retro, non kitsch
- frontend previsto su Cloudflare Pages
- backend previsto su VPS Ubuntu 24.04
- backend stack applicativo: FastAPI
- database: MongoDB Atlas
- repository: GitHub monorepo
- DNS e dominio già configurati
- endpoint `api.progettohangar.com` già attivo con nginx e HTTPS
- VPS già hardenizzata:
  - porta SSH custom `134`
  - utente operativo: `pilota`
  - accesso root disabilitato
  - UFW attivo
  - fail2ban attivo
- pagamenti: Stripe Managed Payments come Merchant of Record
- prodotti già definiti:
  - PH Falchetto — €222
  - PH Falco — €444
  - Upgrade — €234
- OpenNode rinviato a fase successiva, dopo costituzione entità societaria
- policy utente: evitare 2FA dove non strettamente obbligatorio dalla piattaforma

---

## 5. Ordine di priorità operativo

Priorità attuale:

1. consolidare il Runbook
2. inventariare e salvare accessi, chiavi e segreti
3. garantire capacità di ripristino dopo reinstallazione del Mac
4. solo dopo, proseguire con:
   - UI
   - contenuti
   - asset visuali
   - immagini prodotto
   - integrazione frontend/backend

---

## 6. Regole di sicurezza del repository

Nel repository del Runbook:

- non inserire mai:
  - password
  - token API
  - private key
  - seed phrase
  - recovery code
  - cookie di sessione
  - export completi di credenziali in chiaro
- usare invece placeholder come:
  - `<SSH_PRIVATE_KEY_LOCATION>`
  - `<STRIPE_SECRET_KEY_STORED_IN_PASSWORD_MANAGER>`
  - `<MONGODB_URI_STORED_SECURELY>`
- se necessario, riferirsi a:
  - password manager
  - archivio cifrato offline
  - dispositivo fisico dedicato
- ogni segreto deve avere:
  - nome
  - servizio
  - finalità
  - luogo di conservazione
  - responsabile
  - data ultimo controllo

---

## 7. Convenzioni di naming

Convenzioni raccomandate:

- file numerati con prefisso a due cifre
- nomi file in maiuscolo con trattini
- una sola lingua per ciascun file
- date in formato ISO:
  - `YYYY-MM-DD`
- stati consentiti:
  - `Bozza`
  - `Attivo`
  - `Da verificare`
  - `Deprecato`
- ambienti:
  - `local`
  - `staging` (se esisterà)
  - `production`

---

## 8. Uso del Runbook da parte di una IA

Questo Runbook è anche pensato per essere letto e usato da una IA operativa.

Per questo motivo:

- evitare riferimenti impliciti
- specificare sempre il contesto
- dichiarare esplicitamente dipendenze e prerequisiti
- distinguere chiaramente tra:
  - configurazione già esistente
  - azione da compiere
  - decisione ancora aperta
- aggiornare ogni file quando cambia un fatto infrastrutturale

Una IA che legge questo Runbook deve poter:

- ricostruire architettura e flussi
- capire dove si trovano i punti critici
- proporre manutenzione corretta
- assistere in un disaster recovery senza dover inferire troppo

---

## 9. File pronti in questa fase

File prodotti nella fase iniziale:

- `00-INDICE.md`
- `01-PANORAMICA.md`

File operativi da produrre subito dopo:

- `02-INFRASTRUTTURA.md`
- `14-SECRETS-INVENTORY.md`
- `15-BACKUP-E-RECOVERY.md`

---

## 10. Changelog iniziale

### v0.1
- definita struttura del Runbook
- registrato stato attuale sintetico del progetto
- fissate regole redazionali e di sicurezza
- formalizzato ordine di priorità operativo
