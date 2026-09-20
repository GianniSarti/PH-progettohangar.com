# Progetto Hangar — VPS e Hardening
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la configurazione della VPS di **Progetto Hangar** e le misure di sicurezza applicate (hardening).

Serve a:

- documentare le caratteristiche del server
- descrivere le scelte di sicurezza adottate
- fornire una procedura ricostruibile in caso di reinstallazione o sostituzione della VPS
- permettere a un operatore o a una IA di comprendere lo stato di sicurezza senza inferenze
- ridurre il rischio di blocco operativo o di errori di configurazione

Questo file non contiene segreti in chiaro.  
Password, chiavi private e dati di recupero vanno censiti nel file dedicato ai segreti.

---

## 2. Ruolo della VPS

La VPS è il nodo controllato direttamente che ospita:

- il backend FastAPI
- il reverse proxy nginx
- la terminazione HTTPS per `api.progettohangar.com`

È un componente critico:

- rappresenta il punto di esecuzione del backend
- è esposto pubblicamente tramite un sottodominio
- richiede quindi una postura di sicurezza rigorosa ma gestibile

---

## 3. Caratteristiche del server

Parametri principali da documentare.

| Parametro | Valore | Note |
|---|---|---|
| Provider VPS | `<DA_COMPILARE>` | fornitore del server |
| Piano / risorse | `<DA_COMPILARE>` | CPU, RAM, disco |
| Sistema operativo | Ubuntu 24.04 | LTS |
| Regione / datacenter | `<DA_COMPILARE>` | posizione fisica |
| Hostname | `<DA_COMPILARE>` | nome host del server |
| IP pubblico | `<DA_COMPILARE_NON_SEGRETO>` | indirizzo pubblico |
| Utente operativo | `pilota` | utente principale non-root |
| Porta SSH | `134` | porta custom |

Nota:

- l'IP pubblico non è un segreto, ma va comunque conservato e aggiornato
- provider, piano e regione servono per ricostruire o migrare l'ambiente

---

## 4. Principi di hardening adottati

Principi seguiti:

- ridurre la superficie di attacco
- non usare l'utente root per l'operatività quotidiana
- non esporre servizi non necessari
- limitare e monitorare gli accessi
- privilegiare autenticazione a chiave rispetto a password dove possibile
- mantenere il sistema aggiornato
- documentare ogni scelta di sicurezza

Interpretazione pratica:

- accesso amministrativo tramite utente dedicato `pilota`
- root non accessibile via SSH
- porta SSH spostata su valore custom
- firewall attivo con regole minime
- protezione contro tentativi di accesso ripetuti tramite fail2ban

---

## 5. Utente operativo

Utente principale:

- `pilota`

Caratteristiche:

- utente non-root
- utilizzato per accesso SSH e operazioni quotidiane
- dotato di privilegi amministrativi tramite sudo

Regole:

- non usare root per attività ordinarie
- eseguire operazioni amministrative tramite sudo con l'utente `pilota`
- conservare in modo sicuro la password sudo nel file dei segreti

Verifica utente e privilegi:

```bash
whoami
id
sudo -v
```

---

## 6. Accesso SSH

Configurazione adottata:

- accesso SSH su porta custom `134`
- accesso root via SSH disabilitato
- accesso tramite utente `pilota`
- autenticazione basata su chiave SSH

Connessione tipica:

```bash
ssh -p 134 pilota@<IP_O_HOST_VPS>
```

Con alias configurato nel file locale `~/.ssh/config`:

```bash
ssh <ALIAS_HOST>
```

Regole di sicurezza SSH:

- mantenere disabilitato l'accesso diretto come root
- preferire autenticazione a chiave
- non condividere la chiave privata
- conservare la chiave privata secondo il file di backup dedicato

---

## 7. Configurazione SSH lato server

Il comportamento del servizio SSH è definito nella configurazione del daemon.

