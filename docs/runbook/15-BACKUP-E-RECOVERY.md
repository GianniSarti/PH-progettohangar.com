# Progetto Hangar — Backup e Recovery
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento definisce la strategia di backup e le procedure di ripristino (recovery) di **Progetto Hangar**.

Serve a:

- proteggere dati, configurazioni e accessi critici
- garantire la continuità operativa in caso di guasto, errore o perdita di dispositivo
- rendere possibile un disaster recovery ordinato e verificabile
- ridurre la dipendenza dalla memoria dell'operatore
- mettere in sicurezza il progetto prima dell'imminente reinstallazione del Mac

Questo file non contiene segreti in chiaro.  
I valori sensibili sono gestiti secondo il file `14-SECRETS-INVENTORY`.

---

## 2. Obiettivi di backup

Obiettivi principali:

- nessuna perdita di accessi critici
- nessuna perdita di configurazioni difficili da ricostruire
- possibilità di ripristinare il backend su una nuova VPS
- possibilità di ripristinare l'ambiente locale su una nuova macchina
- protezione dei dati applicativi nel database
- ridondanza delle copie in luoghi distinti

---

## 3. Cosa deve essere protetto

Categorie di elementi da includere nei backup.

### 3.1 Accessi e segreti
- chiavi SSH
- password e token
- dati di recupero dei servizi
- file di ambiente del backend

Gestiti tramite: `14-SECRETS-INVENTORY`

### 3.2 Codice e documentazione
- monorepo GitHub
- Runbook
- script operativi

### 3.3 Configurazioni server
- configurazione SSH
- regole UFW
- configurazione fail2ban
- configurazione nginx
- certificati o procedura per riemetterli

### 3.4 Dati applicativi
- database MongoDB Atlas

### 3.5 Configurazioni servizi terzi
- impostazioni Cloudflare (DNS)
- prodotti e configurazione Stripe
- configurazione email (Fastmail, Resend)

### 3.6 Ambiente locale
- chiavi e configurazioni sul Mac
- file `~/.ssh`
- eventuali file di ambiente locali

---

## 4. Classificazione per criticità

### Criticità alta
Perdita = blocco operativo o danno grave:

- chiavi SSH VPS
- file `.env` del backend
- dati DB MongoDB
- accessi ai provider critici (Cloudflare, Stripe, GitHub, MongoDB Atlas)

### Criticità media
Perdita = disagio significativo ma recuperabile:

- configurazioni nginx / firewall / fail2ban
- configurazioni email
- documentazione operativa non versionata

### Criticità bassa
Perdita = ricostruibile con sforzo limitato:

- elementi rigenerabili
- valori DNS pubblici documentabili nuovamente

---

## 5. Principi di backup adottati

Principi:

- regola di ridondanza: più copie
- copie in luoghi distinti
- cifratura dei dati sensibili
- verifica periodica della recuperabilità
- documentazione della posizione dei backup
- separazione tra dati sensibili e dati ordinari

Interpretazione pratica ispirata alla regola 3-2-1:

- almeno 3 copie dei dati critici
- su almeno 2 supporti diversi
- con almeno 1 copia esterna/offline

---

## 6. Strategia per categoria

### 6.1 Chiavi SSH e segreti
Strategia:

- salvare secondo `14-SECRETS-INVENTORY`
- copie ridondanti cifrate
- test di ripristino sui segreti ad alta priorità

Riferimento operativo pratico:

- vedi checklist backup chiavi SSH già predisposta

---

### 6.2 Codice e Runbook
Strategia:

- il monorepo su GitHub è la fonte primaria versionata
- mantenere una copia locale sana in almeno un dispositivo
- opzionale: copia periodica compressa del repository in archivio sicuro

Copia locale compressa del repository (esempio):

```bash
git bundle create progetto-hangar-backup.bundle --all
```

Nota:

- il bundle non deve contenere file di ambiente o segreti
- verificare che `.gitignore` escluda i file sensibili

---

