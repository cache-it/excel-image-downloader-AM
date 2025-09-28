# User Guide - Excel Image Downloader

This application allows you to automatically download images from one or more Excel files, organizing them into folders and renaming them in an orderly way.

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

## 1. Folder content provided
Inside the folder you received you will find:

```
Main folder/
│
├── downloader-win.exe      # Program to run (Windows)
├── downloader-linux        # Program to run (Linux)
├── config.yaml             # Configuration file
├── data/                   # Folder where you put the Excel files
└── foto_download/          # Folder where the downloaded images will be saved
```

## 2. Preparing the Excel files
- Place one or more Excel (`.xlsx`) files with data in the `data/` folder.
- Each file must contain **a column with the image links**, named exactly:

```
Foto
```

### Example of an Excel file
| Rank | Tax Code | ID Number | Last Name | First Name | Foto                                   |
|------|----------|-----------|-----------|------------|---------------------------------------|
| Ten. | RSSMRA80A01H501U | 12345 | Rossi | Mario | https://server.com/images/abc123.jpg  |
| Magg.| VRDLGI75T41H501T | 67890 | Verdi | Luigi | https://server.com/pics/test456.png   |

⚠ **Warning:** The column name must be exactly as indicated (`Foto`) to work correctly.

## 3. Running the program

### Windows
1. Go to the main folder of the project.
2. Double-click on the file:
   ```
   downloader.exe
   ```
3. A black terminal window will open.  
   Wait for the message to appear:
   ```
   🎉 Download of all images completed!
   ```

### Linux
1. Open the terminal in the main folder.
2. Make the file executable (first time only):
   ```bash
   chmod +x downloader-linux
   ```
3. Run the program:
   ```bash
   ./downloader-linux
   ```

## 4. How it works
- The program reads **all Excel files present in the `data/` folder**.
- For each Excel file:
  1. It analyzes the links in the `Foto` column.
  2. Downloads the corresponding images.
  3. Saves the images in a **subfolder** inside `foto_download/` with the same name as the Excel file.

## 5. Naming of downloaded files
The images are automatically renamed following this rule:
```
<final_link_code>.<extension>
```

Example:
- URL in the Excel file:  
  ```
  https://server.com/images/abc123.jpg
  ```

Final output:
```
abc123.jpg
```

## 6. Example of final result
If there is a file named `militari_roma.xlsx` in the `data/` folder, the result will be:

```
foto_download/
└── militari_roma/
    ├── abc123.jpg
    └── test456.png
```

## 7. Common issues

| Problem                                   | Solution |
|------------------------------------------|----------|
| **Error: Column not found**              | Verify that the column with the links is named exactly `Foto`. |
| **No images downloaded**                 | Check that the links in the Excel file are valid and accessible. |
| **The program closes immediately**       | Open the terminal manually and run the program to read the error messages. |
| **Message "File already exists, skipping"** | It means that the image has already been downloaded and will not be downloaded again. |

## 8. Recommended workflow
1. Place all Excel files in the `data/` folder.
2. Run the program (`downloader-win.exe` on Windows or `./downloader-linux` on Linux).
3. Wait for the processing to complete.
4. Find all the images in the `foto_download/` folder.

## 9. Important notes
- Do not modify the `config.yaml` file unless strictly necessary.
- Keep separate Excel files in `data/` for each batch of images.
- Already downloaded images **will not be overwritten**.

## 10. Support
In case of problems:
- Save any error messages displayed on the screen.
- Contact the administrator providing:
  - A copy of the Excel file that didn't work.
  - A screenshot of the terminal showing the error.
