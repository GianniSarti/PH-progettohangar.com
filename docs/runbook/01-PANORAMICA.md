# Progetto Hangar — Panoramica Operativa
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Identità del progetto

**Progetto Hangar** è una boutique artigianale focalizzata sulla vendita di Expert Advisor per MetaTrader 5 (MT5), presentati come strumenti ad alta cura progettuale, con una forte identità di marca e un linguaggio visivo ispirato al mondo aeronautico.

L'obiettivo non è competere sul volume, ma sulla qualità percepita, sulla coerenza del brand e sulla fiducia costruita tramite presentazione professionale, test storici replicabili e comunicazione ordinata.

---

## 2. Obiettivo business

Obiettivo principale:

- vendere prodotti digitali MT5 a trader interessati a soluzioni curate e premium

Obiettivi secondari:

- costruire una presenza online credibile e distintiva
- differenziarsi dai competitor visivamente disordinati o troppo aggressivi
- presentare i prodotti come strumenti sviluppati con metodo e attenzione
- semplificare la compliance fiscale internazionale tramite Merchant of Record
- predisporre una base tecnica pulita, stabile e facilmente estendibile

---

## 3. Tipologia di utenti target

Utente target principale:

- trader MT5 che cerca Expert Advisor di qualità, presentati con trasparenza e tono professionale

Caratteristiche probabili:

- attenzione ai dettagli
- sensibilità alla credibilità del venditore
- interesse per risultati storici, purché comunicati correttamente
- possibile diffidenza verso siti di trading troppo rumorosi o poco seri
- preferenza per pagine pulite, dati leggibili e processo di acquisto lineare

---

## 4. Posizionamento del brand

Posizionamento desiderato:

- artigianale
- premium
- sobrio
- tecnico ma non freddo
- evocativo ma non teatrale
- aeronautico senza eccessi decorativi

Il brand deve trasmettere:

- precisione
- cura
- metodo
- affidabilità
- disciplina
- identità visiva distinta

Il brand **non** deve trasmettere:

- promessa facile di guadagno
- aggressività commerciale
- caos visivo
- effetto scam
- retorica da “guru del trading”

---

## 5. Offerta attuale

Prodotti già definiti:

- **PH Falchetto** — `€222`
- **PH Falco** — `€444`
- **Upgrade** — `€234`

Nota operativa:

- i prodotti sono digitali
- la presentazione visuale deve simularne una presenza fisica elegante, ad esempio tramite confezioni / box di prodotto
- gli SKU e i metadati Stripe risultano già creati

---

## 6. Approccio a test, risultati e compliance

Il progetto adotta una linea prudente nella presentazione dei risultati storici.

Formula concettuale da mantenere:

- non presentare i backtest come promessa di rendimento futuro
- presentarli come:
  - esperimenti storici replicabili
  - evidenze contestualizzate
  - documentazione tecnica del comportamento passato

Obblighi comunicativi:

- inserire disclaimer legali chiari
- evitare formulazioni che possano suggerire:
  - rendimento garantito
  - facilità di profitto
  - riduzione artificiale del rischio
- mantenere un linguaggio credibile, misurato e verificabile

---

## 7. Architettura tecnica decisa

### Stack applicativo
- frontend: Astro + React
- backend: FastAPI
- database: MongoDB Atlas

### Infrastruttura
- repository: GitHub monorepo
- frontend hosting: Cloudflare Pages
- backend hosting: VPS Ubuntu 24.04
- reverse proxy / TLS: nginx + HTTPS
- email dominio: Fastmail
- email transazionali: Resend
- pagamenti: Stripe Managed Payments
- DNS: Cloudflare

---

## 8. Stato infrastrutturale noto

Stato già confermato:

- VPS configurata e hardenizzata
- SSH su porta custom `134`
- utente operativo principale: `pilota`
- accesso root via SSH disabilitato
- UFW attivo
- fail2ban attivo
- API raggiungibile su:
  - `https://api.progettohangar.com`

