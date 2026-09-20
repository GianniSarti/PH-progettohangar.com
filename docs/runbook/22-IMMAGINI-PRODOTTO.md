# Progetto Hangar — Immagini Prodotto
Versione: 0.1  
Stato: Bozza iniziale  
Ultimo aggiornamento: 2026-09-20

---

## 1. Scopo del documento

Questo documento descrive la strategia per le immagini di prodotto di **Progetto Hangar**.

Serve a:

- definire come rappresentare visivamente prodotti digitali
- descrivere l'uso dei box/oggetti fisici e degli screenshot MT5
- garantire coerenza visiva e qualità
- fornire linee guida per la generazione delle immagini
- permettere a un operatore o a una IA di produrre immagini coerenti

Questo file non contiene segreti.

---

## 2. Sfida principale

Problema:

- i prodotti sono digitali (Expert Advisor)
- vanno presentati in modo tangibile e premium

Soluzione:

- rappresentare ogni prodotto come un oggetto fisico elegante (box/confezione)
- integrare screenshot MT5 armonizzati cromaticamente
- collocare i prodotti in un immaginario aeronautico coerente

---

## 3. Concept visivo

Concept:

- ogni EA è una "confezione" da boutique aeronautica
- estetica retro-elegante e artigianale
- materiali percepiti come reali (carta, metallo, legno, pelle)

Principio:

- l'immagine deve comunicare cura, qualità e valore
- coerenza con `21-BRAND-ASSETS`

---

## 4. Tipologie di immagini

| Tipo | Scopo | Note |
|---|---|---|
| Box prodotto | rappresentazione principale del prodotto | uno per EA |
| Screenshot MT5 | evidenza tecnica/estetica | colori armonizzati |
| Immagini di dettaglio | particolari e materiali | opzionali |
| Immagini contestuali | ambientazione aeronautica | hero/sezioni |
| Icone/badge | elementi UI di supporto | coerenti con brand |

---

## 5. Box di prodotto

Linee guida per i box:

- design coerente per tutti i prodotti, con differenziazione per livello
- PH Falchetto e PH Falco riconoscibili come linea, ma distinti
- Upgrade rappresentato in modo coerente con il concetto di passaggio

Elementi tipici del box:

- logo PH
- nome prodotto
- riferimenti aeronautici sobri
- materiali e finiture eleganti

Nota:

- differenziare i livelli con eleganza (es. finiture, dettagli), non con eccesso

---

## 6. Screenshot MT5

Uso degli screenshot:

- mostrare grafici e risultati in modo coerente col brand
- armonizzare i colori del grafico MT5 con la palette del brand

Linee guida:

- personalizzare i colori del grafico MT5 (sfondo, candele, linee)
- mantenere leggibilità e pulizia
- evitare screenshot caotici o sovraccarichi

Nota:

- gli screenshot reali sono da fornire da parte dell'operatore
- i colori personalizzati vanno definiti e documentati

Coerenza legale:

- eventuali risultati mostrati seguono `19-DISCLAIMER-E-COMPLIANCE`

---

## 7. Palette applicata alle immagini

Principi:

- usare la palette di brand (vedi `21-BRAND-ASSETS`)
- coerenza cromatica tra box, screenshot e sfondi
- accenti usati con misura

Nota:

- definire i colori esatti del grafico MT5 una volta consolidata la palette

---

## 8. Specifiche tecniche delle immagini

Linee guida tecniche:

- alta qualità e nitidezza
- formati ottimizzati per il web
- versioni responsive per diverse dimensioni
- peso ottimizzato per le performance
- coerenza di proporzioni tra prodotti

Formati consigliati:

```text
Web: WebP / PNG ottimizzato
Sorgenti: conservare i file editabili
Risoluzione: adeguata a hero e schede prodotto
```

---

## 9. Organizzazione delle immagini

Struttura consigliata:

```text
assets/products/
  falchetto/
    box/
    mt5/
    details/
  falco/
    box/
    mt5/
    details/
  upgrade/
    box/
    ...
```

Principi:

- una cartella per prodotto
- separazione per tipologia di immagine
- nomi file chiari e coerenti

---

## 10. Processo di creazione delle immagini (Fase E)

Sequenza operativa:

1. ricevere logo PH e screenshot MT5
2. definire palette e colori del grafico MT5
3. creare i box di prodotto
4. armonizzare gli screenshot MT5
5. creare eventuali immagini contestuali/hero
6. ottimizzare i file per il web
7. organizzare e versionare gli asset
8. integrare nel frontend
9. aggiornare stato e changelog

Prerequisiti bloccanti:

- logo PH
- screenshot MT5

---

## 11. Coerenza con il frontend

Le immagini devono integrarsi con:

- schede prodotto
- sezioni hero
- pagine marketing
- eventuali anteprime social

Riferimento:

- `05-FRONTEND`, `18-PRODOTTI-E-SKU`

Principio:

- immagini coerenti rafforzano la percezione premium

---

## 12. Superfici critiche

Punti di attenzione:

- immagini incoerenti tra prodotti
- screenshot MT5 caotici o non armonizzati
- immagini troppo pesanti che rallentano il sito
- perdita dei file sorgente
- risultati mostrati senza disclaimer

Mitigazioni:

- linee guida visive chiare
- ottimizzazione dei file
- backup dei sorgenti
- coerenza con brand e compliance

---

## 13. Assunzioni correnti

Assunzioni valide alla stesura:

- prodotti digitali presentati come box fisici
- screenshot MT5 armonizzati con la palette
- tema aeronautico vintage
- logo e screenshot ancora da fornire

Se queste assunzioni cambiano, aggiornare il documento.

---

## 14. Attività aperte

Attività da completare:

- ricevere logo PH e screenshot MT5
- definire i colori del grafico MT5
- creare i box di prodotto
- armonizzare gli screenshot
- ottimizzare e organizzare gli asset
- integrare le immagini nel frontend

---

## 15. Stato del capitolo

Questo capitolo è da considerarsi:

- valido come strategia per le immagini prodotto
- bloccato nella parte operativa in attesa di logo e screenshot
- da aggiornare durante la Fase E

Dipendenze correlate:

- `05-FRONTEND`
- `18-PRODOTTI-E-SKU`
- `19-DISCLAIMER-E-COMPLIANCE`
- `21-BRAND-ASSETS`

---

## 16. Changelog

### v0.1
- definito il concept visivo per prodotti digitali come box fisici
- descritte tipologie, screenshot MT5 e specifiche tecniche
- definiti processo di creazione (Fase E) e organizzazione asset
- registrate superfici critiche e attività aperte
