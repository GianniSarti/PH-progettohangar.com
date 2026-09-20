# Progetto Hangar — Brand Assets
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive l'identità visiva e gli asset di brand di **Progetto Hangar**.

Serve a:

- definire il linguaggio visivo del brand
- documentare logo, palette, tipografia e stile
- garantire coerenza visiva su tutti i materiali
- fornire linee guida per la creazione di nuovi asset
- permettere a un operatore o a una IA di produrre grafiche coerenti

Questo file non contiene segreti.

---

## 2. Identità del brand

Nome:

- Progetto Hangar

Concetto:

- boutique artigianale di Expert Advisor MT5
- immaginario aeronautico e dei biplani
- eleganza retro e cura artigianale

Personalità del brand:

- preciso
- affidabile
- disciplinato
- elegante
- tecnico ma accessibile

---

## 3. Tema visivo

Tema centrale:

- aeronautica vintage / biplani

Stile:

- retro-elegante
- pulito
- materico (percezione di materiali reali)
- ordinato, mai affollato

Da evitare:

- kitsch
- sovraccarico visivo
- estetica aggressiva o da "trading urlato"
- eccesso di elementi decorativi

---

## 4. Logo

Elemento:

- logo PH a tema biplano

Stato:

- da fornire da parte dell'operatore (Gianni)

Linee guida d'uso (da consolidare quando il logo è disponibile):

- spazio di rispetto attorno al logo
- versioni per sfondi chiari e scuri
- dimensioni minime di leggibilità
- versione principale e versione ridotta/icona

Nota:

- il logo è prerequisito per avviare la fase visuale (Fase E)

---

## 5. Palette colori

Direzione cromatica (da consolidare):

- toni sobri ed eleganti
- richiami aeronautici vintage
- buon contrasto per leggibilità

Struttura consigliata della palette:

```text
Primario:      <COLORE_PRINCIPALE>
Secondario:    <COLORE_SECONDARIO>
Accento:       <COLORE_ACCENTO>
Neutri chiari: <TONI_CHIARI>
Neutri scuri:  <TONI_SCURI>
```

Principi:

- palette contenuta e coerente
- usare l'accento con parsimonia
- garantire contrasto sufficiente per accessibilità

Nota:

- i valori esatti (HEX) vanno definiti e documentati

---

## 6. Tipografia

Direzione tipografica (da consolidare):

- carattere elegante e leggibile
- eventuale abbinamento tra un font caratterizzante per i titoli e uno pulito per il testo

Struttura consigliata:

```text
Titoli:  <FONT_TITOLI>
Testo:   <FONT_TESTO>
```

Principi:

- gerarchia tipografica chiara
- leggibilità su tutti i dispositivi
- coerenza con il tono retro-elegante

Nota:

- verificare licenze d'uso dei font scelti

---

## 7. Stile grafico

Elementi stilistici:

- riferimenti aeronautici usati con misura
- eventuali texture materiche leggere
- linee pulite e composizione ordinata
- uso generoso dello spazio bianco/negativo

Principio:

- l'eleganza nasce dall'ordine e dalla misura, non dall'abbondanza

---

## 8. Tono di voce

Tono verbale coerente con il visual:

- professionale
- misurato
- curato
- rassicurante senza essere promozionale
- tecnico ma comprensibile

Da evitare:

- toni sensazionalistici
- promesse
- linguaggio da "guru"

Riferimento:

- coerenza con `19-DISCLAIMER-E-COMPLIANCE`

---

## 9. Organizzazione degli asset

Struttura consigliata per gli asset di brand nel repository:

```text
assets/brand/
  logo/
  colors/
  fonts/
  icons/
  textures/
  templates/
```

Principi:

- asset organizzati e versionati
- formati appropriati (vettoriale dove possibile)
- nomi file chiari e coerenti

---

## 10. Formati degli asset

Linee guida sui formati:

- logo: preferibilmente vettoriale (SVG) più esportazioni PNG
- immagini: formati ottimizzati per il web
- icone: vettoriali quando possibile
- mantenere versioni sorgente modificabili

Principio:

- conservare sempre il sorgente oltre all'esportazione

---

## 11. Coerenza tra i materiali

Il brand deve restare coerente su:

- sito web
- immagini prodotto
- email
- eventuali materiali social o marketing

Riferimenti:

- immagini prodotto: `22-IMMAGINI-PRODOTTO`
- frontend: `05-FRONTEND`

Principio:

- ogni materiale deve essere riconoscibile come Progetto Hangar

---

## 12. Superfici critiche

Punti di attenzione:

- uso incoerente del logo
- palette non rispettata
- font non licenziati
- estetica che scivola nel kitsch
- perdita dei file sorgente

Mitigazioni:

- linee guida chiare
- organizzazione e backup degli asset
- verifica delle licenze
- revisione della coerenza visiva

---

## 13. Assunzioni correnti

Assunzioni valide alla stesura:

- tema aeronautico vintage / biplani
- stile retro-elegante e pulito
- logo ancora da fornire
- palette e tipografia da consolidare

Se queste assunzioni cambiano, aggiornare il documento.

---

## 14. Attività aperte

Attività da completare:

- ricevere e integrare il logo PH
- definire la palette con valori HEX
- scegliere e licenziare la tipografia
- consolidare le linee guida d'uso
- organizzare e versionare gli asset

---

## 15. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come direzione di brand
- incompleto finché logo, palette e font non sono definiti
- prerequisito per la fase visuale

Dipendenze correlate:

- `05-FRONTEND`
- `20-I18N`
- `22-IMMAGINI-PRODOTTO`

---

## 16. Changelog

### v0.1
- definiti tema, personalità e stile del brand
- descritte linee guida per logo, palette, tipografia e asset
- definiti tono di voce e organizzazione degli asset
- registrate superfici critiche e attività aperte
