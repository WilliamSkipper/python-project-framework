from datetime import datetime

def get_timestamp():
    day = datetime.now().strftime('%d-%m-%Y')
    time = datetime.now().strftime('%H:%M:%S')
    return day, time