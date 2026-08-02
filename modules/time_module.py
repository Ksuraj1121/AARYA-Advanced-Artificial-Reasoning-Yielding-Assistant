import datetime

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time


def get_date():
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    return current_date