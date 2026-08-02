
# ==============================
# AARYA App Control Module v1.0
# Windows Application Control
# ==============================

import sys
import os


# Connect Commands Apps

COMMAND_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "05_Commands"
    )
)

sys.path.insert(
    0,
    COMMAND_PATH
)


from apps import (
    open_calculator,
    open_notepad,
    open_paint,
    open_file_explorer,
    open_vscode
)



# ==============================
# Open Application
# ==============================

def open_app(command):

    command = command.lower()


    if "calculator" in command:

        open_calculator()

        return "Opening Calculator."


    elif "notepad" in command:

        open_notepad()

        return "Opening Notepad."


    elif "paint" in command:

        open_paint()

        return "Opening Paint."


    elif "file explorer" in command:

        open_file_explorer()

        return "Opening File Explorer."


    elif (
        "vscode" in command
        or "visual studio code" in command
    ):

        open_vscode()

        return "Opening Visual Studio Code."


    else:

        return "Application not found."