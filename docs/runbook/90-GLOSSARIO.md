# Progetto Hangar — Glossario
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento raccoglie i termini chiave di **Progetto Hangar**, tecnici e di brand.

Serve a:

- garantire un linguaggio comune
- assicurare coerenza terminologica tra documenti, contenuti e traduzioni
- permettere a un operatore o a una IA di interpretare correttamente i termini
- ridurre ambiguità

Questo file non contiene segreti.

---

## 2. Termini di brand e prodotto

| Termine | Definizione |
|---|---|
| Progetto Hangar | brand della boutique artigianale di Expert Advisor MT5 |
| PH | abbreviazione di Progetto Hangar |
| PH Falchetto | Expert Advisor di fascia base della linea (€222) |
| PH Falco | Expert Advisor di fascia superiore (€444) |
| Upgrade | prodotto di passaggio/estensione tra livelli (€234) |
| Box di prodotto | rappresentazione visiva del prodotto digitale come oggetto fisico |
| Tema aeronautico | linguaggio visivo ispirato a biplani ed aviazione vintage |

Nota:

- i nomi prodotto restano invariati in tutte le lingue

---

## 3. Termini di trading

| Termine | Definizione |
|---|---|
| MT5 | MetaTrader 5, piattaforma di trading |
| Expert Advisor (EA) | programma di trading automatico per MT5 |
| Bot di trading | sinonimo divulgativo di Expert Advisor |
| Backtest | test di una strategia su dati storici |
| Esperimento storico replicabile | modo in cui il progetto presenta i backtest |
| Drawdown | riduzione del capitale rispetto a un massimo precedente |
| Parametri | impostazioni configurabili di un EA |

Nota:

- la presentazione dei backtest segue `19-DISCLAIMER-E-COMPLIANCE`

---

## 4. Termini di infrastruttura

| Termine | Definizione |
|---|---|
| VPS | server virtuale privato che ospita il backend |
| Ubuntu 24.04 | sistema operativo della VPS |
| pilota | utente operativo non-root sulla VPS |
| SSH | protocollo di accesso remoto sicuro |
| Porta 134 | porta SSH custom del progetto |
| UFW | firewall di Ubuntu |
| fail2ban | strumento di blocco tentativi di accesso sospetti |
| nginx | reverse proxy e terminazione HTTPS |
| Reverse proxy | componente che inoltra le richieste al backend |
| TLS/HTTPS | protocollo di comunicazione cifrata |
| Let's Encrypt | autorità di certificazione per i certificati TLS |
| certbot | client per emissione/rinnovo certificati |

---

## 5. Termini applicativi

| Termine | Definizione |
|---|---|
| Frontend | interfaccia pubblica del sito |
| Backend | applicazione server-side |
| Astro | framework del frontend |
| React | libreria per componenti interattivi |
| FastAPI | framework del backend (Python) |
| uvicorn | server ASGI per eseguire FastAPI |
| API | interfaccia di programmazione tra frontend e backend |
| Endpoint | punto di accesso di una API |
| Health check | verifica di stato di un servizio |
| CORS | politica che regola le origini autorizzate a chiamare l'API |

---

## 6. Termini di dati

| Termine | Definizione |
|---|---|
| MongoDB | database documentale |
| MongoDB Atlas | servizio gestito di MongoDB |
| M0 Free Tier | piano gratuito di MongoDB Atlas |
| Collezione | insieme di documenti in MongoDB |
| Documento | record dati in MongoDB |
| URI di connessione | stringa con credenziali per connettersi al database |
| Allowlist IP | elenco di IP autorizzati ad accedere al database |
| mongodump / mongorestore | strumenti di export/import dei dati |

---

## 7. Termini di pagamento

| Termine | Definizione |
|---|---|
| Stripe | piattaforma di pagamento |
| Managed Payments | soluzione Stripe usata dal progetto |
| Merchant of Record (MoR) | soggetto venditore di record che gestisce la fiscalità |
| IVA | imposta sul valore aggiunto |
| Checkout | processo di pagamento |
| Sessione di checkout | istanza di pagamento creata dal backend |
| Webhook | notifica automatica di un evento da Stripe al backend |
| Webhook secret | segreto per validare i webhook |
| Idempotenza | proprietà che evita elaborazioni duplicate di uno stesso evento |
| SKU | codice identificativo di un prodotto |
| Product ID / Price ID | identificativi Stripe di prodotto e prezzo |
| OpenNode | servizio di pagamento BTC/Lightning, rinviato |

---

## 8. Termini email

| Termine | Definizione |
|---|---|
| Fastmail | provider della posta di dominio |
| Resend | provider delle email transazionali |
| Email transazionale | email automatica generata dal backend |
| SPF | record di autorizzazione dei server di invio |
| DKIM | firma crittografica dei messaggi |
| DMARC | politica di gestione dei messaggi non autenticati |
| Deliverability | capacità delle email di arrivare in casella |

---

## 9. Termini di rete e dominio

| Termine | Definizione |
|---|---|
| Cloudflare | provider DNS e hosting frontend (Pages) |
| Cloudflare Pages | piattaforma di hosting del frontend |
| DNS | sistema di risoluzione dei nomi di dominio |
| Record A / CNAME / MX / TXT | tipi di record DNS |
| Sottodominio | prefisso del dominio (es. `api`) |
| Proxy Cloudflare | modalità in cui il traffico passa attraverso Cloudflare |

---

## 10. Termini di sicurezza e operativi

| Termine | Definizione |
|---|---|
| Runbook | manuale operativo dell'infrastruttura |
| Segreto | credenziale, chiave o token sensibile |
| Secrets inventory | inventario dei segreti |
| Recovery code | codice di recupero accesso |
| 2FA | autenticazione a due fattori |
| Password manager | strumento di gestione delle credenziali |
| Backup | copia di sicurezza |
| Disaster recovery | ripristino dopo un evento grave |
| Incident response | risposta agli incidenti |
| Hardening | rafforzamento della sicurezza di un sistema |
| Rotazione | sostituzione periodica di un segreto |
| Privilegio minimo | assegnazione dei soli permessi necessari |

---

## 11. Termini di processo

| Termine | Definizione |
|---|---|
| Monorepo | singolo repository con più componenti |
| GitHub | piattaforma di versionamento del codice |
| Deploy | pubblicazione di una nuova versione |
| Rollback | ritorno a una versione precedente |
| Staging | ambiente di test (non ancora presente) |
| CI/CD | integrazione e distribuzione continua |
| i18n | internazionalizzazione (multilingua) |
| Fallback lingua | lingua usata quando manca una traduzione |
| Fase E | fase di creazione delle immagini/asset visivi |

---

## 12. Termini organizzativi

| Termine | Definizione |
|---|---|
| Operatore | responsabile tecnico e gestionale (Gianni) |
| Founder | fondatore del progetto |
| Società portoghese | futura entità societaria prevista |
| Compliance | conformità legale e normativa |
| Disclaimer | avvertenza legale |

---

## 13. Manutenzione del glossario

Regole:

- aggiungere ogni nuovo termine rilevante
- mantenere definizioni brevi e chiare
- usare questo glossario come riferimento per le traduzioni
- aggiornare quando cambiano termini o concetti

Riferimento:

- coerenza terminologica in `20-I18N`

---

## 14. Changelog

### v0.1
- creato il glossario iniziale dei termini chiave
- coperte aree brand, trading, infrastruttura, dati, pagamenti, email, rete, sicurezza, processo e organizzazione
