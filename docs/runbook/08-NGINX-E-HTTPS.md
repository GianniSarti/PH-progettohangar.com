# Progetto Hangar — nginx e HTTPS
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la configurazione di nginx e della sicurezza HTTPS sulla VPS di **Progetto Hangar**.

Serve a:

- documentare il ruolo di nginx come reverse proxy
- descrivere la terminazione TLS per `api.progettohangar.com`
- fornire una base ricostruibile della configurazione web
- permettere un ripristino ordinato del layer di ingresso pubblico
- consentire a un operatore o a una IA di intervenire senza inferenze

Questo file non contiene segreti.  
Chiavi private dei certificati e dati sensibili non vanno inseriti qui.

---

## 2. Ruolo di nginx

nginx è il punto di ingresso pubblico del backend.

Responsabilità principali:

- ricevere il traffico HTTP/HTTPS
- terminare la connessione TLS
- inoltrare le richieste al backend FastAPI in ascolto su localhost
- gestire redirect da HTTP a HTTPS
- fungere da primo filtro dell'esposizione pubblica

Principio:

- il backend non è esposto direttamente
- tutto il traffico pubblico passa da nginx

---

## 3. Dominio servito

Dominio gestito da nginx:

- `api.progettohangar.com`

Stato:

- attivo
- servito in HTTPS

Relazione con il DNS:

- il record `api` punta alla VPS secondo quanto documentato in `03-DNS-E-DOMINI`

---

## 4. Architettura del reverse proxy

Flusso logico:

1. il client invia una richiesta HTTPS a `api.progettohangar.com`
2. nginx riceve la richiesta sulla porta `443`
3. nginx termina il TLS
4. nginx inoltra la richiesta al backend su `127.0.0.1:8000`
5. il backend elabora e risponde
6. nginx restituisce la risposta al client

Le richieste su porta `80` vengono reindirizzate a HTTPS.

---

## 5. Configurazione del virtual host

Percorso tipico delle configurazioni dei siti:

```text
/etc/nginx/sites-available/
/etc/nginx/sites-enabled/
```

Esempio logico di configurazione (da allineare alla configurazione reale sul server):

```text
# Redirect HTTP -> HTTPS
server {
    listen 80;
    server_name api.progettohangar.com;
    return 301 https://$host$request_uri;
}

# HTTPS reverse proxy
server {
    listen 443 ssl;
    server_name api.progettohangar.com;

    ssl_certificate     /etc/letsencrypt/live/api.progettohangar.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/api.progettohangar.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Note:

- i percorsi dei certificati dipendono dal metodo di emissione reale
- i valori effettivi vanno verificati sul server
- la configurazione reale va inclusa nei backup

---

## 6. Certificati HTTPS

Approccio tipico:

- certificati TLS emessi tramite Let's Encrypt
- rinnovo automatico gestito dal client di certificazione

Nota:

- se il record DNS del backend è in modalità proxy Cloudflare, valutare l'impatto sull'emissione e sul rinnovo dei certificati
- la strategia TLS deve essere coerente tra Cloudflare e nginx

Riferimento:

- vedere considerazioni su proxy in `03-DNS-E-DOMINI`

---

## 7. Gestione dei certificati

Strumento tipico:

- certbot (client Let's Encrypt)

Comandi indicativi (da verificare rispetto all'installazione reale):

```bash
# elenco certificati
sudo certbot certificates

