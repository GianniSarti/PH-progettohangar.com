# Progetto Hangar — Backend
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive il backend di **Progetto Hangar**: tecnologia, struttura, esecuzione, configurazione e integrazioni.

Serve a:

- documentare lo stack e la struttura del backend
- descrivere come viene eseguito e gestito sulla VPS
- chiarire configurazione e variabili di ambiente
- fornire una base ricostruibile in caso di ripristino
- permettere a un operatore o a una IA di intervenire senza inferenze

Questo file non contiene segreti.  
Le variabili sensibili sono gestite secondo `14-SECRETS-INVENTORY`.

---

## 2. Ruolo del backend

Il backend è il nodo applicativo controllato direttamente.

Responsabilità principali:

- esporre le API necessarie al frontend
- gestire la logica sensibile lato server
- orchestrare le integrazioni con Stripe, MongoDB e servizi email
- ricevere e validare i webhook di pagamento
- gestire eventuali flussi post-acquisto e automazioni future

Caratteristiche:

- gira su VPS Ubuntu 24.04
- esposto pubblicamente tramite `api.progettohangar.com`
- servito dietro nginx con HTTPS

---

## 3. Stack tecnologico

Tecnologia principale:

- FastAPI (Python)

Motivazioni:

- framework moderno e performante
- adatto a API pulite e ben documentate
- buona integrazione con MongoDB e servizi terzi
- generazione automatica di documentazione API

Componenti tipici associati:

- server ASGI (es. uvicorn)
- driver MongoDB
- librerie per integrazione Stripe ed email

Nota:

- versioni e dipendenze esatte vanno documentate nel file dei requisiti del progetto

---

## 4. Struttura logica del progetto backend

