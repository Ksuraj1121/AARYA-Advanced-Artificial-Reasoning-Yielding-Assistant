# ==========================================
# AARYA v2.11 Live Intelligence Core
# Module Health Scanner
# ==========================================

import os
import json
from datetime import datetime


BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


VERSION = "AARYA v2.11"


MODULES = {

    "Brain Core": "02_Core/brain.py",

    "Memory System": "05_Memory/memory.py",

    "API Server": "09_API/server.py",

    "Website Dashboard": "08_Website/dashboard.html",

    "Speech Engine": "04_Voice/speech_engine.py",

    "Wake Word": "04_Voice/wake_word.py",

    "Automation": "09_Automation/file_control.py"

}


def check_module(path):

    full_path = os.path.join(
        BASE_PATH,
        path
    )

    if os.path.exists(full_path):
        return "ONLINE"
    else:
        return "MISSING"



def memory_count():

    memory_file = os.path.join(
        BASE_PATH,
        "09_API",
        "aarya_memory.json"
    )

    try:

        with open(memory_file,"r") as file:

            data = json.load(file)

            return len(data)

    except:

        return 0



def system_scan():

    print("="*45)

    print("🤖 AARYA LIVE INTELLIGENCE CORE")

    print("="*45)


    print()

    print("Version:", VERSION)

    print(
        "Time:",
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    )

    print()


    online = 0


    for name,path in MODULES.items():

        status = check_module(path)

        if status == "ONLINE":

            online += 1

            print(
                f"{name:<25}: 🟢 {status}"
            )

        else:

            print(
                f"{name:<25}: 🔴 {status}"
            )


    print()

    health = int(
        (online / len(MODULES)) * 100
    )


    print(
        "💾 Memory Entries:",
        memory_count()
    )

    print()

    print(
        "🚀 AARYA Health:",
        health,
        "%"
    )

    print("="*45)



if __name__ == "__main__":

    system_scan()