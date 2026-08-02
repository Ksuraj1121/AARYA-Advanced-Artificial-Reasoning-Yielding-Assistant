# ==========================================
# AARYA AI Desktop Dashboard v2.10
# Jarvis Style Command Center
# ==========================================

import customtkinter as ctk
import os
import json


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


BASE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


def check(path):

    return os.path.exists(
        os.path.join(BASE, path)
    )


def get_progress():

    modules = [

        check("02_Core/brain.py"),
        check("05_Memory/memory.py"),
        check("09_API/server.py"),
        check("08_Website/dashboard.html"),
        check("04_Voice/speech_engine.py"),
        check("04_Voice/wake_word.py"),
        check("09_Automation/file_control.py")

    ]

    score = 0

    for item in modules:

        if item:
            score += 1


    return int(
        (score / len(modules))*100
    )



# Window

app = ctk.CTk()

app.title(
    "🤖 AARYA AI Command Center v2.10"
)

app.geometry(
    "800x600"
)



title = ctk.CTkLabel(
    app,
    text="🤖 AARYA AI",
    font=("Arial",35,"bold")
)

title.pack(
    pady=20
)



subtitle = ctk.CTkLabel(
    app,
    text="COMMAND CENTER v2.10",
    font=("Arial",18)
)

subtitle.pack()



progress = get_progress()



health = ctk.CTkProgressBar(
    app,
    width=500
)

health.pack(
    pady=30
)

health.set(
    progress/100
)



percent = ctk.CTkLabel(
    app,
    text=f"System Health : {progress}%",
    font=("Arial",22)
)

percent.pack()



status_frame = ctk.CTkFrame(app)

status_frame.pack(
    pady=30,
    padx=40,
    fill="both"
)



items = [

("🧠 Brain Core","ONLINE"),
("💾 Memory System","ONLINE"),
("🌐 API Server","ONLINE"),
("🎙 Voice System","READY"),
("👂 Wake Word","ACTIVE"),
("⚡ Automation","ONLINE")

]


for name,state in items:

    label = ctk.CTkLabel(
        status_frame,
        text=f"{name}   :   🟢 {state}",
        font=("Arial",18)
    )

    label.pack(
        pady=8
    )



info = ctk.CTkLabel(
    app,
    text=
    """
    Version : AARYA v2.10
    Founder : Suraj Kamble
    Mission : Building Intelligent AI Ecosystem
    """,
    font=("Arial",16)
)

info.pack(
    pady=20
)



app.mainloop()