pip install pyinstaller

# Rebrandly GUI
cd C:Path\to\folder\with\script
pyinstaller --onefile --noconsole Rebrandly-App-GUI.py

# Rebrandly Clipboard
cd C:Path\to\file\Rebrandly-Clipboard.py
pyinstaller --onefile Rebrandly-App-GUI.py

# Rebrandly Text Integration
cd C:Path\to\folder\with\script
pyinstaller --onefile --noconsole Rebrandly-Test-Integration.py
pyinstaller --onefile --noconsole setup.py
