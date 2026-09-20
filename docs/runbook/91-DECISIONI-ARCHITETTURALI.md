# Progetto Hangar — Decisioni Architetturali
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento registra le decisioni architetturali di **Progetto Hangar** e le loro motivazioni.

Serve a:

- conservare la memoria del perché sono state prese certe scelte
- evitare di rimettere in discussione decisioni già valutate senza motivo
- fornire contesto a un operatore o a una IA
- tracciare l'evoluzione dell'architettura nel tempo

Formato:

- ogni decisione è registrata come ADR (Architecture Decision Record) sintetico
- ogni ADR ha: contesto, decisione, motivazione, alternative, conseguenze, stato

Questo file non contiene segreti.

---

## 2. Indice delle decisioni

| ID | Titolo | Stato |
|---|---|---|
| ADR-001 | Stack frontend Astro + React | Accettata |
| ADR-002 | Backend FastAPI | Accettata |
| ADR-003 | Database MongoDB Atlas | Accettata |
| ADR-004 | Backend su VPS, frontend su Cloudflare Pages | Accettata |
| ADR-005 | Monorepo su GitHub | Accettata |
| ADR-006 | Stripe come Merchant of Record | Accettata |
| ADR-007 | Hardening VPS (porta 134, no root, UFW, fail2ban) | Accettata |
| ADR-008 | Email: Fastmail + Resend | Accettata |
| ADR-009 | Rinvio di OpenNode (crypto) | Accettata |
| ADR-010 | Policy 2FA minima | Accettata |
| ADR-011 | Backtest come esperimenti storici replicabili | Accettata |
| ADR-012 | i18n con italiano primario | Accettata |
| ADR-013 | Prodotti digitali presentati come box fisici | Accettata |

---

## 3. ADR-001 — Stack frontend Astro + React

- **Contesto**: serve un sito vetrina premium, veloce, con parti interattive mirate.
- **Decisione**: usare Astro con isole React.
- **Motivazione**: Astro produce output leggero e veloce; React copre le parti interattive.
- **Alternative**: SPA React pura; altri framework.
- **Conseguenze**: ottime performance; necessità di gestire le isole interattive con criterio.
- **Stato**: Accettata.

---

## 4. ADR-002 — Backend FastAPI

- **Contesto**: serve un backend performante e ben strutturato per API e integrazioni.
- **Decisione**: usare FastAPI (Python).
- **Motivazione**: moderno, veloce, buona integrazione con MongoDB e servizi terzi, documentazione automatica.
- **Alternative**: altri framework backend.
- **Conseguenze**: ecosistema Python; gestione ambiente e servizio su VPS.
- **Stato**: Accettata.

---

## 5. ADR-003 — Database MongoDB Atlas

- **Contesto**: serve persistenza semplice e gestita in fase di avvio.
- **Decisione**: usare MongoDB Atlas (M0, Francoforte).
- **Motivazione**: gestito, costo iniziale nullo, buona integrazione, regione UE.
- **Alternative**: database self-hosted; database relazionale gestito.
- **Conseguenze**: limiti del piano gratuito da sorvegliare; dipendenza da servizio gestito.
- **Stato**: Accettata.

---

## 6. ADR-004 — Backend su VPS, frontend su Cloudflare Pages

- **Contesto**: si vuole controllo diretto sul backend e distribuzione globale del frontend.
- **Decisione**: backend su VPS Ubuntu, frontend su Cloudflare Pages.
- **Motivazione**: controllo diretto del backend; delivery edge veloce del frontend.
- **Alternative**: tutto su una piattaforma gestita; tutto self-hosted.
- **Conseguenze**: due binari di deploy distinti; VPS come punto di esecuzione da presidiare.
- **Stato**: Accettata.

---

## 7. ADR-005 — Monorepo su GitHub

- **Contesto**: progetto gestito da un solo operatore, con frontend, backend e documentazione.
- **Decisione**: usare un monorepo su GitHub.
- **Motivazione**: gestione unificata, documentazione insieme al codice, semplicità.
- **Alternative**: repository separati.
- **Conseguenze**: un unico punto di versionamento; attenzione a non versionare i segreti.
- **Stato**: Accettata.

---

## 8. ADR-006 — Stripe come Merchant of Record

- **Contesto**: vendita globale di prodotti digitali con complessità IVA.
- **Decisione**: usare Stripe Managed Payments come MoR.
- **Motivazione**: delega della fiscalità sulle transazioni, checkout affidabile, minore onere di compliance.
- **Alternative**: gestione IVA autonoma; altri MoR.
- **Conseguenze**: dipendenza da Stripe; termini di vendita coerenti con MoR; verifica coperture.
- **Stato**: Accettata.

