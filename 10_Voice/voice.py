# ==========================================
# AARYA AI
# Version : v2.9
# Module  : Voice Controller
# Author  : Suraj Kamble
# ==========================================

"""
AARYA Voice Controller

This module is the main entry point for
the AARYA Voice System.
"""

from speech_engine import speak


def startup():

    print("=" * 45)
    print("        AARYA AI v2.9")
    print("=" * 45)

    speak("Initializing new core.")
    speak("Core systems online.")
    speak("Memory systems ready.")
    speak("Voice module active.")
    speak("API connected.")
    speak("Dashboard connected.")
    speak("Welcome back Boss.")
    speak("AARYA is fully operational.")
    speak("Awaiting your command.")


def main():

    startup()

    while True:

        command = input("\nYou : ")

        if command.lower() in ["exit", "quit"]:

            speak("Goodbye Boss.")
            break

        elif command.strip() == "":

            continue

        else:

            speak(f"You said {command}")


if __name__ == "__main__":
    main()