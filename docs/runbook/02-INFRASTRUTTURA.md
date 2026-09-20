# Progetto Hangar — Infrastruttura
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la struttura infrastrutturale di **Progetto Hangar** a livello sistemico.

Serve a:

- censire i componenti attivi del progetto
- chiarire il ruolo di ogni servizio
- documentare le dipendenze tra i nodi principali
- fornire una base stabile per deploy, manutenzione, backup e disaster recovery
- permettere a un operatore umano o a una IA di comprendere rapidamente l'architettura senza dover ricostruire il contesto da zero

Questo file è un documento di quadro generale.  
I dettagli operativi di ciascun componente saranno descritti nei file specialistici successivi.

---

## 2. Obiettivo dell'infrastruttura

L'infrastruttura di Progetto Hangar è progettata per supportare una boutique digitale di Expert Advisor MT5 con le seguenti caratteristiche:

- presenza online professionale e premium
- backend indipendente e controllato direttamente
- frontend distribuito globalmente
- costo iniziale contenuto
- sicurezza pragmatica ma rigorosa
- facilità di manutenzione
- facilità di espansione futura
- separazione ordinata tra contenuti pubblici, logica applicativa, dati e servizi terzi

---

## 3. Principi architetturali adottati

L'infrastruttura segue questi principi:

- **semplicità prima della complessità**
- **servizi gestiti dove utile**
- **controllo diretto sui componenti critici**
- **riduzione delle superfici di errore**
- **documentazione prima della crescita**
- **replicabilità**
- **stack piccolo ma coerente**
- **separazione tra presentazione, logica e persistenza**

Interpretazione pratica dei principi:

- il frontend è distribuito tramite piattaforma gestita
- il backend risiede su VPS controllata direttamente
- il database è affidato a un servizio gestito esterno
- DNS e delivery edge sono delegati a Cloudflare
- pagamenti e compliance fiscale internazionale sono delegati a Stripe Managed Payments
- email dominio e email transazionali sono separate per minimizzare confusione operativa

---

## 4. Componenti principali

I componenti principali dell'infrastruttura sono:

- dominio e DNS
- frontend pubblico
- backend API
- reverse proxy e TLS
- database
- email di dominio
- email transazionali
- sistema di pagamento
- repository codice e documentazione
- workstation locale dell'operatore

---

## 5. Panorama sintetico dell'architettura

Vista logica semplificata:

1. l'utente visita il sito pubblico
2. il frontend viene servito da Cloudflare Pages
3. il frontend comunica con il backend tramite `api.progettohangar.com`
4. il backend gira sulla VPS Ubuntu
5. nginx riceve le richieste HTTPS e le inoltra all'app FastAPI
6. FastAPI usa MongoDB Atlas per i dati applicativi
7. Stripe gestisce checkout e pagamenti come Merchant of Record
8. Resend gestisce eventuali email transazionali
9. Fastmail gestisce la posta del dominio per uso operativo/manuale
10. GitHub conserva monorepo e documentazione tecnica

---

## 6. Elenco infrastrutturale attuale

### 6.1 Dominio
Dominio principale del progetto:

- `progettohangar.com`

Ruolo:

- identità pubblica del brand
- radice dei record DNS
- base per frontend, backend e email

---

### 6.2 DNS e rete edge
Servizio:

- Cloudflare

Ruolo:

- gestione DNS
- eventuale proxying dei record compatibili
- supporto al frontend deployato su Cloudflare Pages
- punto di controllo esterno dell'instradamento dei sottodomini

Stato noto:

- configurato
- operativo

---

### 6.3 Frontend pubblico
Tecnologie:

- Astro
- React

Hosting previsto:

- Cloudflare Pages

Ruolo:

- presentazione del brand
- pagine prodotto
- contenuti marketing
- interfaccia utente pubblica
- eventuale interazione con checkout e servizi backend

Caratteristiche desiderate:

- sito leggero
- caricamento rapido
- grafica premium
- struttura pulita
- predisposizione multilingua

Stato:

- architettura decisa
- implementazione contenuti/UI non ancora completata

---

### 6.4 Backend API
Tecnologia:

- FastAPI

Hosting:

- VPS Ubuntu 24.04

Ruolo:

- logica applicativa
- endpoint API
- orchestrazione comunicazioni con servizi terzi
- gestione webhook
- eventuale validazione licenze / flussi acquisto / automazioni future

Endpoint pubblico noto:

