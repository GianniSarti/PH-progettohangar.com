# Progetto Hangar — Email
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la gestione delle email di **Progetto Hangar**: posta di dominio e email transazionali.

Serve a:

- documentare i provider email e i loro ruoli
- chiarire la configurazione DNS necessaria per l'email
- descrivere l'invio transazionale dal backend
- garantire deliverability e sicurezza del dominio
- permettere a un operatore o a una IA di intervenire senza inferenze

Questo file non contiene segreti.  
API key e credenziali email sono gestite secondo `14-SECRETS-INVENTORY`.

---

## 2. Architettura email

Il progetto separa due funzioni distinte.

- **Posta di dominio (Fastmail)**: caselle operative e comunicazioni manuali
- **Email transazionali (Resend)**: email automatiche generate dal backend

Principio:

- separare la posta umana dalle email applicative
- ridurre confusione operativa e migliorare la gestione della deliverability

---

## 3. Posta di dominio (Fastmail)

Provider:

- Fastmail

Ruolo:

- caselle email del dominio
- comunicazioni amministrative e di business
- corrispondenza manuale con clienti o partner

Esempi di caselle tipiche (da definire):

```text
info@progettohangar.com
support@progettohangar.com
gianni@progettohangar.com
```

Configurazione:

- record MX verso Fastmail
- record di autenticazione secondo le indicazioni ufficiali di Fastmail
- vedi `03-DNS-E-DOMINI` per la mappa dei record

---

## 4. Email transazionali (Resend)

Provider:

- Resend

Ruolo:

- invio email automatiche applicative
- conferme d'ordine
- notifiche di consegna prodotto
- eventuali comunicazioni post-acquisto

Principio:

- inviate dal backend tramite API
- inviate da un sottodominio dedicato per non interferire con la posta principale

---

## 5. Sottodominio di invio transazionale

Approccio consigliato:

- usare un sottodominio dedicato per l'invio transazionale

Esempio logico:

```text
mail.progettohangar.com
```

Motivazioni:

- separare la reputazione di invio transazionale dalla posta di dominio
- gestione più pulita dei record di autenticazione
- maggiore controllo sulla deliverability

Nota:

- il nome esatto del sottodominio va deciso e documentato
- i record vanno configurati secondo le indicazioni di Resend

---

## 6. Autenticazione email e deliverability

Meccanismi di autenticazione da configurare:

- SPF: autorizza i server di invio
- DKIM: firma crittografica dei messaggi
- DMARC: politica di gestione dei messaggi non autenticati

Principi:

- configurare correttamente SPF e DKIM per entrambi i flussi (Fastmail e Resend)
- introdurre DMARC per proteggere il dominio da abusi
- verificare periodicamente la validità dei record

Nota:

- i valori esatti dei record provengono dai provider
- non inventare valori: usare quelli forniti da Fastmail e Resend
- documentare i record in `03-DNS-E-DOMINI`

---

## 7. Integrazione email nel backend

Il backend invia email transazionali tramite Resend.

Configurazione:

- API key gestita come variabile di ambiente (`RESEND_API_KEY`)
- mittente configurato sul sottodominio dedicato
- template dei messaggi gestiti a livello applicativo

Variabile logica:

```text
RESEND_API_KEY=<SEGRETO>
EMAIL_FROM=no-reply@mail.progettohangar.com
```

Principi:

- non esporre l'API key
- gestire errori di invio in modo robusto
- non registrare contenuti sensibili nei log

---

## 8. Tipologie di email transazionali previste

Email applicative attese:

| Tipo | Trigger | Contenuto | Note |
|---|---|---|---|
| Conferma d'ordine | pagamento completato | riepilogo acquisto | collegata a webhook Stripe |
| Consegna prodotto | ordine confermato | istruzioni/accesso EA | modalità da definire |
| Notifica di supporto | richiesta cliente | risposta/inoltro | opzionale |

Nota:

- il flusso preciso è collegato agli eventi di pagamento (`12-TRANSAZIONI-E-WEBHOOK`)
- i contenuti devono rispettare i disclaimer (`19-DISCLAIMER-E-COMPLIANCE`)

---

## 9. Verifica configurazione email

Verifiche DNS dei record email:

```bash
# record MX (posta di dominio)
dig progettohangar.com MX +short

# record SPF (esempio)
dig progettohangar.com TXT +short

# record DKIM (nome fornito dal provider)
dig <SELECTOR>._domainkey.<DOMINIO> TXT +short

# record DMARC
dig _dmarc.progettohangar.com TXT +short
```

Verifiche funzionali:

- inviare email di test dal backend tramite Resend
- verificare ricezione e corretta autenticazione
- controllare che i messaggi non finiscano in spam

---

## 10. Superfici critiche email

Punti di attenzione:

- API key Resend
- record di autenticazione errati o mancanti
- reputazione del dominio compromessa
- email transazionali che finiscono in spam
- esposizione di dati sensibili nei contenuti o nei log

Mitigazioni:

- conservare l'API key in modo sicuro
- configurare correttamente SPF, DKIM e DMARC
- usare sottodominio dedicato per l'invio
- monitorare la deliverability

---

## 11. Procedura di ripristino email

Sequenza logica di riferimento:

1. verificare l'accesso agli account Fastmail e Resend
2. verificare i record DNS email in Cloudflare
3. recuperare l'API key Resend in modo sicuro
4. aggiornare la variabile di ambiente del backend
5. inviare email di test transazionale
6. verificare autenticazione e deliverability
7. aggiornare stato e changelog

---

## 12. Assunzioni correnti

Assunzioni valide alla stesura:

- posta di dominio su Fastmail
- email transazionali su Resend
- invio transazionale da sottodominio dedicato
- backend integra Resend via API key
- record DNS gestiti su Cloudflare

Se queste assunzioni cambiano, aggiornare il documento.

---

## 13. Attività aperte

Attività da completare:

- definire le caselle email di dominio
- decidere e documentare il sottodominio di invio
- configurare e verificare SPF, DKIM e DMARC
- integrare l'invio transazionale nel backend
- definire i template delle email
- eseguire test di deliverability

---

## 14. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione dell'architettura email
- incompleto nella configurazione puntuale dei record e dei template
- da aggiornare con l'implementazione reale

Dipendenze correlate:

- `03-DNS-E-DOMINI`
- `06-BACKEND`
- `12-TRANSAZIONI-E-WEBHOOK`
- `14-SECRETS-INVENTORY`
- `19-DISCLAIMER-E-COMPLIANCE`

---

## 15. Changelog

### v0.1
- documentata l'architettura email a due flussi
- descritti posta di dominio e email transazionali
- definiti autenticazione, integrazione backend e verifiche
- registrate superfici critiche e attività aperte
