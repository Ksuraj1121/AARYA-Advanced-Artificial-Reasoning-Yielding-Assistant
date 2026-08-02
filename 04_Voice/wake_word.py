# ==========================================
# AARYA Wake Word System v2.1
# PyAudio Free - SoundDevice Engine
# ==========================================

import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3
import tempfile
import os


# ==============================
# Speech Engine
# ==============================

engine = pyttsx3.init()

engine.setProperty(
    "rate",
    170
)


def speak(text):

    print("🤖 AARYA :", text)

    engine.say(text)
    engine.runAndWait()



# ==============================
# Recorder
# ==============================

SAMPLE_RATE = 16000
DURATION = 5



def record_audio():

    print("🎙 Listening...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1
    )

    sd.wait()


    file_path = tempfile.mktemp(
        suffix=".wav"
    )


    sf.write(
        file_path,
        audio,
        SAMPLE_RATE
    )


    return file_path



# ==============================
# Wake Word Detector
# ==============================

WAKE_WORDS = [
    "aarya",
    "arya",
    "aarya wake up",
    "arya wake up",
    "hey aarya"
]



recognizer = sr.Recognizer()



def listen_for_wake_word():


    file_path = record_audio()


    try:

        with sr.AudioFile(file_path) as source:

            audio = recognizer.record(source)



        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        ).lower()



        print(
            "Heard:",
            command
        )



        for word in WAKE_WORDS:

            if word in command:


                speak(
                    "Yes Boss, I am listening."
                )


                return command.replace(
                    word,
                    ""
                ).strip()



    except sr.UnknownValueError:

        pass


    except sr.RequestError:

        print(
            "Internet speech service error"
        )


    finally:

        if os.path.exists(file_path):

            os.remove(file_path)



    return None



# ==============================
# Test
# ==============================

if __name__ == "__main__":


    speak(
        "AARYA Wake Word System is online."
    )


    while True:


        result = listen_for_wake_word()


        if result:

            print(
                "Command:",
                result
            )