# Progetto Hangar — Prodotti e SKU
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive il catalogo prodotti di **Progetto Hangar**: Expert Advisor MT5, prezzi, SKU e relazione con Stripe.

Serve a:

- documentare i prodotti e i loro identificativi
- mantenere coerenza tra Stripe, backend e frontend
- chiarire la struttura del catalogo
- fornire una base ricostruibile del catalogo
- permettere a un operatore o a una IA di gestire i prodotti senza inferenze

Questo file non contiene segreti.

---

## 2. Natura dei prodotti

I prodotti sono Expert Advisor (EA) per MetaTrader 5.

Caratteristiche:

- prodotti digitali
- consegna digitale
- presentati con un linguaggio premium e artigianale
- accompagnati da evidenze storiche presentate in modo prudente

Presentazione visiva:

- i prodotti digitali sono presentati come oggetti/box fisici eleganti
- vedi `22-IMMAGINI-PRODOTTO`

---

## 3. Catalogo attuale

| Prodotto | Prezzo | Tipo | Descrizione sintetica |
|---|---|---|---|
| PH Falchetto | €222 | Expert Advisor | EA di fascia base della linea |
| PH Falco | €444 | Expert Advisor | EA di fascia superiore |
| Upgrade | €234 | Upgrade | passaggio/estensione tra prodotti |

Stato:

- prodotti creati su Stripe
- metadata/SKU impostati

Nota:

- descrizioni definitive e specifiche tecniche sono da consolidare

---

## 4. Struttura SKU

Schema SKU logico consigliato:

```text
PH_FALCHETTO
PH_FALCO
PH_UPGRADE
```

Principi:

- SKU stabili e leggibili
- coerenti tra Stripe, backend e database
- non modificarli senza aggiornare tutti i sistemi

---

## 5. Mappatura Stripe

Tabella di corrispondenza da compilare con i valori reali.

| SKU | Nome | Prezzo | Stripe Product ID | Stripe Price ID | Note |
|---|---|---|---|---|---|
| `PH_FALCHETTO` | PH Falchetto | €222 | `<PRODUCT_ID>` | `<PRICE_ID>` | |
| `PH_FALCO` | PH Falco | €444 | `<PRODUCT_ID>` | `<PRICE_ID>` | |
| `PH_UPGRADE` | Upgrade | €234 | `<PRODUCT_ID>` | `<PRICE_ID>` | |

Regola:

- ogni modifica su Stripe va riflessa qui
- product id e price id sono la fonte per la creazione delle sessioni di checkout

---

## 6. Metadati prodotto

Metadati consigliati su Stripe e nel catalogo interno:

```text
sku: PH_FALCHETTO | PH_FALCO | PH_UPGRADE
product_type: expert_advisor | upgrade
platform: mt5
delivery: digital
```

Utilità:

- permettono al backend di riconoscere il prodotto acquistato
- guidano la logica di consegna
- mantengono coerenza tra i sistemi

---

## 7. Relazione tra prodotti

Logica del catalogo:

- PH Falchetto: prodotto di ingresso
- PH Falco: prodotto superiore
- Upgrade: percorso di passaggio/estensione

Nota:

- la logica esatta dell'Upgrade (da cosa a cosa, condizioni) va definita e documentata
- eventuali regole di idoneità all'upgrade vanno chiarite

---

## 8. Prezzi e valuta

Caratteristiche:

- valuta principale: Euro
- prezzi definiti come importi fissi
- IVA gestita da Stripe come Merchant of Record

Nota:

- i prezzi mostrati e la gestione fiscale seguono il modello MoR
- vedi `11-STRIPE-MOR`

---

## 9. Consegna del prodotto

La consegna è digitale.

Modalità possibili (da definire):

- invio via email transazionale
- area/link di download
- eventuale gestione licenze

Principi:

- consegna affidabile e tracciata
- collegata all'evento di pagamento confermato
- ripetibile in caso di problemi

Riferimenti:

- `12-TRANSAZIONI-E-WEBHOOK`, `10-EMAIL`

---

## 10. Contenuti di prodotto

Ogni prodotto dovrebbe avere:

- nome e claim
- descrizione sintetica e completa
- caratteristiche principali
- evidenze storiche presentate in modo prudente
- disclaimer obbligatori
- immagini/box di prodotto

Riferimenti:

- `19-DISCLAIMER-E-COMPLIANCE`, `22-IMMAGINI-PRODOTTO`

Nota:

- i contenuti definitivi sono ancora da produrre

---

## 11. Coerenza tra sistemi

Regola fondamentale:

- il catalogo deve restare coerente tra Stripe, backend, database e frontend

Punti di sincronizzazione:

- SKU
- prezzi
- stato attivo/non attivo
- metadati

Verifica periodica:

- confrontare il catalogo Stripe con il catalogo applicativo
- correggere eventuali disallineamenti

---

## 12. Gestione delle modifiche al catalogo

Quando si modifica un prodotto o un prezzo:

1. valutare l'impatto su Stripe, backend e frontend
2. aggiornare Stripe (product/price)
3. aggiornare la mappatura in questo documento
4. aggiornare il catalogo applicativo
5. verificare il flusso di acquisto
6. aggiornare il changelog

Nota:

- modificare un prezzo tipicamente comporta un nuovo price id su Stripe
- non riutilizzare SKU per prodotti diversi

---

## 13. Superfici critiche

Punti di attenzione:

- disallineamento tra Stripe e catalogo applicativo
- price id errati nelle sessioni di checkout
- SKU incoerenti
- consegna non definita o non affidabile
- contenuti privi di disclaimer

Mitigazioni:

- documentare product id e price id reali
- mantenere SKU stabili
- verificare periodicamente la coerenza
- definire la consegna e i disclaimer

---

## 14. Assunzioni correnti

Assunzioni valide alla stesura:

- catalogo composto da tre voci (Falchetto, Falco, Upgrade)
- prezzi in Euro con IVA gestita da Stripe MoR
- prodotti già creati su Stripe
- consegna digitale ancora da definire nel dettaglio

Se queste assunzioni cambiano, aggiornare il documento.

---

## 15. Attività aperte

Attività da completare:

- documentare product id e price id reali
- definire la logica dell'Upgrade
- definire la modalità di consegna
- produrre i contenuti di prodotto
- integrare immagini e box
- verificare la coerenza tra i sistemi

---

## 16. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come struttura del catalogo
- incompleto negli identificativi reali e nei contenuti
- da aggiornare con l'implementazione

Dipendenze correlate:

- `05-FRONTEND`
- `06-BACKEND`
- `09-DATABASE`
- `11-STRIPE-MOR`
- `12-TRANSAZIONI-E-WEBHOOK`
- `19-DISCLAIMER-E-COMPLIANCE`
- `22-IMMAGINI-PRODOTTO`

---

## 17. Changelog

### v0.1
- documentato il catalogo prodotti e la struttura SKU
- definite mappatura Stripe, metadati e relazioni tra prodotti
- descritte consegna, coerenza tra sistemi e gestione modifiche
- registrate superfici critiche e attività aperte
