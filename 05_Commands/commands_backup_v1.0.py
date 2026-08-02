# ==============================
# AARYA Command Center v1.0
# Time + Date + Web Commands
# ==============================


from datetime import datetime
from apps import *



# ==============================
# Execute Command
# ==============================

def execute(command):

    command = command.lower()



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
    # Open Google
    # ==============================

    elif "open google" in command:

        open_google()

        return (
            "Opening Google."
        )



    # ==============================
    # Open YouTube
    # ==============================

    elif "open youtube" in command:

        open_youtube()

        return (
            "Opening YouTube."
        )



    # ==============================
    # Open ChatGPT
    # ==============================

    elif "open chatgpt" in command:

        open_chatgpt()

        return (
            "Opening ChatGPT."
        )



    # ==============================
    # Open GitHub
    # ==============================

    elif "open github" in command:

        open_github()

        return (
            "Opening GitHub."
        )



    # ==============================
    # Exit
    # ==============================

    elif "goodbye" in command or "shutdown" in command:

        return (
            "Goodbye Boss."
        )



    # ==============================
    # Unknown
    # ==============================

    else:

        return (
            "Sorry Boss, I don't know that command yet."
        )