Percorso tipico:

```bash
/etc/ssh/sshd_config
```

Elementi chiave da mantenere coerenti con l'hardening:

- porta impostata su `134`
- accesso root disabilitato
- autenticazione a chiave abilitata

Riferimenti logici delle direttive tipiche:

```text
Port 134
PermitRootLogin no
PubkeyAuthentication yes
```

Nota:

- i valori esatti presenti sul server vanno verificati alla fonte
- ogni modifica al file richiede riavvio controllato del servizio SSH

Verifica dello stato del servizio SSH:

```bash
sudo systemctl status ssh
```

Attenzione operativa:

- prima di riavviare SSH dopo una modifica, assicurarsi di avere una sessione attiva di riserva
- un errore di configurazione può bloccare l'accesso remoto

---

## 8. Firewall (UFW)

Stato:

- UFW attivo

Ruolo:

- limitare le porte accessibili
- consentire solo il traffico necessario

Porte tipicamente necessarie:

- SSH sulla porta custom `134`
- HTTP `80` (per gestione certificati / redirect)
- HTTPS `443` (traffico applicativo pubblico)

Verifica stato firewall:

```bash
sudo ufw status verbose
```

Regole di riferimento (da verificare e adattare allo stato reale):

```bash
sudo ufw allow 134/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

Principi:

- consentire solo ciò che serve
- non lasciare aperta la porta SSH standard `22` se non utilizzata
- documentare ogni regola aggiunta

Attenzione operativa:

- prima di abilitare o modificare il firewall, assicurarsi che la porta SSH `134` sia consentita
- un errore può escludere l'accesso remoto

---

## 9. Protezione accessi (fail2ban)

Stato:

- fail2ban attivo

Ruolo:

- rilevare tentativi di accesso ripetuti e sospetti
- bloccare temporaneamente gli indirizzi che superano le soglie

Verifica stato generale:

```bash
sudo systemctl status fail2ban
```

Verifica stato delle regole attive:

```bash
sudo fail2ban-client status
```

Verifica di una specifica protezione (esempio SSH):

```bash
sudo fail2ban-client status sshd
```

Note:

- la configurazione deve tenere conto della porta SSH custom `134`
- i parametri di ban e soglie vanno documentati se personalizzati
- verificare periodicamente i log per tentativi anomali

---

## 10. Aggiornamenti di sistema

Buone pratiche:

- mantenere il sistema aggiornato
- applicare aggiornamenti di sicurezza con regolarità
- valutare aggiornamenti importanti in momenti controllati

Comandi di aggiornamento:

```bash
sudo apt update
sudo apt upgrade
```

Note:

- pianificare gli aggiornamenti per non impattare il servizio in momenti critici
- dopo aggiornamenti rilevanti, verificare che backend e nginx funzionino correttamente

---

## 11. Servizi in esecuzione

Sulla VPS girano tipicamente:

- servizio SSH
- nginx come reverse proxy
- processo applicativo backend FastAPI
- fail2ban
- firewall UFW

Verifica servizi principali:

```bash
sudo systemctl status ssh
sudo systemctl status nginx
sudo systemctl status fail2ban
```

Nota:

- la gestione operativa del processo FastAPI (modalità di avvio, supervisione, riavvio) sarà dettagliata nei file dedicati a backend e deployment
- questo capitolo si concentra sulla sicurezza del server, non sul ciclo di vita dell'applicazione

---

## 12. Relazione con nginx e HTTPS

La VPS ospita nginx, che:

- riceve il traffico HTTPS pubblico
- inoltra le richieste al backend FastAPI
- gestisce la terminazione TLS per `api.progettohangar.com`

Dettagli specifici:

- la configurazione dei virtual host, dei certificati e del reverse proxy è trattata nel file dedicato `08-NGINX-E-HTTPS`
- in questo documento è sufficiente sapere che nginx è parte integrante della superficie pubblica del server e va incluso nelle verifiche di sicurezza

---

## 13. Superfici critiche del server

Punti sensibili:

- accesso SSH
- utente `pilota` e password sudo
- chiavi SSH autorizzate
- configurazione del daemon SSH
- regole firewall
- configurazione fail2ban
- file di ambiente e segreti applicativi presenti sul server
- configurazione nginx e certificati

Attenzioni:

- la compromissione di uno di questi elementi può compromettere l'intero backend
- ogni modifica va eseguita con cautela e documentata

---

## 14. Procedura di ricostruzione della VPS

In caso di reinstallazione o sostituzione del server, sequenza logica di riferimento:

1. creare la nuova VPS con Ubuntu 24.04
2. creare l'utente operativo `pilota` con privilegi sudo
3. caricare la chiave pubblica SSH autorizzata per `pilota`
4. configurare il daemon SSH:
   - porta `134`
   - root login disabilitato
   - autenticazione a chiave
5. riavviare il servizio SSH mantenendo una sessione di riserva
6. configurare e attivare UFW con le porte necessarie
7. installare e attivare fail2ban, tenendo conto della porta SSH custom
8. installare e configurare nginx
9. ripristinare la configurazione del backend e delle variabili d'ambiente dai backup sicuri
10. ripristinare/riemettere i certificati HTTPS
11. verificare la raggiungibilità di `api.progettohangar.com`
12. eseguire i controlli di sicurezza e i test funzionali
13. aggiornare questo documento e il changelog

Nota:

- i valori e i segreti reali provengono dal file dei segreti e dai backup
- questa procedura è una guida di sequenza, non un elenco di credenziali

---

## 15. Controlli di verifica post-configurazione

Dopo configurazione o ripristino, verificare:

```bash
# accesso SSH sulla porta custom
ssh -p 134 pilota@<IP_O_HOST_VPS>

