# Progetto Hangar — Runbook Infrastrutturale

Documentazione tecnica, operativa e replicabile del progetto **Progetto Hangar**: boutique artigianale di Expert Advisor per MetaTrader 5.

Questo Runbook descrive infrastruttura, servizi, integrazioni, sicurezza, continuità operativa, prodotto e brand. È pensato per essere compreso e utilizzato sia da un operatore umano sia da una IA.

---

## Da dove iniziare

- Leggi prima `00-INDICE.md` per l'orientamento generale
- Poi `01-PANORAMICA.md` per il quadro d'insieme del progetto

---

## Struttura della documentazione

### Indice e orientamento
- `00-INDICE.md`
- `01-PANORAMICA.md`

### Inventario infrastruttura
- `02-INFRASTRUTTURA.md`
- `03-DNS-E-DOMINI.md`
- `04-VPS-E-HARDENING.md`

### Applicazioni e deploy
- `05-FRONTEND.md`
- `06-BACKEND.md`
- `07-DEPLOYMENT.md`
- `08-NGINX-E-HTTPS.md`

### Dati, servizi e integrazioni
- `09-DATABASE.md`
- `10-EMAIL.md`
- `11-STRIPE-MOR.md`
- `12-TRANSAZIONI-E-WEBHOOK.md`

### Sicurezza e continuità operativa
- `13-ACCESSI-E-IDENTITA.md`
- `14-SECRETS-INVENTORY.md`
- `15-BACKUP-E-RECOVERY.md`
- `16-MONITORAGGIO-E-MANUTENZIONE.md`
- `17-INCIDENT-RESPONSE.md`

### Contenuti, compliance e prodotto
- `18-PRODOTTI-E-SKU.md`
- `19-DISCLAIMER-E-COMPLIANCE.md`
- `20-I18N.md`

### Brand e asset visivi
- `21-BRAND-ASSETS.md`
- `22-IMMAGINI-PRODOTTO.md`

### Appendici
- `90-GLOSSARIO.md`
- `91-DECISIONI-ARCHITETTURALI.md`
- `99-CHANGELOG.md`

### Allegati operativi
- `allegati/BACKUP-CHIAVI-SSH-CHECKLIST.md`
- `allegati/SECRETS-INVENTORY-TEMPLATE.md`

---

## Regole importanti

- Non inserire mai segreti in chiaro in questi file. I valori reali vanno conservati in password manager e archivio cifrato, come descritto in `14-SECRETS-INVENTORY.md`.
- I documenti usano placeholder (es. `<DA_COMPILARE>`) dove servono valori reali.
- Ogni modifica infrastrutturale va riflessa nel documento pertinente e annotata nel changelog.

---

## Stato

- Versione corrente: v0.1 (prima stesura completa)
- Tutti i capitoli sono in stato Bozza e vanno completati con i valori reali nelle sedi sicure.
- Priorità immediate: messa in sicurezza di chiavi SSH e segreti prima della reinstallazione del Mac.

---

## Convenzioni

- File numerati con prefisso a due cifre
- Markdown per GitHub
- Date in formato ISO `YYYY-MM-DD`
- Lingua: italiano
