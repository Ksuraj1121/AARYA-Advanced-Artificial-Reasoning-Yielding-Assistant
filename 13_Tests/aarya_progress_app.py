# ==========================================
# AARYA Progress Monitor App v1.0
# GUI Health Dashboard
# ==========================================

import tkinter as tk
from tkinter import ttk
import os


BASE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


def check_file(path):
    return os.path.exists(
        os.path.join(BASE, path)
    )


def generate_report():

    modules = {

        "🧠 Brain Core":
        ("02_Core/brain.py",100),

        "💾 Memory System":
        ("05_Memory/memory.py",100),

        "🌐 API Server":
        ("09_API/server.py",100),

        "🖥 Website Dashboard":
        ("08_Website/dashboard.html",100),

        "🎙 Speech Engine":
        ("04_Voice/speech_engine.py",100),

        "👂 Wake Word":
        ("04_Voice/wake_word.py",80),

        "⚡ Automation":
        ("09_Automation/file_control.py",100)

    }


    total = 0
    count = 0

    output = ""


    for name,(file,percent) in modules.items():

        if check_file(file):

            output += f"{name:<25} {percent}% ✅\n"
            total += percent

        else:

            output += f"{name:<25} 0% ❌\n"


        count += 1



    overall = int(total/count)


    output += "\n-----------------------------\n"

    output += f"🚀 Overall Progress : {overall}%\n"


    if overall >= 90:

        output += "System Health : 🟢 Excellent"

    elif overall >=70:

        output += "System Health : 🟡 Good"

    else:

        output += "System Health : 🔴 Needs Work"


    return output



def refresh():

    report.delete(
        "1.0",
        tk.END
    )

    report.insert(
        tk.END,
        generate_report()
    )



# Window

root = tk.Tk()

root.title(
    "AARYA Progress Monitor v1.0"
)

root.geometry(
    "600x500"
)


title = tk.Label(
    root,
    text="🤖 AARYA SYSTEM HEALTH MONITOR",
    font=("Arial",16,"bold")
)

title.pack(
    pady=15
)



report = tk.Text(
    root,
    font=("Consolas",12)
)

report.pack(
    expand=True,
    fill="both",
    padx=20
)



button = tk.Button(
    root,
    text="🔄 Check AARYA Status",
    font=("Arial",12),
    command=refresh
)

button.pack(
    pady=15
)



refresh()


root.mainloop()