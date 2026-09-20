# Progetto Hangar — Stripe e Merchant of Record
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la configurazione dei pagamenti di **Progetto Hangar** tramite Stripe Managed Payments in qualità di Merchant of Record (MoR).

Serve a:

- documentare l'approccio ai pagamenti e alla compliance fiscale
- descrivere prodotti, prezzi e configurazione Stripe
- chiarire l'integrazione con il backend
- fornire una base ricostruibile in caso di ripristino
- permettere a un operatore o a una IA di intervenire senza inferenze

Questo file non contiene segreti.  
Le chiavi Stripe e i webhook secret sono gestiti secondo `14-SECRETS-INVENTORY`.

---

## 2. Approccio ai pagamenti

Soluzione scelta:

- Stripe Managed Payments come Merchant of Record

Significato:

- Stripe agisce come venditore di record verso il cliente finale
- Stripe gestisce la raccolta e il versamento dell'IVA e delle imposte applicabili
- riduce l'onere di compliance fiscale internazionale per beni digitali

Motivazioni:

- semplificare la gestione dell'IVA su vendite globali
- ridurre la complessità operativa e legale
- offrire un checkout affidabile e riconosciuto

---

## 3. Vantaggi del modello MoR

Vantaggi principali:

- gestione automatizzata della fiscalità sulle vendite digitali
- minor rischio di errori di compliance
- checkout professionale e sicuro
- supporto a più metodi di pagamento
- adatto a un venditore in fase di avvio

Implicazione:

- il progetto può concentrarsi sul prodotto e sul brand, delegando la complessità fiscale delle transazioni

---

## 4. Prodotti e prezzi

Prodotti definiti:

| Prodotto | Prezzo | SKU / riferimento | Note |
|---|---|---|---|
| PH Falchetto | €222 | `<SKU_FALCHETTO>` | EA MT5 |
| PH Falco | €444 | `<SKU_FALCO>` | EA MT5 |
| Upgrade | €234 | `<SKU_UPGRADE>` | passaggio/estensione |

Stato:

- prodotti già creati su Stripe
- metadata/SKU già impostati

Nota:

- gli identificativi reali (product id, price id) vanno documentati con i valori effettivi
- mantenere coerenza tra SKU Stripe e catalogo applicativo

---

## 5. Metadati e SKU

Principi:

- ogni prodotto Stripe ha metadati coerenti con il catalogo interno
- i metadati permettono al backend di riconoscere il prodotto acquistato

Metadati logici consigliati:

```text
sku: PH_FALCHETTO | PH_FALCO | PH_UPGRADE
product_type: expert_advisor | upgrade
delivery: digital
```

Nota:

- i metadati reali vanno verificati e documentati
- servono per collegare pagamento, ordine e consegna

---

## 6. Chiavi e configurazione

Il backend usa le chiavi Stripe come variabili di ambiente.

Variabili logiche:

```text
STRIPE_SECRET_KEY=<SEGRETO>
STRIPE_WEBHOOK_SECRET=<SEGRETO>
```

Chiave pubblica lato frontend:

```text
PUBLIC_STRIPE_PUBLISHABLE_KEY=<CHIAVE_PUBBLICA>
```

Regole:

- la secret key non deve mai essere esposta al client
- la publishable key può essere usata lato frontend
- tutte le chiavi sono tracciate in `14-SECRETS-INVENTORY`

---

## 7. Flusso di acquisto

Flusso logico:

1. l'utente seleziona un prodotto sul frontend
2. il frontend richiede al backend l'avvio del checkout
3. il backend crea una sessione di checkout Stripe con il prodotto/prezzo corretto
4. l'utente viene indirizzato al checkout Stripe
5. Stripe gestisce pagamento, IVA e conferma
6. Stripe reindirizza l'utente alla pagina di esito
7. Stripe invia un evento webhook al backend
8. il backend registra l'ordine ed eventualmente avvia la consegna

Dettagli sui webhook:

- descritti in `12-TRANSAZIONI-E-WEBHOOK`

---

## 8. Creazione della sessione di checkout

Principi:

- la sessione è creata lato backend
- il backend specifica prodotto/prezzo, modalità e URL di esito
- il backend non espone logica sensibile al frontend

Parametri logici tipici:

```text
mode: payment
line_items: [ price: <PRICE_ID> , quantity: 1 ]
success_url: https://progettohangar.com/esito/successo
cancel_url: https://progettohangar.com/esito/annullato
metadata: { sku: <SKU> }
```

