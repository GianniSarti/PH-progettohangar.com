
# Backup Chiavi SSH — Checklist Operativa

## Obiettivo
Mettere al sicuro tutte le chiavi SSH necessarie per accedere ai sistemi e ai repository dopo reinstallazione del Mac o cambio macchina.

---

## 1. Verifica chiavi esistenti sul Mac

Controllare la cartella:

```bash
ls -la ~/.ssh
```

Individuare almeno:

- chiavi private
- chiavi pubbliche
- file `config`
- file `known_hosts`

Esempi comuni:

- `id_ed25519`
- `id_ed25519.pub`
- `config`
- `known_hosts`

---

## 2. Identificare quali chiavi sono critiche

Per ogni chiave, annotare:

- nome file
- uso
- servizio collegato
- obbligatorietà

Tabella esempio:

| Nome chiave | Tipo | Uso | Critica | Note |
|---|---|---|---|---|
| `id_ed25519` | privata | accesso VPS | sì | associata utente `pilota` |
| `id_ed25519.pub` | pubblica | chiave pubblica VPS/GitHub | sì | da conservare con la privata |
| `config` | configurazione | scorciatoie host SSH | sì | utile per ripristino rapido |
| `known_hosts` | fingerprint host | no | opzionale | rigenerabile |

---

## 3. Eseguire backup sicuro

Creare una cartella temporanea locale:

```bash
mkdir -p ~/Desktop/backup-ssh-progetto-hangar
cp -R ~/.ssh ~/Desktop/backup-ssh-progetto-hangar/
```

Poi:

- comprimere il backup
- cifrarlo
- salvarlo in almeno due luoghi distinti

Luoghi consigliati:

- disco esterno cifrato
- archivio locale cifrato
- eventuale vault sicuro offline

---

## 4. Regole di sicurezza

- non inviare mai le chiavi private via email
- non salvarle in note cloud non cifrate
- non inserirle nel repository Git
- non copiarle in chat
- verificare che i permessi siano corretti dopo il ripristino

Permessi tipici dopo restore:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/config
```

---

## 5. Test di ripristino minimo

Dopo reinstallazione o restore, verificare:

```bash
ssh -p 134 pilota@<IP_O_HOST_VPS>
```

Se usi alias nel file config:

```bash
ssh <ALIAS_HOST>
```

Confermare:

- connessione riuscita
- fingerprint coerente
- accesso effettivo al server

---

## 6. Stato checklist

- [ ] elenco chiavi completato
- [ ] backup locale creato
- [ ] backup cifrato creato
- [ ] copia su supporto secondario eseguita
- [ ] test di accesso VPS confermato
- [ ] test accesso GitHub confermato
