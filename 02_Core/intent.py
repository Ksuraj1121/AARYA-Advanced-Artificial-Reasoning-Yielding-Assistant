# ==============================
# AARYA Intent Engine v1.1
# Command Understanding System
# ==============================


def detect_intent(message):

    message = message.lower().strip()


    # ==============================
    # Greeting
    # ==============================

    if any(word in message for word in [
        "hi",
        "hello",
        "hey",
        "namaste"
    ]):

        return "greeting"



    # ==============================
    # Calculator
    # ==============================

    elif any(word in message for word in [
        "plus",
        "minus",
        "multiply",
        "multiplied",
        "times",
        "divide",
        "divided",
        "+",
        "-",
        "*",
        "/"
    ]):

        return "calculator"



    # ==============================
    # Memory Save
    # ==============================

    elif message.startswith("remember"):

        return "memory_save"



    # ==============================
    # Memory Recall
    # ==============================

    elif any(word in message for word in [
        "what is my",
        "do you remember",
        "tell me my"
    ]):

        return "memory_recall"



    # ==============================
    # Application Control
    # ==============================

    elif any(word in message for word in [
        "open",
        "start",
        "launch",
        "run"
    ]):

        return "app_control"



    # ==============================
    # System Status
    # ==============================

    elif any(word in message for word in [
        "system",
        "status",
        "health"
    ]):

        return "system"



    # ==============================
    # File Control
    # ==============================

    elif any(word in message for word in [
        "file",
        "folder",
        "create file",
        "delete file"
    ]):

        return "file_control"



    # ==============================
    # About AARYA
    # ==============================

    elif "about aarya" in message:

        return "about"



    # ==============================
    # Unknown
    # ==============================

    else:

        return "unknown"