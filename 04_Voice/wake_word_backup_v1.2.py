# ==============================
# AARYA Wake Word System v1.2
# ==============================

import speech_recognition as sr


recognizer = sr.Recognizer()

recognizer.pause_threshold = 0.8
recognizer.energy_threshold = 300


WAKE_WORDS = [
    "aarya wake up",
    "arya wake up",
    "hey aarya",
    "hey arya",
    "hello aarya",
    "hello arya",
    "aarya",
    "arya"
]


def listen_for_wake_word():

    with sr.Microphone(device_index=1) as source:

        print("👂 Waiting for wake word...")


        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )


        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )


        except sr.WaitTimeoutError:

            return None



    try:

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        ).lower()


        print("Heard:", command)


        for word in WAKE_WORDS:

            if word in command:

                command = command.replace(
                    word,
                    ""
                )

                return command.strip()



        return None



    except sr.UnknownValueError:

        return None



    except sr.RequestError:

        print(
            "Speech recognition internet error."
        )

        return None