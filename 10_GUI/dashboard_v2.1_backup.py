# ==============================
# AARYA GUI Dashboard v2.1
# Live Core Monitor
# ==============================

import tkinter as tk
from tkinter import ttk
import sys
import os
import time
from datetime import datetime


# ==============================
# Connect System Monitor
# ==============================

SYSTEM_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "06_System"
    )
)

sys.path.insert(0, SYSTEM_PATH)

from system_monitor import full_status



# ==============================
# Main Window
# ==============================

root = tk.Tk()

root.title(
    "AARYA CORE v2.1"
)

root.geometry(
    "700x600"
)



# ==============================
# Header
# ==============================

title = tk.Label(
    root,
    text="🤖 AARYA CORE v2.1",
    font=("Arial", 24)
)

title.pack(
    pady=15
)



clock_label = tk.Label(
    root,
    font=("Arial",14)
)

clock_label.pack()



# ==============================
# Status Box
# ==============================

status_box = tk.Text(
    root,
    height=12,
    width=60,
    font=("Consolas",12)
)

status_box.pack(
    pady=15
)



# ==============================
# Progress Bars
# ==============================

cpu_bar = ttk.Progressbar(
    root,
    length=400,
    maximum=100
)

cpu_bar.pack(
    pady=5
)


ram_bar = ttk.Progressbar(
    root,
    length=400,
    maximum=100
)

ram_bar.pack(
    pady=5
)


battery_bar = ttk.Progressbar(
    root,
    length=400,
    maximum=100
)

battery_bar.pack(
    pady=5
)



# ==============================
# Update Dashboard
# ==============================

def update_dashboard():

    clock_label.config(
        text=datetime.now().strftime(
            "%d-%m-%Y  %I:%M:%S %p"
        )
    )


    status = full_status()


    status_box.delete(
        "1.0",
        tk.END
    )


    report = f"""

🧠 Brain Core       : ONLINE
⚙ Command Center    : ONLINE
💻 System Monitor   : ONLINE
📂 Automation       : ONLINE
🎙 Voice            : ONLINE
💾 Memory           : ONLINE


SYSTEM:

{status}


🤖 AARYA STATUS:
FULLY OPERATIONAL

"""


    status_box.insert(
        tk.END,
        report
    )


    # Demo bars update

    cpu_bar["value"] = 25
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