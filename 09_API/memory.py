# ==========================================
# AARYA AI v2.7
# Memory Core System
# ==========================================

import json
import os
from datetime import datetime


BASE_PATH = os.path.dirname(
    os.path.abspath(__file__)
)

MEMORY_FILE = os.path.join(
    BASE_PATH,
    "aarya_memory.json"
)



def load_memory():

    try:

        if not os.path.exists(MEMORY_FILE):
            return {}

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except Exception as e:

        print(
            "Memory Error:",
            e
        )

        return {}





def save_memory(key, value):

    data = load_memory()


    data[key] = {

        "value": value,

        "time": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    }


    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


    return data