---

## 9. ADR-007 — Hardening VPS

- **Contesto**: il backend è esposto pubblicamente e va protetto.
- **Decisione**: porta SSH custom `134`, root SSH disabilitato, utente `pilota`, UFW, fail2ban.
- **Motivazione**: ridurre superficie di attacco e tentativi di intrusione.
- **Alternative**: configurazione di default.
- **Conseguenze**: maggiore sicurezza; necessità di documentare bene accessi e recovery.
- **Stato**: Accettata.

---

## 10. ADR-008 — Email: Fastmail + Resend

- **Contesto**: servono posta di dominio e email transazionali.
- **Decisione**: Fastmail per la posta di dominio, Resend per le transazionali (sottodominio dedicato).
- **Motivazione**: separare posta umana e applicativa, migliorare deliverability e gestione.
- **Alternative**: un unico provider per entrambe.
- **Conseguenze**: due configurazioni DNS/autenticazione da gestire.
- **Stato**: Accettata.

---

## 11. ADR-009 — Rinvio di OpenNode (crypto)

- **Contesto**: interesse per pagamenti BTC/Lightning, ma con vincoli fiscali per persona fisica.
- **Decisione**: rinviare OpenNode.
- **Motivazione**: complessità fiscale/MoR non risolvibile prima della società; priorità al lancio con Stripe.
- **Alternative**: integrare subito crypto.
- **Conseguenze**: nessun pagamento crypto iniziale; da rivalutare con la società portoghese.
- **Stato**: Accettata (da rivedere).

---

## 12. ADR-010 — Policy 2FA minima

- **Contesto**: preferenza dell'operatore per evitare 2FA dove non obbligatoria.
- **Decisione**: evitare 2FA salvo obbligo di piattaforma; conservare con cura i recovery code dove attiva.
- **Motivazione**: semplicità di accesso; riduzione rischio blocco da dispositivi persi.
- **Alternative**: 2FA ovunque.
- **Conseguenze**: maggiore importanza di password robuste e conservazione sicura dei recovery data.
- **Stato**: Accettata.

---

## 13. ADR-011 — Backtest come esperimenti storici replicabili

- **Contesto**: necessità di comunicare risultati senza rischi legali.
- **Decisione**: presentare i backtest come esperimenti storici replicabili, con disclaimer.
- **Motivazione**: prudenza legale e credibilità; evitare promesse di rendimento.
- **Alternative**: presentazione promozionale dei risultati.
- **Conseguenze**: linguaggio vincolato; disclaimer obbligatori.
- **Stato**: Accettata.

---

## 14. ADR-012 — i18n con italiano primario

- **Contesto**: mercato iniziale italiano con ambizione internazionale.
- **Decisione**: italiano primario e completo; inglese secondario; spagnolo stub; fallback italiano.
- **Motivazione**: forza sul mercato primario ed espansione ordinata.
- **Alternative**: multilingua completo da subito.
- **Conseguenze**: struttura i18n predisposta; evitare traduzioni parziali pubblicate.
- **Stato**: Accettata.

---

## 15. ADR-013 — Prodotti digitali presentati come box fisici

- **Contesto**: prodotti digitali da rendere tangibili e premium.
- **Decisione**: rappresentare gli EA come box/oggetti fisici eleganti a tema aeronautico.
- **Motivazione**: percezione di valore e coerenza col brand artigianale.
- **Alternative**: presentazione puramente digitale/astratta.
- **Conseguenze**: dipendenza da asset visivi curati; necessità di logo e screenshot.
- **Stato**: Accettata.

---

## 16. Processo di gestione delle decisioni

Regole:

- ogni nuova decisione architetturale rilevante diventa un ADR
- gli ADR non si cancellano: si aggiornano di stato
- stati possibili: Proposta, Accettata, Superata, Da rivedere
- quando una decisione cambia, creare un nuovo ADR che la sostituisce e collegarlo

---

## 17. Decisioni da rivedere in futuro

Elenco delle decisioni con revisione prevista:

- ADR-009 (OpenNode) → rivedere dopo attivazione società portoghese
- introduzione di staging e CI/CD → valutare con la crescita
- upgrade del piano MongoDB → valutare con la crescita dei dati

---

## 18. Changelog

### v0.1
- creato il registro delle decisioni architetturali
- documentati gli ADR dal 001 al 013
- definito il processo di gestione e revisione delle decisioni
