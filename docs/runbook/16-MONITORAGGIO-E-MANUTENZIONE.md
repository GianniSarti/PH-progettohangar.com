# Progetto Hangar — Monitoraggio e Manutenzione
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive le attività di monitoraggio e manutenzione ordinaria di **Progetto Hangar**.

Serve a:

- garantire che i servizi restino operativi e sicuri
- definire controlli periodici e loro frequenza
- prevenire problemi prima che diventino critici
- fornire una routine ripetibile di manutenzione
- permettere a un operatore o a una IA di mantenere il sistema in salute

Questo file non contiene segreti.

---

## 2. Obiettivi di monitoraggio

Obiettivi principali:

- verificare la disponibilità del sito e dell'API
- verificare lo stato dei servizi sulla VPS
- monitorare sicurezza e accessi
- monitorare scadenze (certificati, backup)
- monitorare l'uso delle risorse rispetto ai limiti dei piani

---

## 3. Elementi da monitorare

| Elemento | Cosa verificare | Frequenza |
|---|---|---|
| Sito pubblico | raggiungibilità e caricamento | frequente |
| API backend | health check | frequente |
| Servizio backend | stato del servizio di sistema | periodico |
| nginx | stato e validità configurazione | periodico |
| Certificati HTTPS | validità e scadenza | periodico |
| Firewall UFW | regole attive | periodico |
| fail2ban | tentativi e ban | periodico |
| Database | connettività e spazio usato | periodico |
| Backup | esecuzione e verifica | periodico |
| Log | errori e anomalie | periodico |

---

## 4. Controlli di disponibilità

Verifiche di base di disponibilità.

Sito e API:

```bash
# sito pubblico
curl -I https://progettohangar.com

# health API
curl -I https://api.progettohangar.com/health
```

Esito atteso:

- risposte positive
- tempi di risposta ragionevoli

---

## 5. Controlli dei servizi sulla VPS

Stato dei servizi principali:

```bash
sudo systemctl status <nome-servizio-backend>
sudo systemctl status nginx
sudo systemctl status fail2ban
```

Esito atteso:

- tutti i servizi attivi e in esecuzione

---

## 6. Controlli di sicurezza

Firewall:

```bash
sudo ufw status verbose
```

fail2ban:

```bash
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

Log di accesso e sistema:

```bash
sudo journalctl -e
```

Cosa osservare:

- tentativi di accesso sospetti
- ban attivi anomali
- errori ricorrenti

---

## 7. Controllo dei certificati HTTPS

Verifica dei certificati:

```bash
sudo certbot certificates
```

Verifica del rinnovo automatico:

```bash
sudo certbot renew --dry-run
```

Cosa osservare:

- certificati validi
- scadenza non imminente
- rinnovo automatico funzionante

Riferimento:

- `08-NGINX-E-HTTPS`

---

## 8. Controllo del database

Verifiche:

- connettività dal backend
- spazio utilizzato rispetto ai limiti del piano M0
- stato del cluster nella console MongoDB Atlas

Ping di connettività (se disponibile client):

```bash
mongosh "<MONGODB_URI_SICURO>" --eval "db.runCommand({ ping: 1 })"
```

Cosa osservare:

- connessione stabile
- spazio non prossimo al limite
- assenza di errori nel cluster

Riferimento:

- `09-DATABASE`

---

## 9. Controllo dei backup

Verifiche periodiche:

- i backup vengono eseguiti secondo la strategia
- i backup sono verificati e recuperabili
- il registro dei backup è aggiornato

Riferimento:

- `15-BACKUP-E-RECOVERY`

Cosa osservare:

- date di ultimo backup aggiornate
- almeno un test di ripristino recente

---

## 10. Manutenzione del sistema operativo

Aggiornamenti periodici della VPS:

```bash
sudo apt update
sudo apt upgrade
```

Dopo aggiornamenti rilevanti:

- verificare che backend e nginx funzionino
- verificare la raggiungibilità dell'API
- controllare i log per eventuali errori

Principio:

- applicare aggiornamenti di sicurezza con regolarità
- pianificare gli aggiornamenti importanti in momenti controllati

---

## 11. Manutenzione applicativa

Attività periodiche lato applicazione:

- aggiornare le dipendenze quando necessario
- verificare la coerenza tra catalogo Stripe e applicativo
- verificare il funzionamento del flusso di acquisto
- verificare l'invio delle email transazionali
- controllare i log applicativi per errori ricorrenti

---

## 12. Calendario di manutenzione consigliato

| Frequenza | Attività |
|---|---|
| Frequente | health check sito e API |
| Settimanale | stato servizi, log, sicurezza |
| Mensile | certificati, backup, aggiornamenti sistema |
| Periodico | test di ripristino, revisione accessi e token |
| Ad evento | dopo ogni deploy o modifica infrastrutturale |

Nota:

- adattare la frequenza alla crescita reale del progetto

---

## 13. Monitoraggio automatico (opzionale futuro)

Possibili evoluzioni:

- monitoraggio esterno di uptime del sito e dell'API
- avvisi automatici in caso di downtime
- alert sulla scadenza dei certificati
- alert sull'uso delle risorse del database

Stato:

- non implementati
- da valutare con la crescita del progetto

Principio:

- introdurre monitoraggio automatico quando riduce concretamente il rischio

---

## 14. Superfici critiche

Punti di attenzione:

- certificati scaduti non rilevati
- backup non eseguiti o non verificati
- servizi caduti senza accorgersene
- spazio database esaurito
- tentativi di intrusione non monitorati

Mitigazioni:

- routine di controllo periodica
- verifica delle scadenze
- eventuale monitoraggio automatico futuro

---

## 15. Assunzioni correnti

Assunzioni valide alla stesura:

- monitoraggio prevalentemente manuale in questa fase
- unico operatore responsabile
- risorse su piani iniziali con limiti da sorvegliare
- nessun sistema di alert automatico attivo

Se queste assunzioni cambiano, aggiornare il documento.

---

## 16. Attività aperte

Attività da completare:

- definire un calendario di manutenzione concreto
- valutare un monitoraggio esterno di uptime
- impostare promemoria per scadenze certificati e backup
- consolidare i controlli applicativi post-deploy

---

## 17. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come routine di monitoraggio e manutenzione
- da arricchire con eventuali strumenti automatici
- da aggiornare con la crescita del progetto

Dipendenze correlate:

- `04-VPS-E-HARDENING`
- `06-BACKEND`
- `08-NGINX-E-HTTPS`
- `09-DATABASE`
- `15-BACKUP-E-RECOVERY`
- `17-INCIDENT-RESPONSE`

---

## 18. Changelog

### v0.1
- definiti elementi, controlli e frequenze di monitoraggio
- descritte manutenzione di sistema e applicativa
- proposto calendario di manutenzione
- registrate superfici critiche e attività aperte
