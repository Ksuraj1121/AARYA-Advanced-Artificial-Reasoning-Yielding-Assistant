# ==============================
# AARYA Command Center v1.2
# Web + Windows + System Monitor
# ==============================


from datetime import datetime
from apps import *


# ==============================
# Connect System Monitor
# ==============================

import sys
import os


SYSTEM_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "06_System"
    )
)

sys.path.insert(0, SYSTEM_PATH)


from system_monitor import full_status



# ==============================
# Execute Command
# ==============================

def execute(command):

    command = command.lower()



    # ==============================
    # Time
    # ==============================

    if "time" in command:

        now = datetime.now().strftime(
            "%I:%M %p"
        )

        return (
            f"The current time is {now}"
        )



    # ==============================
    # Date
    # ==============================

    elif "date" in command:

        today = datetime.now().strftime(
            "%d %B %Y"
        )

        return (
            f"Today is {today}"
        )



    # ==============================
    # System Status
    # ==============================

    elif "system status" in command or "status" in command:

        return full_status()



    # ==============================
    # Google
    # ==============================

    elif "open google" in command:

        open_google()

        return (
            "Opening Google."
        )



    # ==============================
    # YouTube
    # ==============================

    elif "open youtube" in command:

        open_youtube()

        return (
            "Opening YouTube."
        )



    # ==============================
    # ChatGPT
    # ==============================

    elif "open chatgpt" in command:

        open_chatgpt()

        return (
            "Opening ChatGPT."
        )



    # ==============================
    # GitHub
    # ==============================

    elif "open github" in command:

        open_github()

        return (
            "Opening GitHub."
        )



    # ==============================
    # Windows Apps
    # ==============================

    elif "open calculator" in command:

        open_calculator()

        return (
            "Opening Calculator."
        )



    elif "open notepad" in command:

        open_notepad()

        return (
            "Opening Notepad."
        )



    elif "open paint" in command:

        open_paint()

        return (
            "Opening Paint."
        )



    elif "open file explorer" in command:

        open_file_explorer()

        return (
            "Opening File Explorer."
        )



    elif "open vscode" in command or "open visual studio code" in command:

        open_vscode()

        return (
            "Opening Visual Studio Code."
        )



    # ==============================
    # Shutdown
    # ==============================

    elif "shutdown" in command:

        return (
            "Shutdown command received."
        )



    # ==============================
    # Unknown
    # ==============================

    else:

        return None