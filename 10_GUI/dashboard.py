# ==============================
# AARYA GUI Dashboard v1.0
# Final Base Release
# Live Core Monitor
# ==============================


import tkinter as tk
from tkinter import ttk

import sys
import os

from datetime import datetime



# ==============================
# Connect System Monitor
# ==============================

BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


SYSTEM_PATH = os.path.join(
    BASE_PATH,
    "06_System"
)


sys.path.insert(
    0,
    SYSTEM_PATH
)


from system_monitor import full_status



# ==============================
# Main Window
# ==============================

root = tk.Tk()


root.title(
    "AARYA CORE v1.0"
)


root.geometry(
    "750x600"
)



# ==============================
# Header
# ==============================

title = tk.Label(
    root,
    text="🤖 AARYA CORE v1.0",
    font=(
        "Arial",
        26,
        "bold"
    )
)


title.pack(
    pady=15
)



clock = tk.Label(
    root,
    font=(
        "Arial",
        14
    )
)


clock.pack()



# ==============================
# Status Display
# ==============================

status_box = tk.Text(
    root,
    height=18,
    width=70,
    font=(
        "Consolas",
        12
    )
)


status_box.pack(
    pady=20
)



# ==============================
# System Bars
# ==============================

cpu_label = tk.Label(
    root,
    text="CPU"
)

cpu_label.pack()


cpu_bar = ttk.Progressbar(
    root,
    length=450,
    maximum=100
)


cpu_bar.pack(
    pady=5
)



ram_label = tk.Label(
    root,
    text="RAM"
)

ram_label.pack()


ram_bar = ttk.Progressbar(
    root,
    length=450,
    maximum=100
)


ram_bar.pack(
    pady=5
)



battery_label = tk.Label(
    root,
    text="Battery"
)

battery_label.pack()


battery_bar = ttk.Progressbar(
    root,
    length=450,
    maximum=100
)


battery_bar.pack(
    pady=5
)



# ==============================
# Update Dashboard
# ==============================

def update_dashboard():


    clock.config(
        text=datetime.now().strftime(
            "%d-%m-%Y  %I:%M:%S %p"
        )
    )


    status = full_status()



    report = f"""

🧠 Brain Core        : ONLINE

⚙ Command Center     : ONLINE

💻 System Monitor    : ONLINE

📂 Automation        : ONLINE

🎙 Voice             : ONLINE

💾 Memory            : ONLINE


SYSTEM STATUS:

{status}


🤖 AARYA STATUS:

FULLY OPERATIONAL

"""


    status_box.delete(
        "1.0",
        tk.END
    )


    status_box.insert(
        tk.END,
        report
    )



    # Demo values

    cpu_bar["value"] = 20

    ram_bar["value"] = 80

    battery_bar["value"] = 95



    root.after(
        1000,
        update_dashboard
    )



# ==============================
# Start
# ==============================

update_dashboard()


root.mainloop()