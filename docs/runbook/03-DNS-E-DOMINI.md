# Progetto Hangar — DNS e Domini
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la gestione del dominio e della configurazione DNS di **Progetto Hangar**.

Serve a:

- documentare il dominio principale e i sottodomini in uso
- chiarire il ruolo di ogni record DNS
- spiegare come frontend, backend ed email sono instradati
- fornire una base per verifica, manutenzione e ripristino della configurazione DNS
- permettere a un operatore o a una IA di ricostruire l'instradamento senza inferenze

Questo file non contiene segreti.  
Token, chiavi API e credenziali di accesso a Cloudflare vanno censiti nel file dedicato ai segreti, senza esporli in chiaro.

---

## 2. Dominio principale

Dominio del progetto:

- `progettohangar.com`

Ruolo del dominio:

- identità pubblica del brand
- radice per il sito pubblico
- radice per l'API di backend
- base per la posta elettronica di dominio
- base per l'invio di email transazionali tramite sottodominio dedicato

Stato:

- attivo
- operativo

---

## 3. Gestione DNS

Provider DNS:

- Cloudflare

Ruolo di Cloudflare in ambito DNS:

- autorità di gestione dei record DNS del dominio
- eventuale proxying dei record compatibili
- instradamento verso frontend, backend ed email
- punto di controllo centrale della configurazione di rete pubblica

Stato:

- configurato
- operativo

Nota operativa:

- l'accesso al pannello Cloudflare è una superficie critica
- deve essere documentato nel file dei segreti insieme ai dati di recupero

---

## 4. Modello di instradamento

Vista logica dell'instradamento:

- il sito pubblico risponde sul dominio principale e/o sul sottodominio `www`
- l'API risponde sul sottodominio dedicato `api`
- la posta di dominio è gestita tramite record dedicati verso il provider email
- le email transazionali usano un sottodominio dedicato per l'invio

Principio adottato:

- separazione chiara tra frontend, backend ed email
- ogni funzione ha il proprio punto di ingresso DNS
- nessuna sovrapposizione ambigua tra i servizi

---

## 5. Sottodomini principali

### 5.1 Sito pubblico
Nomi coinvolti:

- `progettohangar.com`
- `www.progettohangar.com`

Destinazione:

- frontend su Cloudflare Pages

Ruolo:

- presentazione pubblica del brand
- pagine prodotto e contenuti

Stato:

- da confermare nel dettaglio dei record durante la pubblicazione definitiva del frontend

---

### 5.2 API backend
Nome:

- `api.progettohangar.com`

Destinazione:

- VPS Ubuntu tramite nginx

Ruolo:

- endpoint pubblico del backend FastAPI

Stato:

- attivo
- servito in HTTPS dietro nginx

---

### 5.3 Email di dominio
Nomi coinvolti:

- record a livello di dominio principale per la posta

Destinazione:

- provider email di dominio (Fastmail)

Ruolo:

- gestione caselle operative e amministrative

Stato:

- da mantenere allineato alle indicazioni ufficiali del provider

---

### 5.4 Email transazionali
Nome:

- sottodominio dedicato per invio transazionale

Destinazione:

- provider email transazionale (Resend)

Ruolo:

- invio di email automatiche applicative

Stato:

- da configurare/verificare con i record richiesti dal provider

---

## 6. Tipologie di record DNS coinvolte

L'infrastruttura di Progetto Hangar coinvolge tipicamente le seguenti categorie di record:

- record di indirizzo per il backend (host `api`)
- record per il frontend gestito su Cloudflare Pages
- record MX per la posta di dominio
- record di autenticazione email (verifiche di dominio e firma dei messaggi)
- eventuali record di verifica proprietà richiesti dai servizi

Nota importante:

- i valori specifici dei record non vanno inventati
- devono corrispondere esattamente a quelli indicati dai rispettivi provider
- ogni valore va verificato nel pannello Cloudflare al momento della manutenzione

---

## 7. Tabella di riferimento dei record

La seguente tabella è un modello da compilare con i valori reali presenti in Cloudflare.  
Non inserire qui segreti; i valori DNS pubblici possono essere documentati, ma vanno verificati alla fonte.

| Nome / Host | Tipo | Scopo | Destinazione logica | Proxy | Stato | Note |
|---|---|---|---|---|---|---|
| `progettohangar.com` | (da compilare) | sito pubblico | Cloudflare Pages | (da compilare) | da verificare | dominio radice |
| `www` | (da compilare) | sito pubblico | Cloudflare Pages | (da compilare) | da verificare | alias sito |
| `api` | (da compilare) | backend API | VPS / nginx | (da compilare) | attivo | endpoint FastAPI |
| posta dominio | MX | email di dominio | Fastmail | non applicabile | da verificare | seguire istruzioni provider |
| autenticazione email | (da compilare) | verifica e firma email | provider email | (da compilare) | da verificare | record di autenticazione dominio |
| sottodominio transazionale | (da compilare) | invio email automatiche | Resend | (da compilare) | da verificare | seguire istruzioni provider |
| record di verifica servizi | (da compilare) | verifica proprietà | servizio richiedente | (da compilare) | da verificare | solo se richiesti |