Nota:

- i price id reali vanno documentati
- gli URL di esito devono corrispondere alle pagine reali del frontend

---

## 9. Gestione dell'IVA e compliance fiscale

Con il modello MoR:

- Stripe determina e applica l'IVA appropriata in base al cliente
- Stripe gestisce il versamento delle imposte dovute
- il progetto non deve gestire direttamente la registrazione IVA nei vari paesi per queste transazioni

Attenzioni:

- verificare le condizioni e le coperture effettive del programma Managed Payments
- conservare la documentazione fiscale fornita da Stripe
- coordinare con la futura entità societaria portoghese quando attiva

---

## 10. Relazione con la futura entità societaria

Stato attuale:

- il progetto opera in fase di avvio
- è prevista la costituzione di una società portoghese

Implicazioni:

- alcune configurazioni fiscali e di pagamento andranno riviste all'attivazione della società
- l'integrazione di pagamenti crypto (OpenNode) è rinviata a dopo la costituzione della società
- aggiornare questo capitolo quando l'entità è operativa

---

## 11. Rimborsi e gestione dei casi

Aspetti da definire:

- politica di rimborso per prodotti digitali
- gestione di dispute e chargeback tramite Stripe
- coerenza tra politica pubblicata e gestione operativa

Principi:

- pubblicare una politica di rimborso chiara
- gestire dispute tramite gli strumenti Stripe
- documentare le decisioni ricorrenti

Nota:

- coordinare con `19-DISCLAIMER-E-COMPLIANCE`

---

## 12. Superfici critiche dei pagamenti

Punti di attenzione:

- secret key Stripe
- webhook secret
- corretta associazione prodotto/prezzo/SKU
- URL di esito corretti
- coerenza tra catalogo Stripe e catalogo applicativo
- copertura effettiva del programma MoR

Mitigazioni:

- conservare le chiavi in modo sicuro
- validare sempre i webhook
- verificare periodicamente la coerenza del catalogo
- documentare product id e price id reali

---

## 13. Procedura di ripristino dei pagamenti

Sequenza logica di riferimento:

1. verificare l'accesso all'account Stripe
2. verificare prodotti, prezzi e metadati
3. recuperare le chiavi Stripe in modo sicuro
4. aggiornare le variabili di ambiente di backend e frontend
5. verificare la configurazione dei webhook (vedi `12-TRANSAZIONI-E-WEBHOOK`)
6. eseguire un acquisto di test
7. verificare la registrazione dell'ordine
8. aggiornare stato e changelog

---

## 14. Controlli di verifica

Verifiche consigliate:

- creare una sessione di checkout di test dal backend
- completare un pagamento in modalità test
- verificare la ricezione del webhook
- verificare la corretta registrazione dell'ordine
- verificare l'invio dell'email di conferma

Nota:

- usare l'ambiente/test mode di Stripe prima di operare in produzione

---

## 15. Assunzioni correnti

Assunzioni valide alla stesura:

- pagamenti tramite Stripe Managed Payments (MoR)
- prodotti e SKU già creati su Stripe
- il backend crea le sessioni di checkout
- l'IVA è gestita da Stripe come MoR
- crypto/OpenNode rinviato a dopo la società portoghese

Se queste assunzioni cambiano, aggiornare il documento.

---

## 16. Attività aperte

Attività da completare:

- documentare product id e price id reali
- confermare i metadati/SKU effettivi
- definire e pubblicare la politica di rimborso
- verificare la copertura effettiva del programma MoR
- completare l'integrazione checkout end-to-end
- coordinare la configurazione con la futura società

---

## 17. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione dell'impianto pagamenti e MoR
- incompleto negli identificativi reali e nelle politiche
- da aggiornare con l'implementazione e con l'attivazione societaria

Dipendenze correlate:

- `05-FRONTEND`
- `06-BACKEND`
- `10-EMAIL`
- `12-TRANSAZIONI-E-WEBHOOK`
- `14-SECRETS-INVENTORY`
- `18-PRODOTTI-E-SKU`
- `19-DISCLAIMER-E-COMPLIANCE`

---

## 18. Changelog

### v0.1
- documentato l'approccio Stripe Managed Payments come MoR
- descritti prodotti, prezzi, metadati e flusso di acquisto
- definiti gestione IVA, rimborsi e ripristino
- registrate superfici critiche e attività aperte
