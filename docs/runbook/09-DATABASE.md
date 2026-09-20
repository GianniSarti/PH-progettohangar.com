# Progetto Hangar — Database
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive il database di **Progetto Hangar**: servizio, configurazione, struttura dati, accesso e sicurezza.

Serve a:

- documentare il servizio di persistenza e la sua configurazione
- descrivere la struttura logica dei dati
- chiarire accesso, sicurezza e backup del database
- fornire una base ricostruibile in caso di ripristino
- permettere a un operatore o a una IA di intervenire senza inferenze

Questo file non contiene segreti.  
URI, credenziali e stringhe di connessione sono gestiti secondo `14-SECRETS-INVENTORY`.

---

## 2. Servizio scelto

Servizio:

- MongoDB Atlas

Piano:

- M0 Free Tier

Regione:

- Francoforte

Motivazioni:

- database gestito senza overhead operativo iniziale
- costo iniziale nullo adatto alla fase di avvio
- buona integrazione con il backend FastAPI
- regione europea coerente con il contesto del progetto

---

## 3. Ruolo del database

Il database è il livello di persistenza dei dati applicativi.

Responsabilità principali:

- conservare i dati generati dal backend
- supportare i flussi di acquisto e post-acquisto
- fornire una base per eventuali funzionalità future (licenze, log applicativi, contatti)

Principio:

- solo il backend accede al database
- il frontend non accede mai direttamente al database

---

## 4. Modello dati logico

