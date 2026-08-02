# ==========================================
# AARYA Progress Monitor v1.0
# Self Diagnostic System
# ==========================================

import os
import json
import subprocess
from datetime import datetime


BASE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


def check_folder(folder):

    path = os.path.join(BASE, folder)

    return os.path.exists(path)



def check_file(file):

    path = os.path.join(BASE, file)

    return os.path.exists(path)



def check_git():

    try:

        result = subprocess.check_output(
            ["git", "status", "--short"],
            cwd=BASE,
            text=True
        )

        if result.strip():
            return False

        return True

    except:

        return False



def status(percent, name, ok=True):

    icon = "✅" if ok else "⚠️"

    print(
        f"{name:<25} : {percent}% {icon}"
    )



print("="*45)

print("🤖 AARYA SYSTEM REPORT v1.0")

print("="*45)

print()



score = []



# Brain

brain = check_file(
    "02_Core/brain.py"
)

status(
    100 if brain else 0,
    "🧠 Brain Core",
    brain
)

score.append(
    100 if brain else 0
)



# Memory

memory = check_file(
    "05_Memory/memory.py"
)

status(
    100 if memory else 0,
    "💾 Memory System",
    memory
)

score.append(
    100 if memory else 0
)



# API

api = check_file(
    "09_API/server.py"
)

status(
    100 if api else 0,
    "🌐 API Server",
    api
)

score.append(
    100 if api else 0
)



# Website

web = check_file(
    "08_Website/dashboard.html"
)

status(
    100 if web else 0,
    "🖥 Website Dashboard",
    web
)

score.append(
    100 if web else 0
)



# Speech

voice = check_file(
    "04_Voice/speech_engine.py"
)

status(
    100 if voice else 0,
    "🎙 Speech Engine",
    voice
)

score.append(
    100 if voice else 0
)



# Wake Word

wake = check_file(
    "04_Voice/wake_word.py"
)

status(
    80 if wake else 0,
    "👂 Wake Word",
    wake
)

score.append(
    80 if wake else 0
)



# Automation

auto = check_file(
    "09_Automation/file_control.py"
)

status(
    100 if auto else 0,
    "⚡ Automation",
    auto
)

score.append(
    100 if auto else 0
)



# Git

git = check_git()

status(
    100 if git else 50,
    "📦 Git Sync",
    git
)

score.append(
    100 if git else 50
)



overall = int(
    sum(score) / len(score)
)


print()

print("-"*45)

print(
    f"🚀 Overall AARYA Progress : {overall}%"
)


print(
    "🕒 Report Time:",
    datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)


print("-"*45)


if overall >= 90:

    print(
        "System Health: 🟢 Excellent"
    )

elif overall >= 70:

    print(
        "System Health: 🟡 Good"
    )

else:

    print(
        "System Health: 🔴 Needs Work"
    )


print("="*45)