Struttura indicativa (da allineare all'implementazione reale nel monorepo):

```text
backend/
  app/
    main.py
    api/
    models/
    services/
    core/
    config.py
  requirements.txt
  .env            # non versionato
```

Note:

- `main.py` è il punto di ingresso dell'applicazione
- `api` contiene le rotte/endpoint
- `models` contiene le strutture dati
- `services` contiene la logica di integrazione (Stripe, email, DB)
- `core` / `config` contengono configurazione e utilità
- il file `.env` non deve essere versionato

---

## 5. Endpoint e superficie API

Categorie tipiche di endpoint attese:

- endpoint di stato/salute
- endpoint prodotti
- endpoint per avvio checkout Stripe
- endpoint webhook Stripe
- eventuali endpoint post-acquisto (consegna, licenze, notifiche)

Endpoint di salute (esempio logico):

```text
GET /health
```

Nota:

- l'elenco definitivo va documentato quando gli endpoint sono consolidati
- FastAPI espone documentazione automatica, la cui accessibilità pubblica va valutata per motivi di sicurezza

---

## 6. Configurazione e variabili di ambiente

Il backend è configurato tramite variabili di ambiente.

Variabili logiche attese (nomi da allineare al codice reale):

```text
APP_ENV=production
MONGODB_URI=<SEGRETO>
STRIPE_SECRET_KEY=<SEGRETO>
STRIPE_WEBHOOK_SECRET=<SEGRETO>
RESEND_API_KEY=<SEGRETO>
ALLOWED_ORIGINS=<DOMINI_FRONTEND>
```

Regole:

- il file `.env` risiede sul server e in backup sicuro
- non deve essere versionato
- ogni variabile sensibile ha una voce in `14-SECRETS-INVENTORY`

---

## 7. CORS e sicurezza applicativa

Aspetti di sicurezza a livello applicativo:

- configurare correttamente CORS per accettare solo le origini del frontend
- validare gli input degli endpoint
- proteggere gli endpoint sensibili
- validare la firma dei webhook Stripe
- non esporre informazioni sensibili nei messaggi di errore

Principio CORS:

- consentire solo i domini legittimi del frontend
- evitare configurazioni permissive non necessarie

---

## 8. Esecuzione del backend

Il backend gira come servizio sulla VPS.

Modalità tipica:

- applicazione ASGI eseguita tramite uvicorn
- gestita come servizio di sistema per riavvio automatico e supervisione

Esecuzione manuale per test (esempio):

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Nota:

- in produzione il backend ascolta su localhost e viene esposto tramite nginx
- l'esposizione pubblica diretta non è desiderata: passa sempre per il reverse proxy

---

## 9. Gestione come servizio di sistema

Per garantire continuità, il backend è gestito come servizio.

Modello logico di servizio (esempio indicativo systemd):

```text
[Unit]
Description=Progetto Hangar Backend
After=network.target

[Service]
User=pilota
WorkingDirectory=/percorso/backend
EnvironmentFile=/percorso/backend/.env
ExecStart=/percorso/venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Comandi di gestione tipici:

```bash
sudo systemctl status <nome-servizio>
sudo systemctl restart <nome-servizio>
sudo journalctl -u <nome-servizio> -e
```

Nota:

- percorsi, nome servizio e ambiente virtuale vanno documentati con i valori reali
- il file di servizio va incluso nei backup delle configurazioni

---

## 10. Ambiente Python e dipendenze

Gestione dipendenze:

- usare un ambiente virtuale dedicato
- fissare le dipendenze in un file dei requisiti

Comandi tipici:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Note:

- mantenere aggiornato `requirements.txt`
- documentare la versione di Python usata
- dopo aggiornamenti rilevanti, testare gli endpoint principali

---

## 11. Integrazioni del backend

Il backend integra i seguenti servizi:

- MongoDB Atlas per la persistenza dati
- Stripe per pagamenti e webhook
- Resend per email transazionali

Dettagli specifici:

- database: `09-DATABASE`
- pagamenti: `11-STRIPE-MOR`
- webhook: `12-TRANSAZIONI-E-WEBHOOK`
- email: `10-EMAIL`

Principio:

- ogni integrazione usa segreti gestiti tramite variabili di ambiente
- la logica sensibile resta lato backend

---

## 12. Log e osservabilità

Aspetti di base:

- il backend produce log accessibili tramite il gestore del servizio
- i log servono per diagnosi e sicurezza

Accesso ai log:

```bash
sudo journalctl -u <nome-servizio> -e
```

Dettagli su monitoraggio e manutenzione:

- descritti in `16-MONITORAGGIO-E-MANUTENZIONE`

Nota:

- evitare di registrare segreti o dati sensibili nei log

---

## 13. Superfici critiche del backend

Punti di attenzione:

- file `.env` con i segreti
- validazione dei webhook Stripe
- configurazione CORS
- esposizione della documentazione automatica
- gestione degli errori
- accesso al servizio e ai log

Mitigazioni:

- proteggere e non versionare `.env`
- validare sempre le firme dei webhook
- limitare CORS ai domini legittimi
- valutare la protezione o disabilitazione della documentazione pubblica in produzione

---

## 14. Procedura di ripristino del backend

Sequenza logica di riferimento:

1. preparare la VPS secondo `04-VPS-E-HARDENING`
2. clonare il monorepo da GitHub
3. creare l'ambiente virtuale e installare le dipendenze
4. ripristinare il file `.env` dal backup sicuro
5. configurare il servizio di sistema
6. avviare e verificare il servizio
7. verificare la connessione a MongoDB
8. verificare le integrazioni Stripe ed email
9. verificare la raggiungibilità pubblica via nginx/HTTPS
10. aggiornare stato e changelog

---

## 15. Controlli di verifica

Verifiche post-avvio o post-ripristino:

```bash
# stato servizio
sudo systemctl status <nome-servizio>

# health locale
curl -I http://127.0.0.1:8000/health

# health pubblica
curl -I https://api.progettohangar.com/health
```

Esito atteso:

- servizio attivo e in esecuzione
- health locale e pubblica rispondono correttamente
- integrazioni funzionanti

---

## 16. Assunzioni correnti

Assunzioni valide alla stesura:

- il backend è FastAPI su VPS Ubuntu 24.04
- ascolta su localhost ed è esposto tramite nginx
- usa MongoDB Atlas, Stripe e Resend
- il file `.env` non è versionato
- esiste un solo ambiente di produzione

Se queste assunzioni cambiano, aggiornare il documento.

---

## 17. Attività aperte

Attività da completare:

- consolidare la struttura reale del progetto
- documentare l'elenco definitivo degli endpoint
- confermare i nomi reali delle variabili di ambiente
- formalizzare il file del servizio di sistema
- allineare con i capitoli di database, pagamenti, webhook ed email
- valutare la protezione della documentazione automatica in produzione

---

## 18. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione dell'impianto backend
- incompleto nei dettagli implementativi finali
- da aggiornare durante lo sviluppo applicativo

Dipendenze correlate:

- `04-VPS-E-HARDENING`
- `05-FRONTEND`
- `07-DEPLOYMENT`
- `08-NGINX-E-HTTPS`
- `09-DATABASE`
- `10-EMAIL`
- `11-STRIPE-MOR`
- `12-TRANSAZIONI-E-WEBHOOK`
- `14-SECRETS-INVENTORY`

---

## 19. Changelog

### v0.1
- documentato stack, struttura ed esecuzione del backend
- descritte configurazione, integrazioni e sicurezza applicativa
- definiti servizio di sistema, ripristino e verifiche
- registrate superfici critiche e attività aperte