Questo documento non sostituisce i file specialistici dedicati a VPS, nginx, DNS e deploy, ma ne fornisce il quadro generale.

---

## 9. Strategia di pagamento e fiscale

Soluzione scelta:

- **Stripe Managed Payments** in qualità di Merchant of Record

Motivazione:

- semplificare gestione IVA e conformità fiscale internazionale
- ridurre complessità operativa per vendita di beni digitali
- offrire checkout professionale e riconosciuto globalmente

Stato su crypto:

- integrazione OpenNode considerata utile come opzione futura
- attualmente rinviata
- motivo del rinvio:
  - complessità fiscale/operativa per persona fisica
  - preferenza per riaprire il tema dopo attivazione della società portoghese

---

## 10. Strategia linguistica

Lingue previste:

- italiano: primaria
- inglese: secondaria
- spagnolo: stub iniziale

Obiettivo:

- partire con contenuti forti in italiano
- predisporre l'architettura per espansione internazionale
- evitare da subito un multilingua confuso o incompleto

---

## 11. Direzione UI/UX

Direzione stilistica confermata:

- aeronautica vintage / biplano
- eleganza retro
- materiali percepiti come fisici
- pulizia visiva
- equilibrio
- assenza di affollamento grafico

Scelte visuali desiderate:

- packaging digitale presentato come oggetto fisico
- visual basati su screenshot MT5 armonizzati cromaticamente
- palette coerente con il brand
- tono premium e ordinato

Da acquisire per la fase visuale:

- logo ufficiale PH
- screenshot MT5
- eventuali preferenze finali su palette e texture

---

## 12. Priorità operative correnti

Ordine di lavoro attuale:

1. completare il Runbook
2. eseguire backup e inventario degli asset critici
3. mettere al sicuro accessi, chiavi e segreti prima del reinstall del Mac
4. proseguire con documentazione tecnica di dettaglio
5. avviare fase visuale appena disponibili logo e screenshot
6. sviluppare UI, contenuti e integrazioni applicative

---

## 13. Rischi attuali

Rischi principali identificati:

- perdita o dispersione di chiavi SSH durante reinstallazione del Mac
- perdita di token/segreti non ancora inventariati
- dipendenza eccessiva dalla memoria manuale dell'operatore
- possibile blocco operativo in caso di sostituzione macchina locale
- ritardi se non vengono raccolti per tempo logo e asset MT5

Mitigazione immediata:

- inventario completo dei segreti
- backup ordinato delle chiavi
- Runbook aggiornato
- salvataggio locale e offline verificato

---

## 14. Decisioni già prese

Decisioni ferme ad oggi:

- brand: Progetto Hangar
- focus: EA MT5 premium
- stack: Astro/React + FastAPI + MongoDB Atlas
- hosting frontend: Cloudflare Pages
- hosting backend: VPS Ubuntu
- pagamenti: Stripe Managed Payments
- email: Fastmail + Resend
- approccio compliance: disclaimer forti + presentazione prudente dei backtest
- OpenNode: posticipato
- policy personale: evitare 2FA dove non obbligatorio

---

## 15. Decisioni ancora aperte

Decisioni non ancora chiuse o dipendenti da file successivi:

- struttura finale delle pagine del sito
- testi completi marketing/prodotto
- schema dei webhook e post-purchase flow
- asset visuali definitivi
- procedura esatta di rilascio CI/CD
- routine di backup periodico documentata in dettaglio
- forma definitiva del catalogo internazionale EN/ES

---

## 16. Scopo di questo documento

Questo file serve come riferimento ad alto livello.

Una persona o una IA che legge questo documento deve capire rapidamente:

- che cos'è Progetto Hangar
- cosa è già stato deciso
- quale infrastruttura esiste già
- quali rischi sono prioritari
- quale ordine di lavoro seguire nelle prossime fasi

Per istruzioni operative dettagliate, consultare i file specialistici del Runbook.