Regola:

- ogni volta che un record viene creato, modificato o rimosso, aggiornare questa tabella e il changelog

---

## 8. Relazione tra DNS e servizi

Sintesi delle dipendenze:

- il sito pubblico dipende dal corretto instradamento del dominio principale verso Cloudflare Pages
- il backend dipende dal record `api` verso la VPS
- la posta di dominio dipende dai record MX e di autenticazione verso Fastmail
- le email transazionali dipendono dai record di dominio/sottodominio verso Resend
- il funzionamento HTTPS del backend dipende sia dal DNS corretto sia dalla configurazione nginx/TLS sulla VPS

Implicazione operativa:

- un errore DNS può interrompere sito, API o email in modo indipendente
- per ogni malfunzionamento, verificare prima il record coinvolto e poi il servizio di destinazione

---

## 9. Considerazioni su proxy e sicurezza

Aspetti da tenere presenti:

- alcuni record possono essere serviti in modalità proxy tramite Cloudflare
- il record del backend deve permettere il corretto funzionamento di HTTPS verso nginx sulla VPS
- eventuali scelte di proxy vanno documentate perché influenzano:
  - indirizzo IP visibile
  - gestione dei certificati
  - comportamento del traffico

Regola prudenziale:

- non modificare la modalità proxy dei record critici senza aver compreso l'impatto su TLS e raggiungibilità
- annotare sempre lo stato proxy nella tabella dei record

---

## 10. Procedura di verifica DNS

Verifiche consigliate periodiche o dopo modifiche.

### 10.1 Verifica risoluzione backend
Controllare che l'host API risponda correttamente:

```bash
dig api.progettohangar.com +short
```

Verificare risposta HTTPS applicativa:

```bash
curl -I https://api.progettohangar.com
```

### 10.2 Verifica dominio principale
Controllare la risoluzione del dominio radice e di `www`:

```bash
dig progettohangar.com +short
dig www.progettohangar.com +short
```

### 10.3 Verifica record email
Controllare i record MX:

```bash
dig progettohangar.com MX +short
```

Controllare i record di autenticazione email secondo le indicazioni dei provider:

```bash
dig <NOME_RECORD_AUTENTICAZIONE> TXT +short
```

Nota:

- i nomi esatti dei record di autenticazione dipendono dalle istruzioni di Fastmail e Resend
- non usare valori generici: usare quelli reali forniti dai provider

---

## 11. Procedura di modifica sicura dei record

Quando si modifica un record DNS:

1. annotare lo stato attuale prima della modifica
2. eseguire una sola modifica per volta quando possibile
3. verificare la propagazione con gli strumenti di controllo
4. testare il servizio impattato
5. aggiornare la tabella dei record
6. aggiornare il changelog del documento

Principio:

- ogni modifica DNS è potenzialmente critica
- meglio procedere in modo incrementale e verificabile

---

## 12. Superfici critiche in ambito DNS

Punti sensibili:

- accesso al pannello Cloudflare
- record del backend `api`
- record MX della posta
- record di autenticazione email
- eventuali record di verifica dei servizi di pagamento o email

Attenzioni:

- la perdita di accesso a Cloudflare comprometterebbe il controllo dell'instradamento
- un errore sui record email può compromettere deliverability e reputazione del dominio
- un errore sul record API può mettere offline il backend

Mitigazione:

- documentare accessi e recovery nel file dei segreti
- mantenere questa mappa DNS aggiornata
- verificare periodicamente i record critici

---

## 13. Assunzioni correnti

Assunzioni valide alla stesura:

- il dominio è gestito tramite Cloudflare
- esiste un solo dominio principale di progetto
- il backend è esposto tramite un unico sottodominio `api`
- la posta di dominio è affidata a Fastmail
- le email transazionali sono affidate a Resend
- non esistono al momento ambienti multipli con sottodomini dedicati aggiuntivi

Se queste assunzioni cambiano, aggiornare il documento.

---

## 14. Attività aperte

Attività ancora da completare o verificare:

- compilare la tabella dei record con i valori reali
- confermare i record definitivi del frontend alla pubblicazione
- verificare e documentare i record di autenticazione email
- confermare la configurazione dei record per l'invio transazionale
- annotare lo stato proxy di ciascun record critico

---

## 15. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come mappa logica di dominio e DNS
- incompleto nei valori puntuali dei record
- da completare con i dati reali presenti in Cloudflare

Dipendenze correlate:

- `02-INFRASTRUTTURA`
- `04-VPS-E-HARDENING`
- `08-NGINX-E-HTTPS`
- `10-EMAIL`
- `14-SECRETS-INVENTORY`

---

## 16. Changelog

### v0.1
- definita la mappa logica di dominio e DNS
- elencati i sottodomini principali e i loro ruoli
- creato il modello di tabella dei record
- documentate procedure di verifica e modifica sicura
- registrate superfici critiche e attività aperte
