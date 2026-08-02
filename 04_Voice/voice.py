# ==============================
# AARYA Voice System v1.1
# Wake Word + Speech + Brain
# ==============================

import speech_recognition as sr
import pyttsx3
from datetime import datetime
import sys
import os


# ==============================
# Connect AARYA Brain
# ==============================

core_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "02_Core"
    )
)

sys.path.insert(0, core_path)

from brain import get_ai_reply


# ==============================
# Connect Wake Word
# ==============================

voice_path = os.path.abspath(
    os.path.dirname(__file__)
)

sys.path.insert(0, voice_path)

from wake_word import listen_for_wake_word


# ==============================
# Initialize
# ==============================

engine = pyttsx3.init()

recognizer = sr.Recognizer()

recognizer.pause_threshold = 0.8
recognizer.energy_threshold = 300


conversation_mode = False



# ==============================
# Speak
# ==============================

def speak(text):

    print("AARYA:", text)

    engine.say(text)

    engine.runAndWait()
    # ==============================
# ==============================
# Listen Voice
# ==============================

def listen():

    with sr.Microphone(device_index=1) as source:

        print("🎤 Listening...")


        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )


        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )


        except sr.WaitTimeoutError:

            return ""


    try:

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        ).lower()


        print("You:", command)

        return command


    except sr.UnknownValueError:

        return ""


    except sr.RequestError:

        speak(
            "Internet connection required."
        )

        return ""

# ==============================
# AARYA Startup Response
# ==============================

speak(
    "Initializing new core. "
    "Core systems online. "
    "Memory systems ready. "
    "Voice module active. "
    "All systems are ready. "
    "Welcome back, Boss. "
    "AARYA is fully operational. "
    "Awaiting your command."
)



# ==============================
# Main Loop
# ==============================

while True:


    if conversation_mode:

        command = listen()


    else:

        wake_command = listen_for_wake_word()


        if wake_command is None:

            continue


        print(
            "Command from wake word:",
            wake_command
        )


        if wake_command == "":

            speak(
                "Yes Boss, I am listening."
            )

            conversation_mode = True

            command = listen()


        else:

            conversation_mode = True

            command = wake_command



    if command == "":

        continue



    print(
        "Recognized:",
        repr(command)
    )



    # Time

    if "time" in command:

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"Current time is {current_time}"
        )



    # Date

    elif "date" in command:

        current_date = datetime.now().strftime(
            "%d %B %Y"
        )

        speak(
            f"Today is {current_date}"
        )



    # System Status

    elif "status" in command:

        speak(
            "All systems are running."
        )



    # Exit

    elif any(word in command for word in [
        "exit",
        "quit",
        "bye",
        "shutdown"
    ]):

        speak(
            "Goodbye Boss. See you again."
        )

        conversation_mode = False

        break



    # Send to Brain

    else:

        reply = get_ai_reply(
            command
        )

        speak(reply)