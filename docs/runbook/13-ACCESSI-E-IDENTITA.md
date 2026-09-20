# Progetto Hangar — Accessi e Identità
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la gestione degli accessi e delle identità di **Progetto Hangar**.

Serve a:

- censire gli account e i punti di accesso ai servizi
- definire la politica di autenticazione e di recupero
- chiarire la posizione del progetto rispetto alla 2FA
- garantire continuità di accesso in caso di reinstallazione del Mac o cambio dispositivo
- permettere a un operatore o a una IA di comprendere la mappa degli accessi

Questo file non contiene segreti.  
Credenziali, token e recovery code sono gestiti secondo `14-SECRETS-INVENTORY`.

---

## 2. Identità dell'operatore

Operatore principale:

- Gianni (founder di Progetto Hangar)

Ruolo:

- unico amministratore e responsabile degli accessi
- gestore dei segreti e dei backup
- responsabile della continuità operativa

Implicazione:

- in assenza di altri operatori, la resilienza degli accessi dipende interamente dalla corretta conservazione di credenziali e recovery data

---

## 3. Politica sulla 2FA

Politica del progetto:

- evitare la 2FA dove non è strettamente obbligatoria
- accettare la 2FA solo dove imposta dalla piattaforma

Motivazione:

- preferenza personale dell'operatore per semplicità di accesso
- riduzione del rischio di blocco dovuto a dispositivi 2FA persi

Servizi che possono imporre comunque 2FA:

- Stripe
- dispositivi/account Apple
- eventuali altri servizi con obbligo non disattivabile

Regola compensativa:

- dove la 2FA è attiva o obbligatoria, i recovery code vanno conservati con la massima cura in `14-SECRETS-INVENTORY`
- questo compensa l'assenza di ridondanza tipica della 2FA

---

## 4. Rischio specifico legato alla 2FA e al reinstall

Rischio:

- reinstallando il Mac o cambiando dispositivo, l'accesso a eventuali app di autenticazione o passkey può andare perso

Mitigazione obbligatoria prima del reinstall:

- salvare tutti i recovery code dei servizi con 2FA attiva
- verificare metodi di accesso alternativi
- confermare la recuperabilità degli account critici
- documentare in `14-SECRETS-INVENTORY` dove si trovano i recovery data

---

## 5. Mappa degli accessi

Elenco dei principali punti di accesso da presidiare.

| Servizio | Tipo accesso | 2FA | Criticità | Recovery documentato | Note |
|---|---|---|---|---|---|
| VPS (SSH) | chiave SSH + utente `pilota` | non applicabile | alta | `<SI/NO>` | porta `134`, root disabilitato |
| GitHub | account + eventuale PAT | `<STATO>` | alta | `<SI/NO>` | monorepo |
| Cloudflare | account | `<STATO>` | alta | `<SI/NO>` | DNS e Pages |
| MongoDB Atlas | account | `<STATO>` | alta | `<SI/NO>` | database |
| Stripe | account | obbligatoria/probabile | alta | `<SI/NO>` | pagamenti MoR |
| Resend | account | `<STATO>` | media | `<SI/NO>` | email transazionali |
| Fastmail | account | `<STATO>` | media | `<SI/NO>` | posta di dominio |
| Registrar dominio | account | `<STATO>` | media | `<SI/NO>` | se separato da Cloudflare |
| Apple ID / dispositivo | account | probabile | media | `<SI/NO>` | continuità locale |
| Password manager | master | dipende | massima | `<SI/NO>` | custodisce tutti i segreti |

Regola:

- ogni nuovo servizio con accesso va aggiunto a questa mappa

---

## 6. Gerarchia della criticità degli accessi

### Criticità massima
- password manager (custodisce tutto il resto)

### Criticità alta
- VPS SSH
- GitHub
- Cloudflare
- MongoDB Atlas
- Stripe

### Criticità media
- Resend
- Fastmail
- registrar dominio
- Apple ID / dispositivo

Principio:

- la perdita del password manager avrebbe l'impatto più grave
- va protetto con priorità assoluta e recovery ridondante

---

## 7. Accesso alla VPS

Modello:

- accesso tramite chiave SSH
- utente operativo `pilota`
- porta custom `134`
- root disabilitato

Riferimento:

- dettagli in `04-VPS-E-HARDENING`

Continuità:

