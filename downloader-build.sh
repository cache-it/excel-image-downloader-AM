#!/bin/bash

# ==============================================
# Script di build per PyInstaller - Ambiente Linux
# ==============================================

# Interrompe lo script in caso di errori
set -e

echo "🚀 Avvio build dell'applicativo Download Images..."

# 1. Attiva l'ambiente virtuale
if [ -d "venv" ]; then
    echo "🔹 Attivazione ambiente virtuale..."
    source venv/bin/activate
else
    echo "❌ Ambiente virtuale non trovato. Crealo con: python3 -m venv venv"
    exit 1
fi

# 2. Installa dipendenze da requirements.txt
REQ_FILE="src/requirements.txt"

if [ -f "$REQ_FILE" ]; then
    echo "🔹 Installazione pacchetti da $REQ_FILE..."
    pip install -r "$REQ_FILE"
else
    echo "❌ File requirements.txt non trovato in src/. Interruzione."
    exit 1
fi

# 3. Controlla se PyInstaller è installato
if ! command -v pyinstaller &> /dev/null
then
    echo "🔹 Installazione PyInstaller..."
    pip install pyinstaller
else
    echo "✔ PyInstaller già installato."
fi

# 4. Pulizia build precedenti
echo "🧹 Pulizia build precedenti..."
rm -rf build/
rm -f download_images.spec
rm -f downloader-linux

# 5. Creazione eseguibile
echo "🏗 Creazione eseguibile..."
pyinstaller --onefile \
  --icon=src/arrow.ico \
  --add-data "src/config.yaml:src" \
  --add-data "data:data" \
  --add-data "foto_download:foto_download" \
  --distpath . \
  src/main.py

# 6. Rinomina eseguibile finale
mv main downloader-linux

rm -f main.spec

# 7. Permessi di esecuzione
chmod +x downloader-linux

# 8. Conclusione
echo "🎉 Build completata!"
echo "L'eseguibile è pronto nella root directory con il nome: downloader-linux"
echo "Per avviarlo: ./downloader-linux"