# test del rinnovo
sudo certbot renew --dry-run
```

Note:

- il rinnovo automatico va verificato periodicamente
- dopo il rinnovo, nginx deve ricaricare la configurazione
- includere la procedura di riemissione nella strategia di recovery

---

## 8. Comandi operativi nginx

Verifica della configurazione prima di applicare modifiche:

```bash
sudo nginx -t
```

Ricarica senza interruzione:

```bash
sudo systemctl reload nginx
```

Riavvio completo:

```bash
sudo systemctl restart nginx
```

Stato del servizio:

```bash
sudo systemctl status nginx
```

Principio:

- verificare sempre con `nginx -t` prima di ricaricare
- preferire `reload` a `restart` per modifiche non invasive

---

## 9. Sicurezza del layer web

Buone pratiche:

- reindirizzare sempre HTTP a HTTPS
- non esporre il backend direttamente su porte pubbliche
- limitare le informazioni rivelate nelle intestazioni
- mantenere nginx aggiornato
- considerare intestazioni di sicurezza appropriate

Intestazioni di sicurezza indicative (da valutare):

```text
add_header X-Content-Type-Options nosniff;
add_header X-Frame-Options SAMEORIGIN;
add_header Referrer-Policy strict-origin-when-cross-origin;
```

Nota:

- valutare l'introduzione graduale delle intestazioni di sicurezza
- testare che non interferiscano con il funzionamento legittimo

---

## 10. Relazione con firewall e backend

Coordinamento con gli altri layer:

- UFW deve consentire le porte `80` e `443` (vedi `04-VPS-E-HARDENING`)
- il backend deve essere in ascolto su `127.0.0.1:8000` (vedi `06-BACKEND`)
- nginx collega il traffico pubblico al backend interno

Verifica coerenza:

```bash
# firewall
sudo ufw status verbose

# backend locale
curl -I http://127.0.0.1:8000/health

# ingresso pubblico
curl -I https://api.progettohangar.com/health
```

---

## 11. Superfici critiche

Punti di attenzione:

- errore di configurazione che blocca il servizio
- certificati scaduti o non rinnovati
- disallineamento tra proxy Cloudflare e TLS nginx
- esposizione involontaria di informazioni
- backend raggiungibile pubblicamente bypassando nginx

Mitigazioni:

- verificare sempre la configurazione prima di ricaricare
- monitorare la scadenza dei certificati
- mantenere coerente la strategia TLS
- assicurarsi che il backend ascolti solo su localhost

---

## 12. Procedura di ripristino del layer web

Sequenza logica di riferimento:

1. installare nginx sulla VPS
2. ripristinare la configurazione del virtual host dai backup
3. ripristinare o riemettere i certificati TLS
4. verificare la configurazione con `nginx -t`
5. avviare/ricaricare nginx
6. verificare il redirect HTTP verso HTTPS
7. verificare la raggiungibilità pubblica dell'API
8. aggiornare stato e changelog

---

## 13. Controlli di verifica

Verifiche post-configurazione o post-ripristino:

```bash
# test configurazione
sudo nginx -t

# stato servizio
sudo systemctl status nginx

# redirect HTTP
curl -I http://api.progettohangar.com

# HTTPS applicativo
curl -I https://api.progettohangar.com/health

# certificati
sudo certbot certificates
```

Esito atteso:

- configurazione valida
- nginx attivo
- HTTP reindirizzato a HTTPS
- HTTPS funzionante verso il backend
- certificati validi e non prossimi alla scadenza

---

## 14. Assunzioni correnti

Assunzioni valide alla stesura:

- nginx gestisce l'ingresso pubblico del backend
- il dominio servito è `api.progettohangar.com`
- il backend ascolta su `127.0.0.1:8000`
- i certificati sono gestiti tramite Let's Encrypt
- esiste un solo ambiente di produzione

Se queste assunzioni cambiano, aggiornare il documento.

---

## 15. Attività aperte

Attività da completare:

- allineare l'esempio di configurazione alla configurazione reale
- confermare i percorsi effettivi dei certificati
- verificare la coerenza TLS con l'eventuale proxy Cloudflare
- valutare l'introduzione delle intestazioni di sicurezza
- includere la configurazione nginx nei backup

---

## 16. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione del layer web e HTTPS
- incompleto nei valori puntuali (percorsi, certificati, intestazioni)
- da aggiornare quando la configurazione è consolidata

Dipendenze correlate:

- `03-DNS-E-DOMINI`
- `04-VPS-E-HARDENING`
- `06-BACKEND`
- `07-DEPLOYMENT`
- `15-BACKUP-E-RECOVERY`

---

## 17. Changelog

### v0.1
- documentato il ruolo di nginx come reverse proxy
- descritta la terminazione HTTPS e la configurazione del virtual host
- definite gestione certificati, comandi operativi e sicurezza web
- registrate superfici critiche e procedura di ripristino
