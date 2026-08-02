# ==========================================
# AARYA AI v2.7
# Memory Core System
# ==========================================

import json
import os
from datetime import datetime


# Memory Database File

MEMORY_FILE = "aarya_memory.json"



# ==========================================
# Save Memory
# ==========================================

def save_memory(key, value):

    memory = load_memory()

    memory[key] = {

        "value": value,

        "time": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    }


    with open(
        MEMORY_FILE,
        "w"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )



    return "Memory Saved"



# ==========================================
# Load Memory
# ==========================================

def load_memory():

    if not os.path.exists(
        MEMORY_FILE
    ):

        return {}


    with open(
        MEMORY_FILE,
        "r"
    ) as file:

        return json.load(file)



# ==========================================
# Read Memory
# ==========================================

def get_memory(key):

    memory = load_memory()

    if key in memory:

        return memory[key]


    return "No Memory Found"





# ==========================================
# Test
# ==========================================

if __name__ == "__main__":


    save_memory(
        "Founder",
        "Suraj Kamble"
    )


    print(
        get_memory("Founder")
    )