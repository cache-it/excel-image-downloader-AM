import os
import sys
import requests
import pandas as pd
import yaml
from glob import glob
from urllib.parse import urlparse

# -----------------------------
# Funzione per ottenere il path dei file (compatibile con PyInstaller)
# -----------------------------
def resource_path(relative_path):
    """Ottiene il path assoluto a un file, compatibile sia in sviluppo che da .exe"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# -----------------------------
# Carica configurazioni
# -----------------------------
config_path = resource_path("src/config.yaml")
with open(config_path, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# ✅ NON usare resource_path per queste cartelle esterne
DATA_FOLDER = config["data_folder"]           # Esempio: "data"
OUTPUT_FOLDER = config["output_folder"]       # Esempio: "foto_download"
URL_COLUMN = config["url_column"]             # Es. "url: image"
NAME_COLUMN = config["name_column"]           # Es. "image_name"

# -----------------------------
# Crea cartella di output se non esiste
# -----------------------------
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------
# Trova tutti i file .xlsx nella cartella data/
# -----------------------------
excel_files = glob(os.path.join(DATA_FOLDER, "*.xlsx"))

if not excel_files:
    print(f"❌ Nessun file .xlsx trovato nella cartella '{DATA_FOLDER}'")
    sys.exit(1)

print(f"📂 Trovati {len(excel_files)} file Excel nella cartella '{DATA_FOLDER}':")
for file in excel_files:
    print(f"   - {os.path.basename(file)}")

# -----------------------------
# Funzione per estrarre il codice finale dal link - NOT USED
# -----------------------------
def get_last_code_from_url(url: str) -> str:
    """
    Estrae l'ultima parte dell'URL dopo l'ultimo '/' senza estensione.
    Esempio: https://server.com/path/img123.jpg -> img123
    """
    parsed_url = urlparse(url)
    base_name = os.path.basename(parsed_url.path)  # es: img123.jpg
    code = os.path.splitext(base_name)[0]          # es: img123
    return code

# -----------------------------
# Funzione per processare un singolo file Excel
# -----------------------------
def process_excel_file(excel_path: str):
    file_name = os.path.splitext(os.path.basename(excel_path))[0]
    print(f"\n📖 Elaborazione file: {file_name}")

    # Sottocartella per questo Excel
    file_output_folder = os.path.join(OUTPUT_FOLDER, file_name)
    os.makedirs(file_output_folder, exist_ok=True)

    # Leggi l'Excel
    try:
        df = pd.read_excel(excel_path)
    except Exception as e:
        print(f"❌ Errore nella lettura di {excel_path}: {e}")
        return

    # Controlla che la colonna URL esista
    if URL_COLUMN not in df.columns:
        print(f"❌ Colonna '{URL_COLUMN}' mancante in {excel_path}")
        return

    # Controlla che la colonna NAME esista
    if NAME_COLUMN not in df.columns:
        print(f"❌ Colonna '{NAME_COLUMN}' mancante in {excel_path}")
        return

    # Scarica le immagini
    for index, row in df.iterrows():
        url = str(row[URL_COLUMN]).strip()
        name = str(row[NAME_COLUMN]).strip()

        if not url or url.lower() == "nan":
            print(f"⚠ Riga {index + 2}: URL vuoto, salto...")
            continue

        # Estrai estensione dall'URL
        ext = os.path.splitext(urlparse(url).path)[-1].lower()
        if ext not in [".jpg", ".jpeg", ".png"]:
            ext = ".jpg"  # default se non riconosciuta

        # Estrai codice finale
        # last_code = get_last_code_from_url(url)
        last_code = name
        filename = f"{last_code}{ext}"
        output_path = os.path.join(file_output_folder, filename)

        # Evita sovrascrittura
        if os.path.exists(output_path):
            print(f"⚠ File già esistente, salto: {output_path}")
            continue

        try:
            print(f"⬇ Scaricando immagine #{index + 1} da {url}...")
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                with open(output_path, "wb") as img_file:
                    img_file.write(response.content)
                print(f"✔ Salvata: {output_path}")
            else:
                print(f"✖ Errore HTTP {response.status_code} per {url}")
        except Exception as e:
            print(f"✖ Errore nel download di {url}: {e}")

    print(f"✅ Completato file: {file_name}")

# -----------------------------
# Processo principale
# -----------------------------
for excel_file in excel_files:
    process_excel_file(excel_file)

print("\n🎉 Download di tutte le immagini completato!")
