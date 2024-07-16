from utils.get_timestamp import get_timestamp
from utils.os_path import os_path
import os

def log(content=str):
    
    log_folder_path = os.path.join(os_path(), 'logs')
    
    if os.path. exists(log_folder_path):
        pass
    else:
        os.makedirs(log_folder_path, exist_ok=True)
    
    
    day, time = get_timestamp()
    
    log_file_name = f"{day}.txt"
    log_file_content= f"[{time}] {content}\n"
    log_file_path = os.path.join(log_folder_path, log_file_name)
    
    f = open(log_file_path, "a")
    f.write(log_file_content)
    f.close()