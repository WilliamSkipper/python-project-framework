from utils.os_path import os_path

import os
from datetime import datetime

def log(content=str):
    day = datetime.now().strftime('%d-%m-%Y')
    time = datetime.now().strftime('%H:%M:%S')
    
    log_folder_path = os.path.join(os_path(), 'logs')
    
    if os.path. exists(log_folder_path):
        pass
    else:
        os.makedirs(log_folder_path, exist_ok=True)
    
    log_file_name = f"{day}.txt"
    log_file_content= f"[{time}] {content}\n"
    log_file_path = os.path.join(log_folder_path, log_file_name)
    
    f = open(log_file_path, "a")
    f.write(log_file_content)
    f.close()