- `https://api.progettohangar.com`

Stato:

- raggiungibile
- pubblicato dietro nginx e HTTPS

---

### 6.5 Reverse proxy e terminazione HTTPS
Tecnologia:

- nginx

Ruolo:

- ricezione traffico HTTP/HTTPS
- inoltro richieste verso FastAPI
- terminazione TLS
- eventuale controllo basilare dell'esposizione pubblica

Stato:

- configurato
- attivo su `api.progettohangar.com`

---

### 6.6 Server applicativo
Tipologia:

- VPS

Sistema operativo:

- Ubuntu 24.04

Ruolo:

- esecuzione backend
- ospitalità del reverse proxy
- nodo infrastrutturale controllato direttamente

Stato hardening noto:

- utente operativo: `pilota`
- porta SSH custom: `134`
- accesso root SSH disabilitato
- UFW attivo
- fail2ban attivo

---

### 6.7 Database
Servizio:

- MongoDB Atlas

Piano:

- M0 Free Tier

Regione nota:

- Francoforte

Ruolo:

- persistenza dati applicativi
- eventuali record relativi a ordini, utenti, eventi, configurazioni e flussi applicativi futuri

Motivazioni della scelta:

- semplicità operativa
- costo iniziale minimo
- gestione esternalizzata del database
- integrazione adeguata con stack backend scelto

Stato:

- scelto e confermato

Nota:

- URI, credenziali, allowlist IP e configurazioni specifiche devono essere documentate nel file dedicato senza esporre segreti in chiaro

---

### 6.8 Pagamenti
Servizio:

- Stripe Managed Payments

Ruolo:

- gestione checkout
- incasso
- Merchant of Record
- supporto alla compliance IVA per beni digitali venduti globalmente

Motivazioni:

- ridurre carico fiscale-operativo
- evitare gestione diretta complessa dell'IVA internazionale
- usare una soluzione affidabile e riconosciuta

Stato:

- prodotti già creati
- metadata/SKU già impostati

Prodotti noti:

- PH Falchetto — €222
- PH Falco — €444
- Upgrade — €234

---

### 6.9 Email dominio
Servizio:

- Fastmail

Ruolo:

- gestione email del dominio
- caselle operative/manuali
- comunicazioni amministrative e di business

Stato:

- identificato come provider di posta principale per il dominio

---

### 6.10 Email transazionali
Servizio:

- Resend

Ruolo:

- invio email automatiche applicative
- conferme, notifiche, eventi di backend, eventuali email post-acquisto

Motivazione:

- separare email transazionali da caselle operative
- mantenere flusso più pulito e manutenibile

Stato:

- provider deciso

---

### 6.11 Repository e controllo versione
Servizio:

- GitHub

Modello:

- monorepo

Ruolo:

- versionamento codice
- contenitore documentazione tecnica
- base per workflow di sviluppo
- archivio ordinato del Runbook

Stato:

- confermato

Struttura logica attesa del monorepo:

- frontend
- backend
- documentazione / runbook
- eventuali script operativi

La struttura effettiva sarà documentata in file successivi.

---

### 6.12 Workstation locale
Dispositivo principale operativo:

- Mac dell'operatore

Ruolo:

- sviluppo
- accesso ai servizi
- gestione repository
- gestione deploy
- amministrazione VPS
- conservazione temporanea o permanente di chiavi e configurazioni locali

Rischio attuale:

- reinstallazione imminente del sistema operativo

Implicazione:

- priorità alta a backup di:
  - chiavi SSH
  - file di configurazione locali
  - accessi
  - token
  - recovery data
  - documentazione operativa

---

## 7. Flussi principali tra componenti

### 7.1 Flusso visitatore pubblico
- utente apre il sito
- Cloudflare Pages serve il frontend
- il frontend presenta contenuti, prodotti e navigazione

### 7.2 Flusso API
- il frontend invia richieste al backend
- il traffico raggiunge `api.progettohangar.com`
- nginx riceve la richiesta
- nginx inoltra a FastAPI
- FastAPI elabora e, se necessario, interagisce con MongoDB Atlas o servizi terzi

### 7.3 Flusso pagamento
- utente seleziona un prodotto
- l'acquisto passa tramite Stripe Managed Payments
- Stripe gestisce checkout e aspetti MoR
- eventuali eventi di pagamento possono essere propagati al backend via webhook

