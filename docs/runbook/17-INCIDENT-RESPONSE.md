# Progetto Hangar — Incident Response
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento definisce come reagire agli incidenti di **Progetto Hangar**: guasti, downtime, compromissioni di sicurezza e perdita di accessi.

Serve a:

- fornire procedure chiare in situazioni di emergenza
- ridurre i tempi di reazione e i danni
- garantire un recupero ordinato
- evitare decisioni improvvisate sotto stress
- permettere a un operatore o a una IA di rispondere in modo strutturato

Questo file non contiene segreti.

---

## 2. Principi di risposta agli incidenti

Principi guida:

- prima contenere, poi risolvere, poi documentare
- non peggiorare la situazione con azioni affrettate
- privilegiare la sicurezza dei dati e degli accessi
- ripristinare da fonti affidabili (backup, documentazione)
- registrare sempre cosa è successo e come è stato risolto

---

## 3. Classificazione degli incidenti

| Livello | Descrizione | Esempi |
|---|---|---|
| Basso | impatto limitato, nessun rischio dati | errore minore, lentezza temporanea |
| Medio | servizio degradato o parziale downtime | API instabile, email non inviate |
| Alto | downtime significativo o rischio dati | backend down, database irraggiungibile |
| Critico | compromissione di sicurezza o perdita dati/accessi | intrusione, chiavi compromesse, dati persi |

Principio:

- il livello determina la priorità e la velocità di risposta

---

## 4. Flusso generale di risposta

Sequenza standard:

1. **Rilevazione**: identificare il problema
2. **Valutazione**: classificare il livello e l'impatto
3. **Contenimento**: limitare i danni
4. **Risoluzione**: ripristinare il servizio
5. **Verifica**: confermare il ritorno alla normalità
6. **Documentazione**: registrare l'incidente e le lezioni apprese

---

## 5. Scenario: downtime del sito (frontend)

Sintomi:

- il sito pubblico non è raggiungibile

Azioni:

1. verificare lo stato di Cloudflare Pages
2. verificare la configurazione DNS in Cloudflare
3. verificare l'ultimo deploy del frontend
4. se causato da un deploy, eseguire rollback a una versione precedente
5. verificare la raggiungibilità dopo l'intervento

Riferimenti:

- `05-FRONTEND`, `07-DEPLOYMENT`, `03-DNS-E-DOMINI`

---

## 6. Scenario: downtime dell'API (backend)

Sintomi:

- `api.progettohangar.com` non risponde o restituisce errori

Azioni:

1. accedere alla VPS via SSH
2. verificare lo stato del servizio backend

```bash
sudo systemctl status <nome-servizio>
```

3. verificare lo stato di nginx

```bash
sudo systemctl status nginx
sudo nginx -t
```

4. controllare i log recenti

```bash
sudo journalctl -u <nome-servizio> -e
```

5. riavviare il servizio se necessario

```bash
sudo systemctl restart <nome-servizio>
```

6. verificare la raggiungibilità

```bash
curl -I https://api.progettohangar.com/health
```

Riferimenti:

- `06-BACKEND`, `08-NGINX-E-HTTPS`

---

## 7. Scenario: certificato HTTPS scaduto

Sintomi:

- errori di sicurezza sul dominio API

Azioni:

1. verificare lo stato dei certificati

```bash
sudo certbot certificates
```

2. tentare il rinnovo

```bash
sudo certbot renew
```

3. ricaricare nginx

```bash
sudo systemctl reload nginx
```

4. verificare HTTPS

Riferimento:

- `08-NGINX-E-HTTPS`

---

## 8. Scenario: database irraggiungibile

Sintomi:

- il backend non riesce a connettersi al database

Azioni:

1. verificare lo stato del cluster su MongoDB Atlas
2. verificare l'allowlist IP (l'IP della VPS deve essere autorizzato)
3. verificare la validità dell'URI di connessione
4. verificare eventuali limiti raggiunti del piano
5. ripristinare la connettività e testare

Riferimento:

- `09-DATABASE`

---

## 9. Scenario: pagamenti non funzionanti

Sintomi:

- checkout non parte o ordini non registrati

Azioni:

1. verificare lo stato di Stripe
2. verificare le chiavi Stripe nel backend
3. verificare la configurazione e la ricezione dei webhook
4. controllare i log del backend per errori di pagamento
5. eseguire un acquisto di test

