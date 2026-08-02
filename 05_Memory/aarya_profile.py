import json
import os


PROFILE_FILE = os.path.join(
    os.path.dirname(__file__),
    "profile.json"
)


def load_profile():

    if os.path.exists(PROFILE_FILE):

        with open(PROFILE_FILE, "r") as file:
            return json.load(file)

    return {}



def get_profile(key):

    profile = load_profile()

    if key in profile:

        return profile[key]

    return "I don't know yet."