### 6.3 Configurazioni server
Strategia:

- salvare copie delle configurazioni chiave della VPS
- conservarle in archivio sicuro fuori dal server

File tipici da salvare:

```text
/etc/ssh/sshd_config
/etc/nginx/ (configurazioni dei siti)
/etc/ufw/ (regole firewall)
/etc/fail2ban/ (configurazioni personalizzate)
```

Esempio di raccolta configurazioni in un archivio (da eseguire con cautela e senza includere segreti non necessari):

```bash
sudo tar -czf /tmp/config-backup.tar.gz \
  /etc/ssh/sshd_config \
  /etc/nginx \
  /etc/ufw \
  /etc/fail2ban
```

Poi trasferire l'archivio in luogo sicuro tramite SSH:

```bash
scp -P 134 pilota@<IP_O_HOST_VPS>:/tmp/config-backup.tar.gz ./
```

Nota:

- rimuovere l'archivio temporaneo dal server dopo il trasferimento
- conservare l'archivio in luogo cifrato

---

### 6.4 Database MongoDB Atlas
Strategia:

- sfruttare le funzionalità di backup del servizio gestito, se disponibili sul piano
- eseguire periodicamente un export applicativo dei dati critici
- conservare gli export in luogo sicuro

Export logico dei dati (esempio con strumenti MongoDB):

```bash
mongodump --uri "<MONGODB_URI_SICURO>" --out ./backup-mongo-$(date +%F)
```

Ripristino (esempio):

```bash
mongorestore --uri "<MONGODB_URI_SICURO>" ./backup-mongo-<DATA>
```

Note:

- non salvare l'URI in chiaro nella documentazione
- valutare i limiti del piano M0 gratuito rispetto ai backup automatici
- man mano che crescono i dati (ordini, licenze), aumentare la frequenza degli export

---

### 6.5 Configurazioni servizi terzi
Strategia:

- documentare la configurazione in modo ricostruibile nei rispettivi capitoli
- annotare i valori DNS in `03-DNS-E-DOMINI`
- annotare prodotti e SKU Stripe in `18-PRODOTTI-E-SKU`
- annotare configurazioni email in `10-EMAIL`

Principio:

- per i servizi gestiti, la miglior forma di backup è la documentazione precisa e aggiornata della configurazione

---

### 6.6 Ambiente locale (Mac)
Strategia prioritaria vista l'imminente reinstallazione:

- backup completo di `~/.ssh`
- backup dei file di ambiente locali
- salvataggio dei segreti nel password manager e in archivio cifrato
- verifica che tutto sia recuperabile prima di procedere al reinstall

Riferimento:

- checklist backup chiavi SSH già predisposta
- inventario segreti `14-SECRETS-INVENTORY`

---

## 7. Frequenza dei backup

Linee guida iniziali.

| Elemento | Frequenza consigliata | Note |
|---|---|---|
| Chiavi SSH e segreti | ad ogni modifica | e prima di reinstall |
| Codice / Runbook | continuo via Git | push regolari |
| Config server | ad ogni modifica rilevante | dopo hardening o cambi nginx |
| Database | periodico | aumentare con crescita dati |
| Config servizi terzi | ad ogni modifica | tramite documentazione |
| Ambiente locale | prima di reinstall + periodico | priorità attuale alta |

---

## 8. Dove conservare i backup

Luoghi raccomandati:

- password manager per i segreti
- archivio cifrato offline
- supporto esterno cifrato dedicato
- GitHub come fonte primaria del codice

Requisiti:

- ridondanza in luoghi distinti
- cifratura per tutto ciò che è sensibile
- posizione documentata (senza esporre contenuti sensibili)

Regola:

- nessun backup critico deve esistere in una sola copia

---

## 9. Procedura di disaster recovery

Sequenza logica di riferimento per un ripristino completo.

### 9.1 Ripristino ambiente locale
1. reinstallare/preparare la macchina
2. ripristinare `~/.ssh` dal backup
3. correggere i permessi delle chiavi
4. recuperare i segreti dal password manager/archivio cifrato
5. clonare il monorepo da GitHub
6. verificare l'accesso ai servizi critici