# stato firewall
sudo ufw status verbose

# stato fail2ban
sudo systemctl status fail2ban

# stato nginx
sudo systemctl status nginx

# raggiungibilità API
curl -I https://api.progettohangar.com
```

Esito atteso:

- accesso SSH funzionante solo su porta `134`
- root non accessibile via SSH
- firewall attivo con sole porte necessarie
- fail2ban attivo
- nginx attivo
- API raggiungibile in HTTPS

---

## 16. Assunzioni correnti

Assunzioni valide alla stesura:

- esiste una sola VPS di produzione
- il sistema operativo è Ubuntu 24.04
- l'accesso avviene tramite utente `pilota` su porta `134`
- root SSH è disabilitato
- UFW e fail2ban sono attivi
- nginx gestisce l'esposizione pubblica del backend

Se queste assunzioni cambiano, aggiornare il documento.

---

## 17. Attività aperte

Attività da completare o verificare:

- compilare i parametri del server nella tabella caratteristiche
- documentare eventuali personalizzazioni di fail2ban
- confermare l'elenco esatto delle regole UFW attive
- allineare questo capitolo con `06-BACKEND`, `07-DEPLOYMENT` e `08-NGINX-E-HTTPS`
- verificare la presenza e la sicurezza dei file di ambiente sul server

---

## 18. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come descrizione della postura di sicurezza della VPS
- incompleto nei parametri puntuali del server
- da completare con i valori reali e con eventuali personalizzazioni

Dipendenze correlate:

- `02-INFRASTRUTTURA`
- `03-DNS-E-DOMINI`
- `06-BACKEND`
- `07-DEPLOYMENT`
- `08-NGINX-E-HTTPS`
- `14-SECRETS-INVENTORY`
- `15-BACKUP-E-RECOVERY`

---

## 19. Changelog

### v0.1
- documentata la configurazione di sicurezza della VPS
- descritti utente operativo, SSH, firewall e fail2ban
- definita la procedura di ricostruzione del server
- elencati controlli di verifica e attività aperte
