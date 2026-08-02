# ==============================
# AARYA Memory System v1.4
# Brain Compatible
# ==============================

import json
import os


# Memory File

MEMORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "aarya_memory.json"
)



# ==============================
# Load Memory
# ==============================

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {}


    try:

        with open(
            MEMORY_FILE,
            "r"
        ) as file:

            return json.load(file)


    except:

        return {}



# ==============================
# Save Memory File
# ==============================

def save_memory_file(memory):

    with open(
        MEMORY_FILE,
        "w"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )



# ==============================
# Remember Function
# Used by Brain
# ==============================

def remember(key, value):

    memory = load_memory()


    memory[key] = value


    save_memory_file(memory)


    return (
        f"I will remember that "
        f"{key} is {value}"
    )



# ==============================
# Recall Function
# Used by Brain
# ==============================

def recall(key):

    memory = load_memory()


    if key in memory:

        return (
            f"{key} is "
            f"{memory[key]}"
        )


    return (
        f"I don't remember your {key}"
    )