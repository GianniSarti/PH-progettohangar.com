# Progetto Hangar — Disclaimer e Compliance
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento definisce l'approccio di **Progetto Hangar** ai disclaimer legali e alla compliance nella comunicazione di prodotti di trading automatico.

Serve a:

- proteggere il progetto da rischi legali e reputazionali
- definire come presentare risultati storici e backtest
- stabilire i disclaimer obbligatori
- garantire coerenza tra tutti i contenuti pubblicati
- permettere a un operatore o a una IA di produrre contenuti conformi

Nota importante:

- questo documento non è una consulenza legale
- prima della messa online definitiva, i testi legali vanno validati da un professionista

---

## 2. Principio guida della comunicazione

Principio fondamentale:

- comunicare con prudenza, trasparenza e onestà
- non promettere profitti
- non minimizzare i rischi
- presentare i risultati storici come tali, senza proiettarli sul futuro

Tono desiderato:

- tecnico
- misurato
- credibile
- privo di retorica da "guru del trading"

---

## 3. Rischi da mitigare

Rischi principali:

- accuse di promesse ingannevoli
- interpretazione dei backtest come garanzia di rendimento
- problematiche con normative su strumenti finanziari e pubblicità
- reclami di clienti insoddisfatti
- danno reputazionale

Strategia:

- linguaggio prudente
- disclaimer chiari e visibili
- presentazione corretta delle evidenze storiche

---

## 4. Presentazione dei backtest

Regola centrale:

- i backtest sono presentati come **esperimenti storici replicabili**, non come previsioni

Formulazioni consentite:

- "risultati storici di un esperimento su dati passati"
- "comportamento osservato in condizioni storiche specifiche"
- "test replicabile con i parametri indicati"

Formulazioni vietate:

- "guadagno garantito"
- "rendimento sicuro"
- "profitto mensile assicurato"
- "senza rischio"
- qualsiasi promessa esplicita o implicita di risultato futuro

---

## 5. Elementi da includere con i backtest

Ogni presentazione di risultati storici dovrebbe includere:

- periodo temporale dei dati
- strumento/mercato di riferimento
- parametri usati
- condizioni del test
- limiti e assunzioni
- disclaimer di rischio

Principio:

- rendere il test contestualizzato e, idealmente, replicabile
- evidenziare che i risultati passati non predicono quelli futuri

---

## 6. Disclaimer di rischio obbligatorio

Testo di riferimento (bozza da validare legalmente):

```text
I prodotti offerti da Progetto Hangar sono strumenti di trading automatico
destinati alla piattaforma MetaTrader 5. Il trading comporta un elevato
livello di rischio e può comportare la perdita totale del capitale investito.

I risultati storici e i backtest presentati rappresentano esperimenti su dati
passati in condizioni specifiche e NON costituiscono una previsione o una
garanzia di risultati futuri. Le performance passate non sono indicative di
performance future.

Progetto Hangar non fornisce consulenza finanziaria, di investimento o fiscale.
L'utente è l'unico responsabile delle proprie decisioni di trading e dovrebbe
valutare la propria situazione e, se necessario, consultare un professionista
qualificato.
```

Nota:

- adattare e far validare il testo da un legale
- mostrare il disclaimer in modo visibile

---

## 7. Posizionamento dei disclaimer

Dove mostrare i disclaimer:

- pagina prodotto (vicino a claim e risultati)
- pagina dedicata ai risultati/esperimenti storici
- footer del sito
- pagina legale dedicata
- eventuali email transazionali rilevanti
- documentazione di prodotto

Principio:

- il disclaimer deve essere presente dove l'utente vede risultati o claim

---

## 8. Pagine legali necessarie

Pagine legali tipiche da predisporre:

| Pagina | Scopo |
|---|---|
| Termini e Condizioni | regole d'uso e vendita |
| Informativa Privacy | trattamento dati personali |
| Cookie Policy | uso dei cookie |
| Disclaimer di rischio | avvertenze sul trading |
| Politica di rimborso | condizioni di rimborso |

Nota:

- i contenuti definitivi vanno validati legalmente
- coordinare con il modello MoR di Stripe per gli aspetti di vendita

---

## 9. Privacy e dati personali

Principi:

- raccogliere solo i dati necessari (minimizzazione)
- informare chiaramente l'utente sul trattamento
- gestire i dati in conformità alle normative applicabili (es. GDPR nell'UE)

Dati tipicamente trattati:

- email del cliente
- dati d'ordine
- eventuali dati necessari alla consegna

Riferimento:

- struttura dati in `09-DATABASE`

Nota:

- gran parte dei dati di pagamento è gestita da Stripe come MoR

---

## 10. Ruolo del Merchant of Record nella compliance

Con Stripe come MoR:

- Stripe è venditore di record verso il cliente
- Stripe gestisce IVA e aspetti fiscali delle transazioni
- parte della compliance di vendita è delegata a Stripe

Implicazioni:

- i termini di vendita devono essere coerenti con il modello MoR
- verificare cosa copre effettivamente il programma
- coordinare con la futura società portoghese

Riferimento:

- `11-STRIPE-MOR`

---

## 11. Coerenza con il brand

I disclaimer devono convivere con il tono premium del brand.

Principi:

- integrare i disclaimer in modo elegante ma visibile
- non nasconderli, ma nemmeno renderli allarmistici in modo incoerente
- mantenere il tono serio e professionale

Principio:

- la trasparenza rafforza la credibilità premium, non la indebolisce

---

## 12. Checklist di conformità dei contenuti

Prima di pubblicare un contenuto con claim o risultati:

- [ ] nessuna promessa di profitto
- [ ] nessuna minimizzazione del rischio
- [ ] backtest presentati come esperimenti storici
- [ ] contesto e parametri indicati
- [ ] disclaimer di rischio presente e visibile
- [ ] linguaggio prudente e coerente
- [ ] coerenza con le pagine legali

---

## 13. Superfici critiche

Punti di attenzione:

- claim troppo ottimistici
- risultati storici senza contesto o disclaimer
- pagine legali mancanti o non validate
- incoerenza tra pagine diverse
- mancata validazione legale prima del lancio

Mitigazioni:

- applicare la checklist di conformità
- validazione legale dei testi
- revisione periodica dei contenuti

---

## 14. Assunzioni correnti

Assunzioni valide alla stesura:

- vendita di prodotti digitali di trading automatico
- Stripe come MoR
- pubblico internazionale con priorità UE/Italia
- testi legali ancora da validare da un professionista

Se queste assunzioni cambiano, aggiornare il documento.

---

## 15. Attività aperte

Attività da completare:

- far validare legalmente tutti i testi
- redigere le pagine legali definitive
- definire la politica di rimborso
- integrare i disclaimer in tutte le sedi previste
- coordinare la compliance con la futura società

---

## 16. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come linea guida di comunicazione prudente
- non sostitutivo di una consulenza legale
- da completare con testi validati

Dipendenze correlate:

- `09-DATABASE`
- `10-EMAIL`
- `11-STRIPE-MOR`
- `18-PRODOTTI-E-SKU`

---

## 17. Changelog

### v0.1
- definito l'approccio prudente alla comunicazione
- stabilite regole per la presentazione dei backtest
- redatta bozza di disclaimer e mappa delle pagine legali
- registrate superfici critiche e attività aperte
