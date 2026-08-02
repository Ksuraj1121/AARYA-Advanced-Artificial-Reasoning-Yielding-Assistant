# ==============================
# AARYA Brain v1.4
# Intent + Skills + Memory
# ==============================


import sys
import os


# ==============================
# Connect Modules
# ==============================

BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


MODULE_PATH = os.path.join(
    BASE_PATH,
    "modules"
)


MEMORY_PATH = os.path.join(
    BASE_PATH,
    "05_Memory"
)


sys.path.append(MODULE_PATH)
sys.path.append(MEMORY_PATH)



# ==============================
# Import
# ==============================

from intent import detect_intent

from skills import run_skill

from memory import remember, recall



# ==============================
# AARYA Reply Engine
# ==============================

def get_ai_reply(message):


    intent = detect_intent(message)



    # Greeting

    if intent == "greeting":

        return run_skill(
            "greeting",
            message
        )



    # Calculator

    elif intent == "calculator":

        return run_skill(
            "calculator",
            message
        )



    # App Control

    elif intent == "app_control":

        return run_skill(
            "app_control",
            message
        )



    # File Control

    elif intent == "file_control":

        return run_skill(
            "file_control",
            message
        )



    # Memory Save

    elif intent == "memory_save":

        text = message.replace(
            "remember",
            ""
        ).strip()


        parts = text.split(
            " is "
        )


        if len(parts) == 2:

            return remember(
                parts[0],
                parts[1]
            )


        return "Tell me what I should remember."



    # Memory Recall

    elif intent == "memory_recall":

        key = message.replace(
            "what is my",
            ""
        ).strip()


        return recall(key)



    # System

    elif intent == "system":

        return "All systems are running."



    # Unknown

    else:

        return (
            "I am still learning. "
            "Please teach me."
        )