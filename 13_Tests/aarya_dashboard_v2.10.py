# ==========================================
# AARYA v2.10 Desktop Command Center
# Jarvis Style Dashboard
# ==========================================

import customtkinter as ctk
import json
import os
from datetime import datetime


# -----------------------------
# Theme
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# -----------------------------
# Main Window
# -----------------------------

app = ctk.CTk()

app.title("AARYA AI | Command Center v2.10")
app.geometry("900x600")


# -----------------------------
# Header
# -----------------------------

title = ctk.CTkLabel(
    app,
    text="🤖 AARYA AI COMMAND CENTER",
    font=("Arial", 30, "bold")
)

title.pack(pady=20)


subtitle = ctk.CTkLabel(
    app,
    text="Initializing Intelligence • Building The Future",
    font=("Arial",16)
)

subtitle.pack()



# -----------------------------
# Progress
# -----------------------------

progress_title = ctk.CTkLabel(
    app,
    text="🚀 Overall System Progress",
    font=("Arial",20,"bold")
)

progress_title.pack(pady=20)


progress = ctk.CTkProgressBar(
    app,
    width=600
)

progress.pack()

progress.set(0.91)



progress_label = ctk.CTkLabel(
    app,
    text="91% System Health 🟢",
    font=("Arial",18)
)

progress_label.pack(pady=10)



# -----------------------------
# Dashboard Cards
# -----------------------------

frame = ctk.CTkFrame(app)

frame.pack(
    pady=20,
    padx=20,
    fill="both",
    expand=True
)



def create_card(name,value,row,column):

    card = ctk.CTkFrame(
        frame,
        width=200,
        height=120
    )

    card.grid(
        row=row,
        column=column,
        padx=20,
        pady=20
    )


    ctk.CTkLabel(
        card,
        text=name,
        font=("Arial",18,"bold")
    ).pack(pady=10)


    ctk.CTkLabel(
        card,
        text=value,
        font=("Arial",16)
    ).pack()



# System Modules

create_card(
    "🧠 Brain Core",
    "100% ✅",
    0,
    0
)


create_card(
    "💾 Memory",
    "Connected ✅",
    0,
    1
)


create_card(
    "🌐 API Server",
    "Online 🟢",
    0,
    2
)


create_card(
    "🎙 Voice",
    "Ready ✅",
    1,
    0
)


create_card(
    "⚡ Automation",
    "Active ✅",
    1,
    1
)


create_card(
    "👂 Wake Word",
    "80% ⚠️",
    1,
    2
)



# -----------------------------
# Version Panel
# -----------------------------

version = ctk.CTkFrame(app)

version.pack(
    pady=10
)


ctk.CTkLabel(
    version,
    text="""
🤖 AARYA VERSION

Current:
v2.10

Developer:
Suraj Kamble

Status:
ACTIVE 🟢
""",
    font=("Arial",16)
).pack(
    padx=30,
    pady=20
)



# -----------------------------
# Footer
# -----------------------------

footer = ctk.CTkLabel(
    app,
    text="© 2026 AARYA AI | Command Center",
    font=("Arial",12)
)

footer.pack(
    pady=10
)



app.mainloop()