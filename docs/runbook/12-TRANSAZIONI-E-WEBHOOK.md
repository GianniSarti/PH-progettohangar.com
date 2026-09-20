# Progetto Hangar — Transazioni e Webhook
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la gestione delle transazioni e dei webhook di pagamento di **Progetto Hangar**.

Serve a:

- documentare come il backend riceve e valida gli eventi Stripe
- descrivere il ciclo di vita di una transazione
- chiarire la logica post-acquisto (ordine, consegna, email)
- garantire affidabilità e sicurezza del flusso di pagamento
- permettere a un operatore o a una IA di intervenire senza inferenze

Questo file non contiene segreti.  
Il webhook secret è gestito secondo `14-SECRETS-INVENTORY`.

---

## 2. Ruolo dei webhook

I webhook sono il meccanismo con cui Stripe notifica al backend gli eventi di pagamento.

Importanza:

- garantiscono che l'ordine sia registrato in modo affidabile
- non dipendono dal ritorno del browser dell'utente
- sono la fonte autorevole dello stato del pagamento

Principio:

- la conferma dell'ordine si basa sui webhook, non solo sul redirect di successo

---

## 3. Endpoint webhook

Il backend espone un endpoint dedicato per i webhook Stripe.

Endpoint logico:

```text
POST /webhooks/stripe
```

Caratteristiche:

- raggiungibile pubblicamente tramite `api.progettohangar.com`
- riceve gli eventi inviati da Stripe
- valida ogni evento prima di elaborarlo

---

## 4. Validazione della firma

Ogni webhook deve essere validato.

Principi:

- Stripe firma ogni evento con una firma nell'header
- il backend verifica la firma usando il webhook secret
- gli eventi non validi vengono rifiutati

Logica di validazione (concettuale):

```text
1. leggere il payload grezzo della richiesta
2. leggere l'header della firma Stripe
3. verificare la firma con STRIPE_WEBHOOK_SECRET
4. se non valida -> rispondere con errore e non elaborare
5. se valida -> elaborare l'evento
```

Regola:

- non fidarsi mai di un webhook non validato

---

## 5. Eventi rilevanti

Eventi Stripe tipici da gestire:

| Evento | Significato | Azione backend |
|---|---|---|
| `checkout.session.completed` | checkout completato | registrare ordine, avviare consegna |
| `payment_intent.succeeded` | pagamento riuscito | conferma stato pagamento |
| `payment_intent.payment_failed` | pagamento fallito | registrare esito negativo |
| `charge.refunded` | rimborso | aggiornare stato ordine |
| `charge.dispute.created` | disputa | segnalare e gestire |

Nota:

- l'evento principale per la conferma d'ordine è tipicamente `checkout.session.completed`
- l'elenco definitivo dipende dalla configurazione Stripe

---

## 6. Ciclo di vita di una transazione

Sequenza logica:

1. l'utente avvia il checkout dal frontend
2. il backend crea la sessione Stripe
3. l'utente paga sul checkout Stripe
4. Stripe elabora pagamento e IVA
5. Stripe invia `checkout.session.completed` al webhook
6. il backend valida l'evento
7. il backend registra l'ordine nel database
8. il backend avvia la consegna del prodotto
9. il backend invia l'email di conferma tramite Resend
10. l'utente vede la pagina di esito sul frontend

---

## 7. Registrazione dell'ordine

Alla ricezione dell'evento valido, il backend:

- crea o aggiorna un documento ordine nel database
- collega l'ordine all'identificativo della sessione Stripe
- registra prodotto, importo, valuta, stato ed email cliente

Campi logici dell'ordine:

```text
order {
  stripe_session_id
  product_sku
  amount
  currency
  status
  customer_email
  created_at
}
```

Riferimento:

- struttura dati in `09-DATABASE`

---

## 8. Idempotenza

Problema:

- Stripe può inviare lo stesso evento più volte

Soluzione:

- il backend deve gestire gli eventi in modo idempotente
- evitare di registrare due volte lo stesso ordine

Approccio:

- usare l'identificativo dell'evento o della sessione come chiave univoca
- verificare se l'ordine è già stato elaborato prima di crearlo

Logica:

```text
se esiste già ordine con stripe_session_id -> non duplicare
altrimenti -> crea ordine
```

---

## 9. Consegna del prodotto

