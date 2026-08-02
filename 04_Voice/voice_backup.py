import speech_recognition as sr
import pyttsx3
from datetime import datetime
import sys
import os


# ==============================
# Connect AARYA Brain
# ==============================

core_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "02_Core")
)

sys.path.append(core_path)

from brain import get_ai_reply



# ==============================
# Connect Wake Word
# ==============================

from wake_word import listen_for_wake_word



# ==============================
# Initialize
# ==============================

engine = pyttsx3.init()

recognizer = sr.Recognizer()



# ==============================
# Speak
# ==============================

def speak(text):

    print("AARYA:", text)

    engine.say(text)

    engine.runAndWait()



# ==============================
# Normal Listen
# ==============================

def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)


    try:

        command = recognizer.recognize_google(audio).lower()

        print("You:", command)

        return command


    except sr.UnknownValueError:

        return ""


    except sr.RequestError:

        speak("Internet connection required.")

        return ""



# ==============================
# Start AARYA
# ==============================

speak("Hello Suraj. I am AARYA. Memory voice system is ready.")



# ==============================
# Main Loop
# ==============================

while True:


    wake_command = listen_for_wake_word()


    if wake_command is None:

        continue



    print("Command from wake word:", wake_command)



    # Only wake word

    if wake_command == "":

        speak("Yes Suraj, I am listening.")

        command = listen()



    else:

        command = wake_command



    if command == "":

        continue



    print("Recognized:", repr(command))



    # Time

    if "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"Current time is {current_time}")



    # Date

    elif "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        speak(f"Today is {current_date}")



    # Status

    elif "status" in command:

        speak("All systems are running.")



    # Exit

    elif any(word in command for word in ["exit", "quit", "bye"]):

        speak("Goodbye Suraj. See you again.")

        break



    # Brain + Memory

    else:

        reply = get_ai_reply(command)

        speak(reply)