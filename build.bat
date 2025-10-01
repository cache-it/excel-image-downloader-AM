@echo off
SETLOCAL ENABLEEXTENSIONS

echo ==============================================
echo  Build Script per PyInstaller - Ambiente Windows
echo ==============================================
echo.

:: 1. Controllo ambiente virtuale
IF NOT EXIST venv (
    echo ❌ Ambiente virtuale non trovato. Crealo con:
    echo python -m venv venv
    pause
    exit /b 1
)

echo 🔹 Attivazione ambiente virtuale...
call venv\Scripts\activate

:: 2. Installazione dipendenze da requirements.txt
IF EXIST src\requirements.txt (
    echo 🔹 Installazione pacchetti da requirements.txt...
    pip install -r src\requirements.txt
) ELSE (
    echo ❌ File requirements.txt non trovato nella cartella src.
    pause
    exit /b 1
)

:: 3. Controllo installazione PyInstaller
where pyinstaller >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo 🔹 Installazione PyInstaller...
    pip install pyinstaller
) ELSE (
    echo ✔ PyInstaller già installato.
)

:: 4. Pulizia build precedenti
echo 🧹 Pulizia build precedenti...
IF EXIST build rmdir /S /Q build
IF EXIST download_images.spec del /F /Q download_images.spec
IF EXIST downloader-win.exe del /F /Q downloader-win.exe

:: 5. Costruzione eseguibile
echo 🏗 Creazione eseguibile...
pyinstaller --onefile --icon=src/arrow.ico --add-data "src/config.yaml;src" --add-data "data;data" --add-data "foto_download;foto_download" --distpath . src/main.py

:: 6. Rinomina l'eseguibile finale
rename download_images.exe downloader-win.exe

echo.
echo 🎉 Build completata!
echo L'eseguibile e' pronto nella root directory con il nome: downloader-win.exe
echo Per eseguirlo, fai doppio click oppure lancia: downloader-win.exe
pause
