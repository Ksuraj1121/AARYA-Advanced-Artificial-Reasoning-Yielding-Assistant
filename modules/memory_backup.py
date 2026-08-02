import json

MEMORY_FILE = "data/memory.json"


def save_memory(name):
    data = {
        "name": name,
        "preferences": {}
    }

    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {
            "name": "",
            "preferences": {}
        }