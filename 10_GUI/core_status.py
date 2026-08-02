# ==============================
# AARYA Core Status Engine v2.2
# ==============================

import os


BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


modules = {

    "Brain Core":
        "02_Core/brain.py",

    "Command Center":
        "05_Commands/commands.py",

    "System Monitor":
        "06_System/system_monitor.py",

    "File Automation":
        "09_Automation/file_control.py",

    "Project Builder":
        "09_Automation/project_builder.py",

    "Voice":
        "04_Voice",

    "Memory":
        "05_Memory",

    "Vision":
        "08_Vision",

    "GUI":
        "10_GUI",

    "Hardware":
        "11_Hardware"

}



def check_core():

    result = {}

    for name, path in modules.items():

        full_path = os.path.join(
            BASE_PATH,
            path
        )


        if os.path.exists(full_path):

            result[name] = "ONLINE"

        else:

            result[name] = "OFFLINE"


    return result