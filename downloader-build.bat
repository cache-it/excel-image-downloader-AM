@echo off
echo Attivazione ambiente virtuale...
call .venv\Scripts\activate

echo Costruzione eseguibile...
pyinstaller --onefile --icon=src/arrow.ico --add-data "src/config.yaml;src" --add-data "data;data" --add-data "foto_download;foto_download" --distpath . src/main.py

echo Fatto! Eseguibile disponibile nella root come main.exe
pause
