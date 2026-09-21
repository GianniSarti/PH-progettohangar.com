# PASSAGGIO CONSEGNE — Progetto Hangar — Fase E (Immagini e Identità Visiva)
Destinatario: nuova istanza IA incaricata della Fase E  
Redatto da: istanza precedente  
Data: 2026-09-21  
Lingua di lavoro: Italiano (rispondi sempre e solo in italiano)

---

## 0. Leggimi per primo — Ordine delle operazioni

Benvenuta. Questo documento è la prima cosa che ricevi. Segui questo ordine:

1. Leggi per intero questo documento di consegne.
2. Consulta il Runbook del progetto su GitHub (link al punto 3), in particolare, in quest'ordine:
   - `docs/runbook/01-PANORAMICA.md`
   - `docs/runbook/21-BRAND-ASSETS.md`
   - `docs/runbook/22-IMMAGINI-PRODOTTO.md`
   - `docs/runbook/18-PRODOTTI-E-SKU.md`
   - `docs/runbook/19-DISCLAIMER-E-COMPLIANCE.md`
3. Chiedi a Gianni i materiali elencati al punto 6 (prerequisiti bloccanti) se non te li ha già forniti.
4. Non iniziare a generare immagini prima di aver analizzato l'esistente e allineato palette e concept (Fasi E.1–E.3).
5. Procedi con il piano operativo (punto 8), un passo per volta, chiedendo validazione a Gianni ai punti di approvazione.

Regola di comunicazione: proponi, non dare per scontato. Gianni approva prima di procedere ai passaggi chiave.

---

## 1. Chi è l'utente

- Nome: Gianni Sarti, founder di Progetto Hangar.
- Preferenze: risposte in italiano, tono concreto, niente entusiasmo artificiale.
- Metodo di lavoro: un passo per volta, con validazione esplicita ai punti chiave.
- Convenzione documenti: quando produci capitoli/documenti Markdown destinati al repo, usali in code box con QUATTRO backtick (perché possono contenere a loro volta blocchi da tre backtick).

---

## 2. Cos'è Progetto Hangar

Boutique artigianale di Expert Advisor (bot di trading) per MetaTrader 5 (MT5). Vende qualità, non quantità. Identità visiva a tema aeronautico/biplani, elegante, retro, materica, mai kitsch né affollata. Prodotti digitali presentati come oggetti fisici (box da boutique).

Prodotti:
- PH Falchetto — €222 (fascia base)
- PH Falco — €444 (fascia superiore)
- Upgrade — €234 (passaggio tra livelli)

---

## 3. Base di conoscenza già pronta (Runbook)

Il progetto ha un Runbook completo (26 documenti + 2 allegati) già su GitHub:

- Repo: https://github.com/GianniSarti/PH-progettohangar.com
- Percorso Runbook: `docs/runbook/`
- Indice di ingresso: `docs/runbook/README.md` e `docs/runbook/00-INDICE.md`

Questo è la tua memoria di progetto. Se un dubbio è coperto lì, consulta il Runbook prima di chiedere.

---

## 4. Il tuo compito: la Fase E

Definire e produrre l'identità visiva e le immagini del brand e dei prodotti, coerenti con lo stile già approvato, integrando il richiamo al trading dove manca.

Obiettivo: immagini che identifichino il brand, con la commistione riuscita tra aeronautica, officina/hangar e trading.

---

## 5. Stato attuale e punto di partenza

- Stile e palette colori: già approvati in linea di massima (non irrevocabili, si possono affinare).
- Esistono immagini già create con Nano Banana Pro (NBP) e i relativi prompt: Gianni te li fornirà.
  - Alcune sono ottime.
  - Alcune sono molto buone ma prive di richiamo al trading: vanno integrate o affiancate a immagini adatte.
- Palette: Gianni aveva raccolto i colori in un artifact su claude.ai NON accessibile pubblicamente. Chiedi a Gianni i valori HEX esatti, oppure estraili dalle immagini approvate e faglieli validare.

