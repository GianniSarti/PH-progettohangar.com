# Progetto Hangar — Changelog del Runbook
Versione: 0.1  
Stato: Attivo  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento traccia l'evoluzione complessiva del Runbook di **Progetto Hangar**.

Serve a:

- registrare le modifiche significative alla documentazione
- fornire una vista d'insieme dello stato di avanzamento
- permettere a un operatore o a una IA di capire cosa è cambiato e quando

Nota:

- ogni singolo capitolo mantiene anche il proprio changelog interno
- questo file offre la vista globale

---

## 2. Convenzioni di versionamento

Regole:

- versioni in formato `MAJOR.MINOR`
- incrementare MINOR per aggiunte e aggiornamenti ordinari
- incrementare MAJOR per revisioni strutturali importanti
- date in formato ISO `YYYY-MM-DD`

Stati dei documenti:

- `Bozza`
- `Attivo`
- `Da verificare`
- `Deprecato`

---

## 3. Stato di avanzamento dei capitoli

| File | Versione | Stato |
|---|---|---|
| 00-INDICE | 0.1 | Bozza |
| 01-PANORAMICA | 0.1 | Bozza |
| 02-INFRASTRUTTURA | 0.1 | Bozza |
| 03-DNS-E-DOMINI | 0.1 | Bozza |
| 04-VPS-E-HARDENING | 0.1 | Bozza |
| 05-FRONTEND | 0.1 | Bozza |
| 06-BACKEND | 0.1 | Bozza |
| 07-DEPLOYMENT | 0.1 | Bozza |
| 08-NGINX-E-HTTPS | 0.1 | Bozza |
| 09-DATABASE | 0.1 | Bozza |
| 10-EMAIL | 0.1 | Bozza |
| 11-STRIPE-MOR | 0.1 | Bozza |
| 12-TRANSAZIONI-E-WEBHOOK | 0.1 | Bozza |
| 13-ACCESSI-E-IDENTITA | 0.1 | Bozza |
| 14-SECRETS-INVENTORY | 0.1 | Bozza |
| 15-BACKUP-E-RECOVERY | 0.1 | Bozza |
| 16-MONITORAGGIO-E-MANUTENZIONE | 0.1 | Bozza |
| 17-INCIDENT-RESPONSE | 0.1 | Bozza |
| 18-PRODOTTI-E-SKU | 0.1 | Bozza |
| 19-DISCLAIMER-E-COMPLIANCE | 0.1 | Bozza |
| 20-I18N | 0.1 | Bozza |
| 21-BRAND-ASSETS | 0.1 | Bozza |
| 22-IMMAGINI-PRODOTTO | 0.1 | Bozza |
| 90-GLOSSARIO | 0.1 | Bozza |
| 91-DECISIONI-ARCHITETTURALI | 0.1 | Bozza |
| 99-CHANGELOG | 0.1 | Attivo |

---

## 4. Storico delle versioni globali

### v0.1 — 2026-09-20
Prima stesura completa della struttura del Runbook.

Aggiunti:

- indice e panoramica (00, 01)
- inventario infrastruttura (02, 03, 04)
- applicazioni e deploy (05, 06, 07, 08)
- dati, servizi e integrazioni (09, 10, 11, 12)
- sicurezza e continuità (13, 14, 15, 16, 17)
- contenuti, compliance e prodotto (18, 19, 20)
- brand e asset visivi (21, 22)
- appendici (90, 91, 99)
- allegati operativi: checklist backup chiavi SSH e template inventario segreti

Note:

- tutti i capitoli sono in stato Bozza (v0.1)
- i contenuti puntuali (valori reali, segreti, id) sono da compilare nelle sedi sicure

---

## 5. Attività prioritarie post-stesura

Priorità immediate:

- compilare `14-SECRETS-INVENTORY` con i riferimenti reali
- eseguire e verificare i backup (`15`) prima del reinstall del Mac
- completare la checklist accessi (`13`) prima del reinstall
- compilare i valori reali di infrastruttura, DNS, VPS, database e Stripe

Priorità successive:

- avviare la Fase E (immagini) al ricevimento di logo e screenshot MT5
- sviluppare contenuti e UI del frontend
- completare integrazione pagamenti, webhook ed email end-to-end

---

## 6. Come aggiornare questo changelog

Regole:

- registrare qui ogni modifica significativa al Runbook
- aggiornare la tabella di stato dei capitoli quando cambiano versione o stato
- mantenere l'ordine cronologico inverso nello storico (più recente in alto)
- indicare sempre la data ISO

---

## 7. Changelog di questo documento

### v0.1
- creato il changelog globale del Runbook
- registrata la prima stesura completa di tutti i capitoli
- definite convenzioni di versionamento e attività prioritarie
