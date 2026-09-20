# Progetto Hangar — Frontend
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive il frontend pubblico di **Progetto Hangar**: tecnologie, struttura, build, deploy e relazione con backend e servizi.

Serve a:

- documentare lo stack e la struttura del frontend
- chiarire come viene costruito e pubblicato
- definire come comunica con il backend
- fornire una base ricostruibile in caso di ripristino
- permettere a un operatore o a una IA di intervenire senza inferenze

Questo file non contiene segreti.  
Eventuali variabili sensibili lato build vanno gestite secondo `14-SECRETS-INVENTORY`.

---

## 2. Ruolo del frontend

Il frontend è l'interfaccia pubblica del brand.

Responsabilità principali:

- presentare il brand in modo premium e coerente
- mostrare i prodotti (Expert Advisor MT5)
- presentare contenuti, evidenze storiche e disclaimer
- guidare l'utente verso l'acquisto tramite Stripe
- offrire un'esperienza pulita, rapida e ordinata

Non responsabilità:

- non gestisce logica sensibile lato server
- non conserva segreti applicativi
- non esegue operazioni critiche che competono al backend

---

## 3. Stack tecnologico

Tecnologie:

- Astro (framework principale)
- React (componenti interattivi)

Motivazioni:

- Astro produce siti leggeri e veloci, adatti a contenuti prevalentemente statici
- React consente isole interattive dove servono
- combinazione adatta a una vetrina premium con parti dinamiche mirate

Caratteristiche desiderate:

- performance elevate
- output ottimizzato
- struttura chiara dei componenti
- predisposizione multilingua

---

## 4. Hosting e distribuzione

Piattaforma di hosting:

- Cloudflare Pages

Ruolo:

- build e distribuzione globale del frontend
- delivery su rete edge
- integrazione con il dominio gestito su Cloudflare

Vantaggi:

- distribuzione rapida e globale
- integrazione naturale con DNS Cloudflare
- gestione semplice dei deploy da repository

---

## 5. Struttura logica del progetto frontend

