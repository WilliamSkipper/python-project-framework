import sys
import os

def resource_path(relative_path=None):
# Get absolute path to resource, works for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    if relative_path:
        return os.path.join(base_path, relative_path)
    else:
        return os.path.join(base_path)