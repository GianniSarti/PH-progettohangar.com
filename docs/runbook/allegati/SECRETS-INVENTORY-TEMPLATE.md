 Secrets Inventory — Template

## Regola
Non inserire mai i segreti in chiaro in questo file.  
Inserire solo metadati, posizione di conservazione e stato.

---

## Campi standard

| Nome segreto | Servizio | Ambiente | Finalità | Dove è conservato | Stato | Ultimo controllo | Note |
|---|---|---|---|---|---|---|---|

---

## Voci da censire subito

| Nome segreto | Servizio | Ambiente | Finalità | Dove è conservato | Stato | Ultimo controllo | Note |
|---|---|---|---|---|---|---|---|
| SSH private key VPS | VPS | production | accesso server | `<DA_COMPILARE>` | da verificare | `<DATA>` | utente `pilota` |
| GitHub token / accesso repo | GitHub | production | accesso codice e repo | `<DA_COMPILARE>` | da verificare | `<DATA>` | verificare se presente PAT |
| Cloudflare API token | Cloudflare | production | DNS / deploy / config | `<DA_COMPILARE>` | da verificare | `<DATA>` | |
| Cloudflare account recovery data | Cloudflare | production | recupero accesso | `<DA_COMPILARE>` | da verificare | `<DATA>` | |
| MongoDB URI | MongoDB Atlas | production | connessione backend DB | `<DA_COMPILARE>` | da verificare | `<DATA>` | non salvare URI in chiaro qui |
| MongoDB account recovery data | MongoDB Atlas | production | recupero accesso | `<DA_COMPILARE>` | da verificare | `<DATA>` | |
| Stripe secret key | Stripe | production | API pagamenti | `<DA_COMPILARE>` | da verificare | `<DATA>` | |
| Stripe webhook secret | Stripe | production | validazione webhook | `<DA_COMPILARE>` | da verificare | `<DATA>` | |
| Stripe account recovery data | Stripe | production | recupero accesso | `<DA_COMPILARE>` | da verificare | `<DATA>` | 2FA solo se obbligatoria |
| Resend API key | Resend | production | email transazionali | `<DA_COMPILARE>` | da verificare | `<DATA>` | |
| Fastmail app password / access data | Fastmail | production | posta dominio | `<DA_COMPILARE>` | da verificare | `<DATA>` | |
| VPS sudo password | VPS | production | operazioni amministrative | `<DA_COMPILARE>` | da verificare | `<DATA>` | non salvarla in chiaro nel repo |
| Environment file backend | Backend | production | config runtime | `<DA_COMPILARE>` | da verificare | `<DATA>` | es. `.env` su server |
| nginx site config backup | VPS/nginx | production | ripristino reverse proxy | `<DA_COMPILARE>` | da verificare | `<DATA>` | non è un segreto puro, ma va censito |
| Domain registrar access / recovery | Dominio | production | gestione dominio | `<DA_COMPILARE>` | da verificare | `<DATA>` | se separato da Cloudflare |
| Apple / dispositivi recovery codes | Dispositivo | personal | continuità accesso locale | `<DA_COMPILARE>` | da verificare | `<DATA>` | utile per reinstall e recovery |

---

## Priorità di messa in sicurezza

### Priorità alta
- SSH key VPS
- Stripe secret key
- Stripe webhook secret
- MongoDB URI
- Cloudflare token
- Resend API key
- accessi GitHub

### Priorità media
- Fastmail
- backup config nginx
- recovery data servizi

### Priorità bassa
- elementi rigenerabili o facilmente ricostruibili

---

## Stato finale desiderato

Ogni voce deve risultare:

- identificata
- localizzata
- verificata
- copiata in archivio sicuro
- recuperabile senza dipendere dalla memoria
