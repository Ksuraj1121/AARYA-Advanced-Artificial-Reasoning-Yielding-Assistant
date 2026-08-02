# ==============================
# AARYA Command Center v1.0
# Final Base Release
# Web + Windows + System + File Control
# ==============================


from datetime import datetime

import sys
import os



# ==============================
# Connect Paths
# ==============================

BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)



# ==============================
# Connect Apps
# ==============================

sys.path.insert(
    0,
    os.path.dirname(__file__)
)


from apps import *



# ==============================
# Connect System
# ==============================

SYSTEM_PATH = os.path.join(
    BASE_PATH,
    "06_System"
)


sys.path.insert(
    0,
    SYSTEM_PATH
)


from system_monitor import full_status



# ==============================
# Connect Automation
# ==============================

AUTOMATION_PATH = os.path.join(
    BASE_PATH,
    "09_Automation"
)


sys.path.insert(
    0,
    AUTOMATION_PATH
)


from file_control import (
    open_folder,
    create_folder,
    create_file,
    search_file,
    rename_file,
    delete_file,
    list_files,
    open_file,
    read_file
)



from project_builder import create_project



# ==============================
# Execute Commands
# ==============================

def execute(command):


    command = command.lower().strip()



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

    elif (
        "system status" in command
        or command == "status"
    ):

        return full_status()



    # ==============================
    # Project Builder
    # ==============================

    elif "create project" in command:


        name = command.replace(
            "create project",
            ""
        ).strip()


        return create_project(
            name
        )



    # ==============================
    # Folder
    # ==============================

    elif "create folder" in command:


        name = command.replace(
            "create folder",
            ""
        ).strip()


        return create_folder(
            name
        )



    elif "open folder" in command:


        name = command.replace(
            "open folder",
            ""
        ).strip()


        return open_folder(
            name
        )



    # ==============================
    # File
    # ==============================

    elif "create file" in command:


        name = command.replace(
            "create file",
            ""
        ).strip()


        return create_file(
            name
        )



    elif "search file" in command:


        name = command.replace(
            "search file",
            ""
        ).strip()


        return search_file(
            name
        )



    elif "rename file" in command:


        data = command.replace(
            "rename file",
            ""
        ).strip()


        parts = data.split(
            " to "
        )


        if len(parts) == 2:

            return rename_file(
                parts[0],
                parts[1]
            )


        return (
            "Use: rename file old to new"
        )



    elif "delete file" in command:


        name = command.replace(
            "delete file",
            ""
        ).strip()


        return delete_file(
            name
        )



    elif "list files" in command:

        return list_files()



    elif "open file" in command:


        name = command.replace(
            "open file",
            ""
        ).strip()


        return open_file(
            name
        )



    elif "read file" in command:


        name = command.replace(
            "read file",
            ""
        ).strip()


        return read_file(
            name
        )



    # ==============================
    # Web
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



    elif (
        "open vscode" in command
        or "open visual studio code" in command
    ):

        open_vscode()

        return "Opening Visual Studio Code."



    # ==============================
    # Shutdown
    # ==============================

    elif "shutdown" in command:

        return (
            "Shutdown command received."
        )



    return None