Riferimenti:

- `11-STRIPE-MOR`, `12-TRANSAZIONI-E-WEBHOOK`

---

## 10. Scenario: email non inviate

Sintomi:

- le email transazionali non arrivano

Azioni:

1. verificare lo stato di Resend
2. verificare l'API key nel backend
3. verificare i record DNS di autenticazione email
4. controllare i log di invio
5. inviare un'email di test

Riferimento:

- `10-EMAIL`

---

## 11. Scenario: compromissione di sicurezza

Sintomi:

- accessi non autorizzati, comportamenti anomali, segreti esposti

Azioni immediate (contenimento):

1. valutare l'isolamento del servizio interessato
2. revocare o ruotare immediatamente i segreti coinvolti
3. cambiare le credenziali degli account interessati
4. verificare gli accessi recenti e i log

Azioni successive:

5. identificare la causa e il punto di ingresso
6. applicare le correzioni necessarie
7. ripristinare da backup puliti se necessario
8. ripristinare i segreti in modo sicuro
9. documentare l'incidente in dettaglio

Riferimenti:

- `13-ACCESSI-E-IDENTITA`, `14-SECRETS-INVENTORY`

---

## 12. Scenario: segreto esposto nel repository

Sintomi:

- una chiave o un token è finito nel codice versionato

Azioni:

1. considerare il segreto compromesso
2. ruotare/revocare immediatamente il segreto
3. aggiornare il segreto nei sistemi che lo usano
4. rimuovere il segreto dal repository
5. verificare la cronologia del repository
6. aggiornare `14-SECRETS-INVENTORY`

Principio:

- un segreto esposto va sempre ruotato, non solo rimosso

---

## 13. Scenario: perdita di accesso / dispositivo

Sintomi:

- perdita del Mac, blocco di un account critico

Azioni:

1. usare i backup e il password manager per ripristinare gli accessi
2. usare i recovery code dei servizi con 2FA
3. seguire la procedura di ripristino accessi
4. verificare che nessun accesso sia stato compromesso
5. aggiornare la mappa accessi

Riferimenti:

- `13-ACCESSI-E-IDENTITA`, `15-BACKUP-E-RECOVERY`

---

## 14. Registro degli incidenti

Ogni incidente va documentato.

Modello di voce:

```text
incidente {
  data
  livello
  descrizione
  sistemi coinvolti
  azioni di contenimento
  azioni di risoluzione
  causa
  lezioni apprese
  stato
}
```

Principio:

- il registro serve a migliorare la resilienza nel tempo
- ogni incidente critico deve produrre almeno un miglioramento

---

## 15. Superfici critiche

Punti di attenzione:

- assenza di procedure porta a reazioni improvvisate
- backup non testati inutili in emergenza
- recovery code mancanti bloccano il ripristino
- segreti non ruotati dopo un incidente
- mancata documentazione degli incidenti

Mitigazioni:

- mantenere queste procedure aggiornate
- testare periodicamente backup e ripristini
- conservare con cura i recovery data
- documentare sempre gli incidenti

---

## 16. Assunzioni correnti

Assunzioni valide alla stesura:

- unico operatore responsabile della risposta
- backup e segreti gestiti secondo i capitoli dedicati
- un solo ambiente di produzione
- nessun sistema di alert automatico attivo

Se queste assunzioni cambiano, aggiornare il documento.

---

## 17. Attività aperte

Attività da completare:

- creare un registro incidenti operativo
- testare almeno uno scenario di ripristino
- verificare la disponibilità dei recovery code
- valutare alert automatici per rilevazione più rapida

---

## 18. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come guida di risposta agli incidenti
- da arricchire con l'esperienza reale
- da aggiornare dopo ogni incidente significativo

Dipendenze correlate:

- `04-VPS-E-HARDENING`
- `06-BACKEND`
- `08-NGINX-E-HTTPS`
- `09-DATABASE`
- `11-STRIPE-MOR`
- `12-TRANSAZIONI-E-WEBHOOK`
- `13-ACCESSI-E-IDENTITA`
- `14-SECRETS-INVENTORY`
- `15-BACKUP-E-RECOVERY`

---

## 19. Changelog

### v0.1
- definiti principi e classificazione degli incidenti
- descritti scenari operativi e relative procedure
- definiti registro incidenti e superfici critiche
- registrate attività aperte
