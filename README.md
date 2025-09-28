# Guida all'utilizzo - Download Immagini da Excel

Questa applicazione ti permette di scaricare automaticamente immagini partendo da uno o più file Excel, organizzandole in cartelle e rinominandole in modo ordinato.

## 📦 Download

<p>
  <img src="https://img.icons8.com/fluency/28/000000/zip.png" alt="ZIP Icon" style="vertical-align:middle; margin-right:10px;"/>
  <a href="https://github.com/cache-it/excel-image-downloader-AM/archive/refs/heads/downloader-win.zip" style="font-size:18px; text-decoration:none; margin:auto;">
    excel-image-downloader-AM/downloader-win.zip
  </a> &nbsp;&nbsp;  (Windows)
</p>

<p>
  <img src="https://img.icons8.com/fluency/28/000000/zip.png" alt="ZIP Icon" style="vertical-align:middle; margin-right:10px;"/>
  <a href="https://github.com/cache-it/excel-image-downloader-AM/archive/refs/heads/downloader-linux.zip" style="font-size:18px; text-decoration:none; margin:auto;">
    excel-image-downloader-AM/downloader-linux.zip
  </a> &nbsp;&nbsp;  (Linux)
</p>

---

## 1. Contenuto della cartella fornita
All'interno della cartella che hai ricevuto troverai:

```
Cartella principale/
│
├── downloader-win.exe      # Programma da avviare (Windows)
├── downloader-linux        # Programma da avviare (Linux)
├── config.yaml             # File di configurazione
├── data/                   # Cartella dove inserire i file Excel
└── foto_download/          # Cartella dove saranno salvate le immagini
```

## 2. Preparazione dei file Excel
- Inserisci nella cartella `data/` uno o più file Excel (`.xlsx`) con i dati.
- Ogni file deve contenere **una colonna con i link delle immagini**, chiamata esattamente:

```
Foto
```

### Esempio di file Excel
| Grado | Codice Fiscale | Matricola | Cognome | Nome  | Foto                                   |
|-------|----------------|-----------|---------|-------|---------------------------------------|
| Ten.  | RSSMRA80A01H501U | 12345     | Rossi   | Mario | https://server.com/images/abc123.jpg  |
| Magg. | VRDLGI75T41H501T | 67890     | Verdi   | Luigi | https://server.com/pics/test456.png   |

⚠ **Attenzione:** Il nome della colonna deve essere scritto esattamente come indicato (`Foto`) per funzionare correttamente.

## 3. Avvio del programma

### Windows
1. Vai nella cartella principale del progetto.
2. Fai doppio click sul file:
   ```
   downloader.exe
   ```
3. Si aprirà una finestra nera (terminal).  
   Attendi che compaia il messaggio:
   ```
   🎉 Download di tutte le immagini completato!
   ```

### Linux
1. Apri il terminale nella cartella principale.
2. Rendi il file eseguibile (solo la prima volta):
   ```bash
   chmod +x downloader-linux
   ```
3. Avvia il programma:
   ```bash
   ./downloader-linux
   ```

## 4. Come funziona
- Il programma legge **tutti i file Excel presenti nella cartella `data/`**.
- Per ogni file Excel:
  1. Analizza i link nella colonna `Foto`.
  2. Scarica le immagini corrispondenti.
  3. Salva le immagini in una **sottocartella** all'interno di `foto_download/` con lo stesso nome del file Excel.

## 5. Nome dei file scaricati
Le immagini vengono rinominate automaticamente seguendo questa regola:
```
<codice_finale_link>_<ID progressivo>.<estensione>
```

Esempio:
- URL nel file Excel:  
  ```
  https://server.com/images/abc123.jpg
  ```
- Riga nel file Excel: 1

Output finale:
```
abc123_1.jpg
```

## 6. Esempio di risultato finale
Se nella cartella `data/` hai un file chiamato `militari_roma.xlsx`, il risultato sarà:

```
foto_download/
└── militari_roma/
    ├── abc123_1.jpg
    └── test456_2.png
```

## 7. Problemi comuni

| Problema                                   | Soluzione |
|-------------------------------------------|-----------|
| **Errore: Colonna non trovata**           | Verifica che la colonna con i link sia chiamata esattamente `Foto`. |
| **Nessuna immagine scaricata**            | Controlla che i link nel file Excel siano validi e accessibili. |
| **Il programma si chiude subito**         | Apri il terminale manualmente e lancia l'applicativo per leggere i messaggi di errore. |
| **Messaggio "File già esistente, salto"** | Significa che l'immagine è già stata scaricata e non viene riscaricata. |

## 8. Flusso di lavoro consigliato
1. Inserisci tutti i file Excel nella cartella `data/`.
2. Avvia il programma (`downloader-win.exe` su Windows o `./downloader-linux` su Linux).
3. Attendi la fine dell'elaborazione.
4. Trova tutte le immagini nella cartella `foto_download/`.

## 9. Note importanti
- Non modificare il file `config.yaml` a meno che non sia strettamente necessario.
- Mantieni separati i file Excel in `data/` per ogni batch di immagini.
- Le immagini già scaricate **non vengono sovrascritte**.

## 10. Supporto
In caso di problemi:
- Conserva eventuali messaggi di errore mostrati a video.
- Contatta l'amministratore fornendo:
  - Una copia del file Excel che non ha funzionato.
  - Uno screenshot del terminale con l'errore.
