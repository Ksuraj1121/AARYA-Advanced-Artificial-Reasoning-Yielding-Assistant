import datetime

LOG_FILE = "logs/aarya.log"


def log_activity(message):
    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{time}] {message}\n")