### 7.4 Flusso email transazionale
- un evento applicativo richiede invio email
- il backend chiama Resend
- Resend invia il messaggio dal sottodominio/configurazione dedicata

### 7.5 Flusso amministrativo
- l'operatore usa il Mac locale
- accede a GitHub, VPS, Cloudflare, Stripe, MongoDB Atlas, Fastmail e Resend
- la continuità operativa dipende dalla corretta conservazione di chiavi e segreti

---

## 8. Separazione delle responsabilità

Per chiarezza operativa, ogni componente ha una responsabilità principale.

| Componente | Responsabilità primaria |
|---|---|
| Cloudflare DNS | risoluzione DNS e instradamento esterno |
| Cloudflare Pages | hosting frontend statico/edge |
| VPS Ubuntu | esecuzione backend sotto controllo diretto |
| nginx | ingresso HTTP/HTTPS e reverse proxy |
| FastAPI | logica applicativa e API |
| MongoDB Atlas | persistenza dati |
| Stripe Managed Payments | checkout e Merchant of Record |
| Resend | email transazionali |
| Fastmail | email di dominio operative |
| GitHub | codice, versionamento, documentazione |
| Mac locale | amministrazione e sviluppo |

Questa separazione riduce ambiguità e facilita il troubleshooting.

---

## 9. Superfici critiche dell'infrastruttura

Le superfici più sensibili o ad alto rischio sono:

- accesso SSH alla VPS
- pannello Cloudflare
- accesso GitHub
- accesso Stripe
- accesso MongoDB Atlas
- segreti applicativi del backend
- configurazione DNS
- webhook di pagamento
- email transazionali
- backup locali delle chiavi

Questi punti devono essere sempre:

- censiti
- documentati
- verificati periodicamente
- protetti con particolare attenzione

---

## 10. Assunzioni operative attuali

Assunzioni valide al momento della stesura:

- esiste una sola VPS di produzione
- non esiste ancora ambiente staging formalizzato
- il traffico iniziale previsto è contenuto
- il database può stare su piano iniziale gestito
- il frontend può essere distribuito come sito statico/app leggera
- il backend non richiede al momento architetture distribuite complesse
- i pagamenti crypto non fanno parte del perimetro attuale

Se una di queste assunzioni cambia, il Runbook va aggiornato.

---

## 11. Vincoli progettuali

Vincoli rilevanti:

- budget iniziale da mantenere ragionevole
- massima chiarezza operativa prima dell'espansione
- preferenza per setup affidabile e leggibile
- necessità di compliance prudente per contenuti legati al trading
- policy personale: evitare 2FA dove non obbligatorio
- imminente reinstallazione della macchina locale, con rischio di perdita accessi se non documentati

---

## 12. Punti forti dell'architettura scelta

Vantaggi principali dell'architettura attuale:

- frontend globale e rapido tramite Cloudflare Pages
- backend sotto controllo diretto su VPS
- database gestito senza overhead iniziale elevato
- pagamenti delegati a MoR con vantaggio fiscale/operativo
- buona separazione dei ruoli tra servizi
- stack sufficientemente piccolo da restare governabile
- buona base per crescita ordinata

---

## 13. Limiti e attenzioni

Limiti o attenzioni correnti:

- una sola VPS rappresenta un single point of execution per il backend
- parte della resilienza dipende dalla qualità della documentazione
- l'assenza di staging può aumentare il rischio di modifiche dirette
- la perdita delle chiavi SSH o dei token può bloccare l'operatività
- parte della pipeline di deploy deve ancora essere formalizzata
- la fase visuale dipende ancora da asset non forniti

Questi limiti sono accettabili nella fase attuale, purché accompagnati da Runbook e backup disciplinati.

---

## 14. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come mappa generale dell'infrastruttura
- incompleto nei dettagli operativi
- base di riferimento per i capitoli successivi

Dipendenze logiche successive:

- `03-DNS-E-DOMINI.md`
- `04-VPS-E-HARDENING.md`
- `05-FRONTEND.md`
- `06-BACKEND.md`
- `09-DATABASE.md`
- `10-EMAIL.md`
- `11-STRIPE-MOR.md`
- `14-SECRETS-INVENTORY.md`
- `15-BACKUP-E-RECOVERY.md`

---

## 15. Changelog

### v0.1
- definita la mappa generale dell'infrastruttura
- censiti i componenti principali
- descritti i flussi logici essenziali
- registrati vincoli, punti forti e aree critiche