Struttura indicativa (da allineare all'implementazione reale nel monorepo):

```text
frontend/
  src/
    pages/
    components/
    layouts/
    styles/
    i18n/
    assets/
  public/
  astro.config.mjs
  package.json
```

Note:

- `pages` contiene le rotte del sito
- `components` contiene i componenti riutilizzabili (inclusi quelli React)
- `layouts` definisce le strutture di pagina comuni
- `i18n` gestisce le traduzioni
- `assets` contiene immagini e risorse statiche
- la struttura effettiva va documentata quando consolidata

---

## 6. Pagine principali previste

Pagine di base attese:

- home / presentazione brand
- catalogo prodotti
- pagina prodotto (PH Falchetto, PH Falco, Upgrade)
- pagina evidenze storiche / esperimenti replicabili
- pagina legale / disclaimer
- contatti
- pagine di esito acquisto (successo / annullamento)

Nota:

- la struttura definitiva delle pagine è ancora una decisione aperta
- va allineata con contenuti e branding

---

## 7. Comunicazione con il backend

Il frontend comunica con il backend tramite l'endpoint pubblico:

- `https://api.progettohangar.com`

Principi:

- il frontend chiama solo endpoint pubblici previsti
- non incorpora segreti server-side
- eventuali chiavi pubbliche (es. Stripe publishable key) sono ammesse lato client
- la logica sensibile resta sul backend

Configurazione tipica:

- l'URL base dell'API va gestito come variabile di ambiente di build
- differenziare eventuale ambiente locale da produzione

Esempio logico di variabile:

```text
PUBLIC_API_BASE_URL=https://api.progettohangar.com
```

Nota:

- in Astro le variabili esposte al client seguono convenzioni specifiche (prefisso pubblico)
- verificare i nomi reali nel codice

---

## 8. Integrazione pagamenti lato frontend

Il frontend avvia il flusso di acquisto verso Stripe.

Principi:

- il frontend usa solo dati pubblici (publishable key, identificativi prodotto)
- la creazione delle sessioni di pagamento e la logica sensibile avvengono lato backend
- l'esito del pagamento è gestito tramite pagine dedicate e/o conferme del backend

Dettagli specifici:

- la logica completa è descritta in `11-STRIPE-MOR` e `12-TRANSAZIONI-E-WEBHOOK`

---

## 9. Internazionalizzazione (i18n)

Lingue previste:

- italiano: primaria
- inglese: secondaria
- spagnolo: stub iniziale

Principi:

- struttura predisposta al multilingua fin dall'inizio
- contenuti italiani completi come priorità
- evitare traduzioni incomplete pubblicate come definitive

Dettagli specifici:

- descritti in `20-I18N`

---

## 10. Direzione UI/UX

Direzione stilistica:

- tema aeronautico vintage / biplano
- eleganza retro
- materiali percepiti come fisici
- pulizia e ordine
- assenza di affollamento grafico

Elementi visuali chiave:

- prodotti digitali presentati come oggetti/box fisici
- immagini prodotto basate su screenshot MT5 armonizzati
- palette coerente con il brand

Dettagli specifici:

- asset e immagini descritti in `21-BRAND-ASSETS` e `22-IMMAGINI-PRODOTTO`

---

## 11. Build del frontend

Comandi tipici (da allineare al `package.json` reale):

```bash
# installazione dipendenze
npm install

# sviluppo locale
npm run dev

# build di produzione
npm run build

# anteprima build
npm run preview
```

Note:

- l'output di build viene pubblicato tramite Cloudflare Pages
- verificare la cartella di output attesa dalla configurazione Astro

---

## 12. Deploy del frontend

Modello di deploy:

- deploy collegato al repository GitHub
- build automatica su Cloudflare Pages al push
- pubblicazione su dominio gestito da Cloudflare

Dettagli specifici del flusso di rilascio:

- descritti in `07-DEPLOYMENT`

Principi:

- deploy ripetibili
- separazione tra codice e configurazione sensibile
- verifica post-deploy

---

## 13. Variabili di ambiente lato frontend

Regole:

- solo variabili non sensibili possono essere esposte al client
- le variabili pubbliche devono usare le convenzioni previste da Astro
- nessun segreto server-side nel bundle frontend

Variabili tipiche:

```text
PUBLIC_API_BASE_URL=<URL_API>
PUBLIC_STRIPE_PUBLISHABLE_KEY=<CHIAVE_PUBBLICA>
```

Nota:

- le chiavi pubbliche non sono segrete, ma vanno comunque tracciate in `14-SECRETS-INVENTORY`

---

## 14. Superfici critiche del frontend

Punti di attenzione:

- accidentale inclusione di segreti nel bundle client
- errata configurazione dell'URL API
- rottura del flusso di pagamento
- traduzioni incomplete pubblicate
- asset pesanti che degradano le performance

Mitigazioni:

- revisione delle variabili esposte
- test del flusso di acquisto dopo ogni modifica rilevante
- controllo performance e peso degli asset

---

## 15. Assunzioni correnti

Assunzioni valide alla stesura:

- il frontend è servito da Cloudflare Pages
- lo stack è Astro + React
- l'API è raggiungibile su `api.progettohangar.com`
- non esiste ancora un ambiente di staging formalizzato
- il contenuto definitivo è in fase di sviluppo

Se queste assunzioni cambiano, aggiornare il documento.

---

## 16. Attività aperte

Attività da completare:

- consolidare la struttura definitiva delle pagine
- definire i contenuti reali
- integrare completamente il flusso di pagamento
- completare la configurazione i18n
- integrare gli asset visuali definitivi
- documentare la struttura reale del progetto nel monorepo

---

## 17. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione dell'impianto frontend
- incompleto nei dettagli implementativi finali
- da aggiornare durante lo sviluppo dell'interfaccia

Dipendenze correlate:

- `02-INFRASTRUTTURA`
- `06-BACKEND`
- `07-DEPLOYMENT`
- `11-STRIPE-MOR`
- `20-I18N`
- `21-BRAND-ASSETS`
- `22-IMMAGINI-PRODOTTO`

---

## 18. Changelog

### v0.1
- documentato stack, hosting e struttura del frontend
- descritte comunicazione con il backend e integrazione pagamenti
- definiti build, deploy e variabili di ambiente
- registrate superfici critiche e attività aperte