Permessi chiavi dopo ripristino:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/config
```

### 9.2 Ripristino backend / VPS
1. seguire la procedura di ricostruzione in `04-VPS-E-HARDENING`
2. ripristinare le configurazioni server dai backup
3. ripristinare il file `.env` del backend dal luogo sicuro
4. riavviare i servizi
5. riemettere/ripristinare i certificati HTTPS
6. verificare la raggiungibilità dell'API

### 9.3 Ripristino dati
1. recuperare l'URI del database in modo sicuro
2. ripristinare i dati con `mongorestore` se necessario
3. verificare integrità e coerenza dei dati

### 9.4 Verifica finale
1. testare sito, API, pagamenti ed email
2. aggiornare stato e date nei documenti
3. aggiornare il changelog

---

## 10. Test di ripristino

Principio:

- un backup non testato non è un backup affidabile

Test consigliati:

- test periodico di accesso SSH dopo ripristino chiavi
- test di clonazione del repository
- test di recupero di almeno un segreto ad alta priorità
- test occasionale di restore parziale del database

Registrazione:

- annotare esito e data dei test nella tabella di stato

---

## 11. Registro dei backup

Tabella da mantenere aggiornata.

| Elemento | Ultimo backup | Luogo | Verificato | Data verifica | Note |
|---|---|---|---|---|---|
| Chiavi SSH | `<DATA>` | `<DA_COMPILARE>` | `<SI/NO>` | `<DATA>` | |
| Segreti | `<DATA>` | `<DA_COMPILARE>` | `<SI/NO>` | `<DATA>` | |
| `.env` backend | `<DATA>` | `<DA_COMPILARE>` | `<SI/NO>` | `<DATA>` | |
| Config server | `<DATA>` | `<DA_COMPILARE>` | `<SI/NO>` | `<DATA>` | |
| Database | `<DATA>` | `<DA_COMPILARE>` | `<SI/NO>` | `<DATA>` | |
| Repository | `<DATA>` | GitHub + locale | `<SI/NO>` | `<DATA>` | |

---

## 12. Superfici critiche di backup

Punti sensibili:

- unica copia locale non ridondata
- backup non cifrati
- backup mai testati
- segreti inclusi per errore in copie non sicure
- assenza di copia esterna/offline

Attenzioni:

- ogni backup contenente segreti va cifrato
- ogni categoria critica deve avere almeno una copia esterna
- ogni backup deve avere una data e una verifica

---

## 13. Assunzioni correnti

Assunzioni valide alla stesura:

- esiste un solo ambiente di produzione
- il repository primario è su GitHub
- il database è su piano gestito con eventuali limiti di backup automatico
- l'operatore reinstallerà a breve la workstation
- i segreti sono gestiti secondo `14-SECRETS-INVENTORY`

Se queste assunzioni cambiano, aggiornare il documento.

---

## 14. Attività aperte

Attività da completare:

- eseguire e verificare il backup dell'ambiente locale prima del reinstall
- compilare il registro dei backup
- definire la frequenza definitiva degli export del database
- verificare le opzioni di backup disponibili sul piano MongoDB Atlas
- eseguire un primo test di ripristino end-to-end
- salvare le configurazioni server in archivio sicuro

---

## 15. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come strategia di backup e recovery
- incompleto finché non compilati registro e verifiche
- prioritario da attuare prima della reinstallazione del Mac

Dipendenze correlate:

- `04-VPS-E-HARDENING`
- `06-BACKEND`
- `08-NGINX-E-HTTPS`
- `09-DATABASE`
- `14-SECRETS-INVENTORY`

---

## 16. Changelog

### v0.1
- definita la strategia di backup e recovery
- classificati gli elementi per criticità
- definite strategie per categoria e frequenze
- descritta la procedura di disaster recovery
- creati registro dei backup e attività aperte