- la chiave privata SSH deve essere backuppata secondo la checklist dedicata
- in assenza della chiave, l'accesso al server verrebbe perso

---

## 8. Accesso ai servizi cloud

Principi:

- ogni servizio cloud ha un account presidiato dall'operatore
- gli accessi sono documentati nella mappa
- i recovery data sono conservati in modo sicuro

Buone pratiche:

- usare password robuste e uniche per ogni servizio
- conservarle nel password manager
- non riutilizzare la stessa password su più servizi

---

## 9. Gestione dei token e delle chiavi API

Token e chiavi API (Cloudflare, GitHub PAT, Stripe, Resend):

- sono a tutti gli effetti credenziali
- vanno trattati come segreti
- vanno tracciati in `14-SECRETS-INVENTORY`

Principi:

- creare token con privilegi minimi necessari
- revocare i token non più usati
- ruotare i token in caso di sospetto compromesso

---

## 10. Password manager

Ruolo centrale:

- custodisce le credenziali di tutti i servizi
- custodisce i recovery code
- è il punto più critico dell'intera catena di accesso

Requisiti:

- master password robusta e memorizzata in modo sicuro
- recovery del password manager documentato e ridondato
- accesso verificato prima del reinstall del Mac

Attenzione:

- se il password manager usa 2FA o chiavi legate al dispositivo, garantire il recupero su nuova macchina

---

## 11. Procedura di continuità accessi prima del reinstall

Checklist critica prima di reinstallare il Mac:

- [ ] backup chiavi SSH completato e verificato
- [ ] accesso al password manager garantito su nuovo dispositivo
- [ ] recovery code di tutti i servizi con 2FA salvati
- [ ] credenziali di tutti i servizi verificate nel password manager
- [ ] accesso a GitHub verificato
- [ ] accesso a Cloudflare verificato
- [ ] accesso a Stripe verificato
- [ ] accesso a MongoDB Atlas verificato
- [ ] accesso email (Fastmail/Resend) verificato
- [ ] mappa accessi aggiornata

Regola:

- non procedere al reinstall finché tutte le voci non sono confermate

---

## 12. Procedura di ripristino accessi su nuovo dispositivo

Sequenza logica:

1. installare e sbloccare il password manager
2. ripristinare le chiavi SSH e correggere i permessi
3. verificare l'accesso alla VPS
4. verificare l'accesso a GitHub e clonare il repository
5. verificare l'accesso ai pannelli dei servizi critici
6. riconfigurare eventuali 2FA obbligatorie sui nuovi dispositivi
7. aggiornare la mappa accessi con eventuali nuovi metodi
8. aggiornare il changelog

---

## 13. Superfici critiche di accesso

Punti di attenzione:

- password manager compromesso o non recuperabile
- perdita delle chiavi SSH
- perdita dei recovery code 2FA
- token API con privilegi eccessivi
- account critici senza metodo di recupero verificato

Mitigazioni:

- ridondanza e verifica del password manager
- backup delle chiavi SSH
- conservazione accurata dei recovery code
- principio del privilegio minimo per i token
- verifica periodica dei metodi di recupero

---

## 14. Assunzioni correnti

Assunzioni valide alla stesura:

- unico operatore: Gianni
- politica di evitare 2FA dove non obbligatoria
- alcuni servizi impongono comunque 2FA
- il password manager è il fulcro della gestione accessi
- reinstallazione del Mac imminente

Se queste assunzioni cambiano, aggiornare il documento.

---

## 15. Attività aperte

Attività da completare:

- compilare la mappa accessi con stati reali di 2FA e recovery
- verificare la recuperabilità del password manager
- salvare tutti i recovery code
- eseguire la checklist di continuità prima del reinstall
- rivedere i privilegi dei token API

---

## 16. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come mappa e politica degli accessi
- incompleto finché non compilati stati reali e recovery
- prioritario da completare prima del reinstall del Mac

Dipendenze correlate:

- `04-VPS-E-HARDENING`
- `14-SECRETS-INVENTORY`
- `15-BACKUP-E-RECOVERY`
- `17-INCIDENT-RESPONSE`

---

## 17. Changelog

### v0.1
- documentata la mappa e la politica degli accessi
- definita la posizione sulla 2FA e i rischi legati al reinstall
- create checklist di continuità e ripristino accessi
- registrate superfici critiche e attività aperte
