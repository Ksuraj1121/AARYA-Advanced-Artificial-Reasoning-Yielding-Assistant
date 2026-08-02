# ==============================
# AARYA Apps Control v1.1
# Windows + Web Application Launcher
# ==============================

import webbrowser
import os


# ==============================
# Web Apps
# ==============================

def open_google():
    webbrowser.open(
        "https://www.google.com"
    )


def open_youtube():
    webbrowser.open(
        "https://www.youtube.com"
    )


def open_chatgpt():
    webbrowser.open(
        "https://chat.openai.com"
    )


def open_github():
    webbrowser.open(
        "https://github.com"
    )


# ==============================
# Windows Apps
# ==============================

def open_calculator():

    os.system(
        "start calc"
    )


def open_notepad():

    os.system(
        "start notepad"
    )


def open_paint():

    os.system(
        "start mspaint"
    )


def open_file_explorer():

    os.system(
        "start explorer"
    )


def open_vscode():

    os.system(
        "start code"
    )