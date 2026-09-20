# Progetto Hangar — Inventario dei Segreti
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento definisce l'inventario dei segreti di **Progetto Hangar**: credenziali, chiavi, token, dati di recupero e configurazioni sensibili.

Serve a:

- sapere sempre quali segreti esistono
- sapere dove sono conservati
- sapere a cosa servono
- garantire continuità operativa in caso di reinstallazione del Mac o sostituzione di dispositivi
- ridurre la dipendenza dalla memoria dell'operatore
- rendere possibile un disaster recovery ordinato

Questo documento è particolarmente importante nella fase attuale, vista l'imminente reinstallazione del sistema operativo della workstation.

---

## 2. Regola fondamentale di sicurezza

Regola inderogabile:

- in questo file NON vanno mai inseriti segreti in chiaro

Non inserire mai:

- password
- chiavi private
- token API
- webhook secret
- URI con credenziali incorporate
- seed phrase
- recovery code
- codici OTP
- cookie o token di sessione

In questo file vanno inseriti solo:

- nome del segreto
- servizio
- ambiente
- finalità
- luogo di conservazione
- responsabile
- stato
- data di ultimo controllo
- note non sensibili

---

## 3. Dove conservare i segreti reali

I valori reali dei segreti devono risiedere in luoghi sicuri e ridondanti, distinti da questo repository.

Luoghi raccomandati:

- password manager affidabile
- archivio cifrato offline
- supporto esterno cifrato dedicato

Requisiti:

- almeno due copie in luoghi distinti
- cifratura sempre attiva
- accesso controllato
- verifica periodica di integrità e recuperabilità

Regola:

- questo file indica dove trovare il segreto, non il segreto stesso

---

## 4. Convenzioni dell'inventario

Campi standard per ogni voce:

- **Nome segreto**: identificativo chiaro
- **Servizio**: piattaforma o sistema associato
- **Ambiente**: `local`, `production`, `personal`
- **Finalità**: a cosa serve
- **Dove è conservato**: luogo sicuro di riferimento (senza esporre il valore)
- **Responsabile**: chi lo gestisce
- **Stato**: `attivo`, `da verificare`, `da ruotare`, `deprecato`
- **Ultimo controllo**: data ISO `YYYY-MM-DD`
- **Note**: informazioni non sensibili

Placeholder consigliati:

- `<CONSERVATO_IN_PASSWORD_MANAGER>`
- `<CONSERVATO_IN_ARCHIVIO_CIFRATO_OFFLINE>`
- `<CONSERVATO_SU_SUPPORTO_ESTERNO_CIFRATO>`

---

## 5. Inventario principale dei segreti

Tabella da compilare con i riferimenti reali (senza valori sensibili).

| Nome segreto | Servizio | Ambiente | Finalità | Dove è conservato | Responsabile | Stato | Ultimo controllo | Note |
|---|---|---|---|---|---|---|---|---|
| SSH private key VPS | VPS | production | accesso server come `pilota` | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | porta `134` |
| SSH public key VPS | VPS | production | chiave pubblica autorizzata | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | da conservare con la privata |
| Password sudo `pilota` | VPS | production | operazioni amministrative | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | non salvare in chiaro nel repo |
| GitHub accesso / PAT | GitHub | production | accesso repo e workflow | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | verificare presenza token |
| GitHub recovery data | GitHub | personal | recupero accesso account | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | codici di backup |
| Cloudflare accesso account | Cloudflare | production | gestione DNS e Pages | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | superficie critica |
| Cloudflare API token | Cloudflare | production | automazioni DNS/deploy | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | solo se creato |
| Cloudflare recovery data | Cloudflare | personal | recupero accesso | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| MongoDB Atlas accesso | MongoDB Atlas | production | gestione cluster | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | account console |
| MongoDB connection URI | MongoDB Atlas | production | connessione backend al DB | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | non salvare URI in chiaro |
| MongoDB DB user/password | MongoDB Atlas | production | credenziali utente DB | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| MongoDB recovery data | MongoDB Atlas | personal | recupero accesso | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| Stripe accesso account | Stripe | production | gestione pagamenti/MoR | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | 2FA se obbligatoria |
| Stripe secret key | Stripe | production | API server-side | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | chiave critica |
| Stripe publishable key | Stripe | production | uso lato client | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | non segreta ma da tracciare |
| Stripe webhook secret | Stripe | production | validazione webhook | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| Stripe recovery data | Stripe | personal | recupero accesso | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| Resend API key | Resend | production | email transazionali | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| Resend accesso account | Resend | production | gestione invii/domini | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| Fastmail accesso account | Fastmail | production | posta di dominio | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| Fastmail app password | Fastmail | production | accesso client/app | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | se usata |
| Fastmail recovery data | Fastmail | personal | recupero accesso | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | |
| Backend `.env` production | Backend | production | config runtime | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | contiene più segreti |
| Registrar dominio accesso | Dominio | production | gestione dominio | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | se separato da Cloudflare |
| Apple ID / dispositivi recovery | Dispositivo | personal | continuità locale | `<DA_COMPILARE>` | Gianni | da verificare | `<DATA>` | utile per reinstall |

Regola:

