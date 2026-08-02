# ==========================================
# AARYA AI
# Version : v2.9
# Module  : Speech Engine
# Author  : Suraj Kamble
# ==========================================

"""
Speech Engine

Converts text into voice using pyttsx3.
"""

import pyttsx3


# Initialize engine
engine = pyttsx3.init()


# Voice Settings
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)


def speak(text):
    """
    Speak the given text.
    """

    print(f"\n🤖 AARYA : {text}")

    engine.say(text)
    engine.runAndWait()


def test():

    speak("Speech engine is online.")
    speak("Welcome back Boss.")
    speak("AARYA Voice System is ready.")


if __name__ == "__main__":
    test()