Dopo la registrazione dell'ordine, il backend avvia la consegna dell'Expert Advisor.

Modalità possibili (da definire):

- invio di istruzioni e file tramite email transazionale
- fornitura di un link/area di download
- eventuale gestione licenze

Principi:

- la consegna deve essere affidabile e tracciata
- in caso di errore, prevedere ripetibilità
- rispettare i disclaimer e le condizioni

Nota:

- la modalità definitiva di consegna è una decisione aperta

---

## 10. Gestione degli errori e ripetibilità

Buone pratiche:

- se l'elaborazione fallisce, rispondere in modo che Stripe ripeta l'invio
- registrare gli eventi elaborati e quelli falliti
- prevedere la possibilità di rielaborare manualmente un evento
- non perdere transazioni a causa di errori temporanei

Principio:

- meglio un evento gestito in ritardo che un ordine perso

---

## 11. Risposta corretta ai webhook

Regole di risposta:

- rispondere con successo solo dopo aver elaborato o accettato l'evento in modo sicuro
- rispondere con errore se la validazione fallisce o se l'elaborazione non può completarsi
- evitare tempi di elaborazione eccessivi nella risposta diretta

Principio:

- se l'elaborazione è lunga, accettare l'evento e processarlo in modo asincrono quando possibile

---

## 12. Test dei webhook

Modalità di test:

- usare l'ambiente test di Stripe
- usare gli strumenti Stripe per inviare eventi di test
- verificare che il backend validi e registri correttamente

Verifica funzionale:

- eseguire un acquisto di test
- confermare la ricezione di `checkout.session.completed`
- confermare la registrazione dell'ordine
- confermare l'invio dell'email di conferma

Nota:

- il webhook secret dell'ambiente test è diverso da quello di produzione

---

## 13. Superfici critiche

Punti di attenzione:

- validazione della firma dei webhook
- gestione dell'idempotenza
- affidabilità della consegna del prodotto
- gestione di rimborsi e dispute
- coerenza tra stato Stripe e stato ordine nel database

Mitigazioni:

- validare sempre la firma
- garantire l'idempotenza
- registrare e monitorare gli eventi
- prevedere la rielaborazione manuale

---

## 14. Procedura di ripristino del flusso webhook

Sequenza logica di riferimento:

1. verificare la configurazione dell'endpoint webhook su Stripe
2. verificare che l'URL punti a `api.progettohangar.com/webhooks/stripe`
3. recuperare il webhook secret in modo sicuro
4. aggiornare la variabile `STRIPE_WEBHOOK_SECRET` nel backend
5. inviare un evento di test
6. verificare validazione e registrazione ordine
7. aggiornare stato e changelog

---

## 15. Controlli di verifica

Verifiche consigliate:

```bash
# raggiungibilità endpoint (deve rifiutare richieste non firmate)
curl -I https://api.progettohangar.com/webhooks/stripe
```

Verifiche funzionali:

- evento di test inviato da Stripe ricevuto e validato
- ordine registrato una sola volta (idempotenza)
- email di conferma inviata
- log privi di errori critici

---

## 16. Assunzioni correnti

Assunzioni valide alla stesura:

- i pagamenti passano da Stripe (MoR)
- il backend espone un endpoint webhook dedicato
- la validazione della firma è obbligatoria
- l'evento principale è `checkout.session.completed`
- la modalità di consegna del prodotto è ancora da definire

Se queste assunzioni cambiano, aggiornare il documento.

---

## 17. Attività aperte

Attività da completare:

- confermare l'elenco definitivo degli eventi gestiti
- implementare la validazione della firma
- implementare l'idempotenza
- definire e implementare la consegna del prodotto
- definire la gestione di rimborsi e dispute
- completare i test end-to-end

---

## 18. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione del flusso transazioni e webhook
- incompleto nell'implementazione e nella consegna prodotto
- da aggiornare con lo sviluppo applicativo

Dipendenze correlate:

- `06-BACKEND`
- `09-DATABASE`
- `10-EMAIL`
- `11-STRIPE-MOR`
- `14-SECRETS-INVENTORY`

---

## 19. Changelog

### v0.1
- documentato il ruolo e la sicurezza dei webhook
- descritti eventi, ciclo di vita e registrazione ordine
- definiti idempotenza, consegna, errori e ripristino
- registrate superfici critiche e attività aperte
