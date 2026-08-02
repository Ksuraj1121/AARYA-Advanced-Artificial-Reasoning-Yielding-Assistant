# ==============================
# AARYA Brain Core v10.1
# Identity + Database + Intent
# Skills + Memory + Commands
# ==============================


import sys
import os



# ==============================
# Base Path
# ==============================

BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)



# ==============================
# Module Paths
# ==============================

MODULE_PATH = os.path.join(
    BASE_PATH,
    "modules"
)


MEMORY_PATH = os.path.join(
    BASE_PATH,
    "05_Memory"
)


COMMAND_PATH = os.path.join(
    BASE_PATH,
    "05_Commands"
)


DATABASE_PATH = os.path.join(
    BASE_PATH,
    "database"
)



sys.path.insert(0, MODULE_PATH)
sys.path.insert(0, MEMORY_PATH)
sys.path.insert(0, COMMAND_PATH)
sys.path.insert(0, DATABASE_PATH)



# ==============================
# Core Imports
# ==============================

from intent import detect_intent

from skills import run_skill


from memory import (
    remember,
    recall
)


from commands import execute



# ==============================
# Database Identity Layer
# ==============================

from database_api import (
    get_name,
    get_status,
    get_profile
)



# ==============================
# AARYA Brain Reply Engine
# ==============================

def get_ai_reply(message):


    message = message.strip()

    lower_message = message.lower()



    # ==============================
    # Identity System
    # ==============================


    if (
        "who is your founder" in lower_message
        or "your founder" in lower_message
        or "founder of aarya" in lower_message
    ):

        return (
            "Welcome back, Boss.\n"
            f"My founder is {get_name()}, "
            "Founder & Chief Architect of AARYA AI."
        )



    if (
        "aarya status" in lower_message
        or "your status" in lower_message
        or "system status" in lower_message
    ):

        return (
            "Welcome back, Boss.\n"
            f"AARYA status is {get_status()}.\n"
            "All core systems are ready."
        )



    if (
        "about aarya" in lower_message
        or "about yourself" in lower_message
        or "who are you" in lower_message
    ):


        profile = get_profile()


        return (
            "Welcome back, Boss.\n"
            f"I am {profile['aarya']['name']}.\n"
            f"Release: {profile['aarya']['release']}\n"
            f"Status: {profile['aarya']['status']}\n"
            "Awaiting your command."
        )



    # ==============================
    # Command Center
    # ==============================


    command_response = execute(
        message
    )


    if command_response:

        return command_response



    # ==============================
    # Intent Detection
    # ==============================


    intent = detect_intent(
        message
    )



    # ==============================
    # Greeting
    # ==============================


    if intent == "greeting":

        return (
            "Welcome back, Boss.\n"
            "AARYA is online and ready."
        )



    # ==============================
    # Calculator
    # ==============================


    elif intent == "calculator":

        return run_skill(
            "calculator",
            message
        )



    # ==============================
    # App Control
    # ==============================


    elif intent == "app_control":

        return run_skill(
            "app_control",
            message
        )



    # ==============================
    # File Control
    # ==============================


    elif intent == "file_control":

        return run_skill(
            "file_control",
            message
        )



    # ==============================
    # Memory Save
    # ==============================


    elif intent == "memory_save":


        data = message.replace(
            "remember",
            ""
        ).strip()


        parts = data.split(
            " is "
        )


        if len(parts) == 2:

            return remember(
                parts[0],
                parts[1]
            )


        return (
            "Tell me what I should remember, Boss."
        )



    # ==============================
    # Memory Recall
    # ==============================


    elif intent == "memory_recall":


        key = message.replace(
            "what is my",
            ""
        ).strip()


        return recall(
            key
        )



    # ==============================
    # System
    # ==============================


    elif intent == "system":

        return (
            "Welcome back, Boss.\n"
            "All systems are running."
        )



    # ==============================
    # Unknown
    # ==============================


    else:

        return (
            "I am still learning, Boss."
        )