- ogni nuovo segreto introdotto nel progetto va aggiunto qui immediatamente

---

## 6. Contenuto tipico del file di ambiente del backend

Il file di ambiente del backend è un contenitore di più segreti.  
Qui va documentata solo la struttura logica, non i valori.

Elenco logico delle variabili attese (nomi indicativi, da allineare al codice reale):

```text
MONGODB_URI=<SEGRETO>
STRIPE_SECRET_KEY=<SEGRETO>
STRIPE_WEBHOOK_SECRET=<SEGRETO>
RESEND_API_KEY=<SEGRETO>
APP_ENV=production
```

Regole:

- il file reale risiede sul server e/o in backup sicuro
- non deve essere versionato nel repository
- ogni variabile presente deve avere una voce corrispondente nell'inventario
- i nomi effettivi delle variabili vanno verificati nel codice del backend

---

## 7. Classificazione per priorità

### Priorità alta
Segreti la cui perdita blocca l'operatività o espone rischi gravi:

- SSH private key VPS
- password sudo `pilota`
- Stripe secret key
- Stripe webhook secret
- MongoDB connection URI e credenziali DB
- Cloudflare accesso e token
- GitHub accesso / PAT
- Resend API key
- backend `.env` production

### Priorità media
Segreti importanti ma con impatto più gestibile:

- Fastmail accesso e app password
- accesso registrar dominio
- recovery data dei vari servizi

### Priorità bassa
Elementi tracciabili ma rigenerabili o non sensibili:

- chiavi pubbliche
- Stripe publishable key
- valori DNS pubblici

---

## 8. Procedura di messa in sicurezza iniziale

Sequenza operativa consigliata, prioritaria prima del reinstall del Mac:

1. elencare tutti i segreti esistenti in questa tabella
2. per ciascuno, individuare il valore reale
3. salvare il valore nel password manager o archivio cifrato
4. creare una seconda copia in luogo distinto e cifrato
5. verificare che ogni voce abbia un luogo di conservazione compilato
6. testare almeno un recupero per i segreti ad alta priorità
7. aggiornare stato e data di ultimo controllo
8. aggiornare il changelog

Obiettivo:

- nessun segreto ad alta priorità deve dipendere solo dalla macchina locale

---

## 9. Rotazione dei segreti

Buone pratiche di rotazione:

- ruotare i segreti in caso di sospetto compromesso
- ruotare dopo eventi rilevanti, ad esempio prima o dopo la reinstallazione del sistema
- ruotare periodicamente i segreti ad alta priorità

Dopo ogni rotazione:

- aggiornare il valore nel luogo di conservazione sicuro
- aggiornare i sistemi che usano il segreto
- aggiornare stato e data in questo inventario
- verificare il funzionamento dei servizi impattati

Attenzione:

- la rotazione di alcuni segreti (URI DB, chiavi Stripe, webhook) richiede aggiornamento coordinato del backend

---

## 10. Regole per non esporre i segreti

Regole operative:

- non inserire segreti nel repository
- non inviarli via email o chat
- non salvarli in note cloud non cifrate
- non incollarli in strumenti non affidabili
- usare `.gitignore` per escludere i file di ambiente
- verificare periodicamente la cronologia del repository per evitare inclusioni accidentali

Verifica rapida che i file sensibili siano ignorati:

```bash
git check-ignore -v .env
```

---

## 11. Superfici critiche legate ai segreti

Punti più sensibili:

- workstation locale (imminente reinstallazione)
- backend `.env` sul server
- password manager e archivio cifrato
- accessi ai pannelli dei provider critici

Attenzioni:

- la compromissione del password manager avrebbe impatto ampio
- la perdita non ridondata dei segreti locali causerebbe blocco operativo
- l'esposizione accidentale in repository richiederebbe rotazione immediata

---

## 12. Assunzioni correnti

Assunzioni valide alla stesura:

- l'operatore principale e responsabile dei segreti è Gianni
- la politica personale prevede di evitare 2FA dove non obbligatorio
- alcuni servizi possono imporre comunque 2FA (es. Stripe, dispositivi Apple)
- esiste un solo ambiente di produzione
- i segreti reali risiedono fuori dal repository

Se queste assunzioni cambiano, aggiornare il documento.

---

## 13. Attività aperte

Attività da completare:

- compilare tutti i luoghi di conservazione
- verificare l'esistenza di token GitHub e Cloudflare
- confermare i nomi reali delle variabili nel backend
- eseguire e verificare le copie ridondanti
- testare il recupero dei segreti ad alta priorità
- completare stato e date di controllo

---

## 14. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come struttura di inventario dei segreti
- incompleto finché non compilato con i riferimenti reali
- prioritario da completare prima della reinstallazione del Mac

Dipendenze correlate:

- `04-VPS-E-HARDENING`
- `06-BACKEND`
- `09-DATABASE`
- `10-EMAIL`
- `11-STRIPE-MOR`
- `15-BACKUP-E-RECOVERY`

---

## 15. Changelog

### v0.1
- definita la struttura dell'inventario dei segreti
- creato l'elenco iniziale delle voci da censire
- stabilite regole di conservazione, rotazione e non esposizione
- classificate le priorità e definita la procedura di messa in sicurezza
