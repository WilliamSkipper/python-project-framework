import os
import platform
from utils.config import load_config

def os_path():
    # Determine the operating system
    current_os = platform.system()

    # Fetch application name
    config = load_config()
    app_name = config['app_name']

    # Define default folder paths for different operating systems
    if current_os == 'Windows':
        folder_path = os.path.join('C:\\ProgramData', app_name)
    elif current_os == 'Darwin':  # macOS
        folder_path = os.path.join('/Library/Application Support', app_name)
    elif current_os == 'Linux':
        folder_path = os.path.join('/var/lib', app_name)
    else:
        raise ValueError(f"Unsupported operating system: {current_os}")
    
    return folder_path
