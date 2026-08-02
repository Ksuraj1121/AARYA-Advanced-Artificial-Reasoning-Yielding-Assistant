# ==============================
# AARYA Command Center v1.3
# Web + Windows + System + File Control
# ==============================


from datetime import datetime

import sys
import os



# ==============================
# Connect Apps
# ==============================

from apps import *



# ==============================
# Connect System Monitor
# ==============================

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
# Connect File Automation
# ==============================

AUTOMATION_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "09_Automation"
    )
)

sys.path.insert(0, AUTOMATION_PATH)


from file_control import (
    open_folder,
    create_folder,
    create_file,
    search_file
)



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

        return f"The current time is {now}"



    # ==============================
    # Date
    # ==============================

    elif "date" in command:

        today = datetime.now().strftime(
            "%d %B %Y"
        )

        return f"Today is {today}"



    # ==============================
    # System Status
    # ==============================

    elif "system status" in command or "status" in command:

        return full_status()



    # ==============================
    # File Control
    # ==============================

    elif "create folder" in command:

        folder_name = command.replace(
            "create folder",
            ""
        ).strip()

        return create_folder(folder_name)



    elif "create file" in command:

        file_name = command.replace(
            "create file",
            ""
        ).strip()

        return create_file(file_name)



    elif "search file" in command:

        file_name = command.replace(
            "search file",
            ""
        ).strip()

        return search_file(file_name)



    # ==============================
    # Web Control
    # ==============================

    elif "open google" in command:

        open_google()

        return "Opening Google."



    elif "open youtube" in command:

        open_youtube()

        return "Opening YouTube."



    elif "open chatgpt" in command:

        open_chatgpt()

        return "Opening ChatGPT."



    elif "open github" in command:

        open_github()

        return "Opening GitHub."



    # ==============================
    # Windows Apps
    # ==============================

    elif "open calculator" in command:

        open_calculator()

        return "Opening Calculator."



    elif "open notepad" in command:

        open_notepad()

        return "Opening Notepad."



    elif "open paint" in command:

        open_paint()

        return "Opening Paint."



    elif "open file explorer" in command:

        open_file_explorer()

        return "Opening File Explorer."



    elif "open vscode" in command or "open visual studio code" in command:

        open_vscode()

        return "Opening Visual Studio Code."



    # ==============================
    # Folder Open
    # ==============================

    elif "open folder" in command:

        folder = command.replace(
            "open folder",
            ""
        ).strip()

        return open_folder(folder)



    # ==============================
    # Shutdown
    # ==============================

    elif "shutdown" in command:

        return "Shutdown command received."



    # ==============================
    # Unknown
    # ==============================

    else:

        return None