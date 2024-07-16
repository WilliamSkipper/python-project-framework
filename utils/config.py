import json
import os

# Function to load config data
def load_config():
    
    # Get the directory path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to config.json one directory back
    config_file_path = os.path.join(current_dir, '..', 'manifest.json')

    # Normalize the path to handle any double slashes or backslashes
    config_file_path = os.path.normpath(config_file_path)

    with open(config_file_path, 'r') as f:
        config_data = json.load(f)
        
    return config_data

