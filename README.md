# Recoil reducer

### An app that helps you deal with recoil in shooters. Uses win32api for mouse manipulations.
 
## Building

```bash
>  pip install -r requirements.txt
```

```bash
>  python -m PyInstaller --onefile --hidden-import=pywintypes --add-data="./settings;settings" main.py
```

Then open `dist` folder