Strumenti a tua disposizione:
- Analisi immagini/file (per valutare le immagini esistenti e quelle nuove).
- Generazione immagini (motore tipo nano banana). Puoi sia analizzare le NBP esistenti sia generarne di nuove.
- Ricerca web (se serve riferimenti su font stencil militari, strumenti d'epoca, ecc.).

Nota sul flusso NBP: valuta tu, dopo aver visto gli asset, se mantenere le immagini NBP esistenti (approccio ibrido) o rigenerare. Criterio: coerenza con lo stile approvato + capacità di includere il richiamo al trading + controllo sui mockup dei box. Esito atteso più probabile: ibrido (tieni le NBP approvate per hero/contesto, genera/componi box e elementi trading dove mancano). Decisione finale a Gianni.

---

## 6. Prerequisiti bloccanti (chiedili a Gianni se mancano)

- Immagini NBP già create + i prompt che le hanno generate (via GitHub o incollate in chat: vedi punto 7).
- Logo PH (file sorgente, vettoriale se possibile).
- Screenshot MT5 reali (per gli elementi trading e i grafici).
- Valori HEX della palette approvata (o autorizzazione a estrarli dalle immagini).
- Specifiche di differenziazione tra i tre prodotti (come distinguere visivamente Falchetto, Falco, Upgrade).

---

## 7. Come Gianni ti fornirà i materiali

Modalità consigliata: caricare immagini NBP + prompt in una cartella dedicata del repo, ad esempio `docs/runbook/allegati/asset-nbp/` (immagini + un file di testo/markdown con i prompt associati, uno per immagine). Così restano versionati e tu puoi analizzarli per URL/percorso.

In alternativa Gianni può incollarli in chat. Concorda con lui la modalità all'inizio. Se usate il repo, chiedi il link diretto ai file.

---

## 8. Piano operativo Fase E

E.0 — Prerequisiti
- Raccogli tutti i materiali del punto 6.

E.1 — Intake e analisi dell'esistente
- Analizza ogni immagine NBP: stile, palette, composizione, presenza/assenza del richiamo al trading, livello qualitativo.
- Classifica ciascuna: APPROVATA / DA INTEGRARE o AFFIANCARE / DA SCARTARE.
- Produci un "registro asset" (tabella) con il verdetto per ogni immagine.
- Fai validare il registro a Gianni.

E.2 — Sistema visivo
- Consolida palette (valori HEX), motivi aeronautici ricorrenti, direzione tipografica.
- Definisci lo schema colori del grafico MT5 armonizzato con la palette (candele verdi/rosse come unici colori brillanti — vedi concept al punto 9).

E.3 — Decisione su NBP nel flusso
- Proponi a Gianni: ibrido o rigenerazione. Motiva. Attendi conferma.

E.4 — Produzione asset per prodotto
- Box PH Falchetto, box PH Falco, rappresentazione Upgrade (coerenti come linea, distinti per livello).
- Screenshot MT5 armonizzati cromaticamente.
- Immagini hero/contestuali mancanti (in primis l'immagine-firma dell'altimetro, punto 9).

E.5 — Ciclo iterativo
- genera → analizza → correggi → fai approvare. Non accumulare troppe varianti senza validazione.

E.6 — Ottimizzazione e organizzazione
- Formati web ottimizzati, versioni responsive, struttura cartelle come da `22-IMMAGINI-PRODOTTO.md`.
- Conserva sempre i file sorgente.

E.7 — Integrazione e tracciamento
- Prepara gli asset per il frontend.
- Aggiorna `docs/runbook/99-CHANGELOG.md` e, se serve, `21-BRAND-ASSETS.md` / `22-IMMAGINI-PRODOTTO.md` con le decisioni prese.

---

## 9. Concept visivi guida (indicazioni dirette di Gianni)

Questi due concept sono il cuore dell'identità. Trattali come riferimento primario.

CONCEPT 1 — Immagine-firma del brand (priorità massima)
- Soggetto: un altimetro aeronautico "vissuto" (weathered, usato, con segni del tempo) posato su un banco di lavoro dell'hangar/officina.
- Dettaglio chiave: nello schermo rotondo e convesso dello strumento si riflettono le candele del trading, verdi e rosse.
- Ambiente: legno, metallo, lampadine a filamento, strumenti d'epoca. Atmosfera calda e materica.
- Regola cromatica forte: verde e rosso delle candele sono gli UNICI colori brillanti nella scena; tutto il resto è in toni caldi/desaturati (legno, ottone, metallo brunito, luce ambrata dei filamenti).
- Perché conta: è la fusione perfetta tra aeronautica, officina e trading. È l'immagine identitaria del brand.

CONCEPT 2 — Contaminazione aeronautica/trading (esempio di linguaggio)
- Riferimento: il fianco della fusoliera di un caccia vicino alla cabina, dove un tempo si segnavano gli aerei abbattuti (kill markings).
- Reinterpretazione: invece degli abbattimenti, si segnano i take profit colpiti.
- Elementi: scritta "TAKE PROFIT" in caratteri stencil militari; sotto, file di "X" verdi che compilano righe da 10 X per riga.
- Uso: è un esempio del tipo di contaminazione visiva desiderata; puoi proporne altre sulla stessa logica.

Linea guida trasversale: aeronautica + officina/hangar + trading, con eleganza retro e ordine. Il trading entra come accento cromatico e simbolico (candele, take profit), mai come estetica "urlata".

---

## 10. Vincoli di compliance sulle immagini

- Le immagini che mostrano risultati/grafici non devono suggerire guadagni garantiti.
- I risultati storici sono "esperimenti storici replicabili" (vedi `19-DISCLAIMER-E-COMPLIANCE.md`).
- Evita nelle grafiche claim numerici che promettano rendimenti. Le candele/take profit come elemento estetico-simbolico sono ok; una promessa di profitto no.

---

## 11. Cosa NON fare

- Non pubblicare/consegnare immagini prima della validazione di Gianni ai punti chiave.
- Non introdurre estetica kitsch o affollata.
- Non usare font senza verificarne la licenza (specie stencil militari).
- Non perdere i file sorgente.
- Non inserire mai segreti nel repo (non ti servono per la Fase E, ma vale come regola generale del progetto).

---

## 12. Punti aperti da confermare con Gianni a inizio lavoro

- Modalità di consegna dei materiali (repo vs chat).
- Valori HEX della palette (o autorizzazione a estrarli).
- Differenziazione visiva tra i tre prodotti.
- Se, dopo l'analisi, si adotta flusso ibrido o rigenerazione.

---

## 13. Chiusura della Fase E e passaggio successivo

Quando le immagini sono validate:
- aggiorna il Runbook (changelog + capitoli brand/immagini) con le decisioni finali;
- prepara un breve documento di passaggio consegne per la fase seguente (probabile: contenuti e UI del frontend), perché a fine Fase E il tuo contesto sarà molto consumato e la fase successiva andrà affidata a un'istanza fresca.

Modello del progetto: la memoria vive nei documenti, le istanze sono sostituibili. Ogni fase pesante = istanza fresca + consegne aggiornate.

---

## 14. Riepilogo essenziale (se leggi solo una cosa)

- Sei incaricata SOLO della Fase E: identità visiva e immagini.
- Base di conoscenza: Runbook su GitHub (`docs/runbook/`).
- Prima analizza l'esistente e allinea palette/concept, POI genera.
- Immagine-firma: altimetro vissuto su banco d'officina, schermo convesso che riflette candele verdi/rosse, uniche note brillanti in un ambiente di legno, metallo e filamenti.
- Valida con Gianni ai punti chiave. Rispondi in italiano.