Il modello dati è documentale (MongoDB).  
Collezioni indicative attese (da consolidare con l'implementazione reale):

| Collezione | Scopo | Note |
|---|---|---|
| `orders` | ordini e transazioni | collegata agli eventi Stripe |
| `products` | catalogo prodotti | può riflettere gli SKU Stripe |
| `customers` | dati minimi cliente | rispettare minimizzazione dati |
| `licenses` | eventuali licenze/consegne | se previste per gli EA |
| `events` | log applicativi rilevanti | audit e diagnosi |

Nota:

- la struttura definitiva va documentata quando consolidata
- privilegiare la minimizzazione dei dati personali

---

## 5. Struttura indicativa dei documenti

Esempi logici (non vincolanti, da allineare al codice reale).

Ordine:

```text
order {
  _id
  stripe_session_id
  product_sku
  amount
  currency
  status
  customer_email
  created_at
  updated_at
}
```

Prodotto:

```text
product {
  _id
  sku
  name
  price
  currency
  active
}
```

Principi:

- usare campi coerenti e tipizzati
- includere sempre timestamp di creazione/aggiornamento
- evitare di memorizzare dati sensibili non necessari

---

## 6. Accesso e connessione

Il backend si connette tramite URI di connessione MongoDB.

Regole:

- l'URI contiene credenziali e non va mai salvato in chiaro nella documentazione
- l'URI è gestito come variabile di ambiente del backend (`MONGODB_URI`)
- l'URI reale è conservato secondo `14-SECRETS-INVENTORY`

Forma logica (senza credenziali reali):

```text
MONGODB_URI=mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>/<DB>?retryWrites=true&w=majority
```

---

## 7. Sicurezza del database

Misure di sicurezza:

- utente database dedicato con privilegi minimi necessari
- allowlist degli indirizzi IP autorizzati
- credenziali robuste e conservate in modo sicuro
- accesso limitato al solo backend

### 7.1 Allowlist IP
Principio:

- consentire l'accesso solo dagli IP legittimi (VPS backend)
- evitare regole eccessivamente permissive

Voci tipiche da documentare:

| IP consentito | Origine | Scopo | Note |
|---|---|---|---|
| `<IP_VPS>` | VPS backend | accesso applicativo | production |
| `<IP_OPERATORE>` | workstation | manutenzione | opzionale/temporaneo |

Nota:

- rimuovere IP temporanei quando non più necessari
- l'IP della VPS deve restare sempre autorizzato

---

## 8. Gestione utenti database

Principi:

- creare un utente applicativo dedicato per il backend
- assegnare solo i privilegi necessari sul database del progetto
- evitare l'uso di utenti con privilegi eccessivi per l'operatività ordinaria

Documentazione utenti (senza password):

| Utente DB | Privilegi | Scopo | Note |
|---|---|---|---|
| `<USER_APP>` | lettura/scrittura sul DB progetto | backend | credenziali in secrets |
| `<USER_ADMIN>` | amministrazione | gestione | uso limitato |

---

## 9. Backup del database

Strategia (coordinata con `15-BACKUP-E-RECOVERY`):

- valutare le funzionalità di backup disponibili sul piano M0
- eseguire export applicativi periodici dei dati critici
- conservare gli export in luogo sicuro e ridondante

Export logico:

```bash
mongodump --uri "<MONGODB_URI_SICURO>" --out ./backup-mongo-$(date +%F)
```

Ripristino:

```bash
mongorestore --uri "<MONGODB_URI_SICURO>" ./backup-mongo-<DATA>
```

Note:

- il piano gratuito può avere limiti sui backup automatici
- aumentare la frequenza degli export con la crescita dei dati
- non salvare l'URI in chiaro nella documentazione

---

## 10. Indici e prestazioni

Buone pratiche:

- creare indici sui campi usati per ricerche frequenti
- indicizzare identificativi come `stripe_session_id` e `sku`
- monitorare la crescita dei dati rispetto ai limiti del piano

Esempio logico di indice (concettuale):

```text
orders: index su stripe_session_id (unico)
products: index su sku (unico)
```

Nota:

- definire gli indici reali in base alle query effettive del backend

---

## 11. Limiti del piano M0

Consapevolezza dei limiti del Free Tier:

- capacità di archiviazione limitata
- risorse condivise
- possibili limiti su backup automatici e prestazioni

Implicazioni:

- monitorare l'uso dello spazio
- pianificare un eventuale upgrade quando il progetto cresce
- non fare affidamento esclusivo sui backup automatici del piano gratuito

---

## 12. Superfici critiche del database

Punti di attenzione:

- URI di connessione con credenziali
- allowlist IP configurata correttamente
- utenti con privilegi eccessivi
- assenza di backup verificati
- superamento dei limiti del piano gratuito

Mitigazioni:

- conservare l'URI solo in luogo sicuro
- mantenere allowlist minima e aggiornata
- applicare il principio del privilegio minimo
- eseguire e verificare export periodici

---

## 13. Procedura di ripristino del database

Sequenza logica di riferimento:

1. verificare l'accesso alla console MongoDB Atlas
2. verificare/riconfigurare cluster e utenti se necessario
3. aggiornare l'allowlist IP con l'IP della VPS
4. recuperare l'URI di connessione in modo sicuro
5. aggiornare la variabile `MONGODB_URI` nel backend
6. se necessario, ripristinare i dati con `mongorestore`
7. verificare la connessione del backend
8. aggiornare stato e changelog

---

## 14. Controlli di verifica

Verifiche di connettività e stato:

```bash
# verifica connessione dal backend (esempio via health che tocca il DB)
curl -I https://api.progettohangar.com/health

# verifica accesso con client mongo (se disponibile)
mongosh "<MONGODB_URI_SICURO>" --eval "db.runCommand({ ping: 1 })"
```

Esito atteso:

- connessione riuscita
- ping positivo
- backend in grado di leggere/scrivere

---

## 15. Assunzioni correnti

Assunzioni valide alla stesura:

- il database è MongoDB Atlas su piano M0, regione Francoforte
- solo il backend accede al database
- l'accesso è limitato tramite allowlist IP
- esiste un solo ambiente di produzione
- il modello dati è ancora in via di consolidamento

Se queste assunzioni cambiano, aggiornare il documento.

---

## 16. Attività aperte

Attività da completare:

- consolidare il modello dati e le collezioni reali
- definire e creare gli indici necessari
- compilare allowlist IP e utenti reali (senza segreti)
- verificare le opzioni di backup del piano
- stabilire la frequenza definitiva degli export
- monitorare l'uso dello spazio

---

## 17. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione del livello dati
- incompleto nel modello dati definitivo
- da aggiornare con l'evoluzione del backend

Dipendenze correlate:

- `06-BACKEND`
- `12-TRANSAZIONI-E-WEBHOOK`
- `14-SECRETS-INVENTORY`
- `15-BACKUP-E-RECOVERY`

---

## 18. Changelog

### v0.1
- documentato servizio, piano e regione del database
- descritti modello dati logico, accesso e sicurezza
- definiti backup, indici, limiti del piano e ripristino
- registrate superfici critiche e attività aperte
