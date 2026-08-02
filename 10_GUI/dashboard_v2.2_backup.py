# ==============================
# AARYA GUI Dashboard v2.2
# Real Core Health Monitor
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
# Connect Core Status
# ==============================

sys.path.insert(
    0,
    os.path.dirname(__file__)
)


from core_status import check_core



# ==============================
# Main Window
# ==============================

root = tk.Tk()

root.title(
    "AARYA CORE v2.2"
)

root.geometry(
    "750x650"
)



# ==============================
# Header
# ==============================

title = tk.Label(
    root,
    text="🤖 AARYA CORE v2.2",
    font=("Arial",24)
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
# Module Status
# ==============================

module_box = tk.Text(
    root,
    height=15,
    width=65,
    font=("Consolas",12)
)

module_box.pack(
    pady=15
)



# ==============================
# System Bars
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
# Dashboard Update
# ==============================

def update_dashboard():


    clock_label.config(
        text=datetime.now().strftime(
            "%d-%m-%Y  %I:%M:%S %p"
        )
    )


    modules = check_core()


    online = 0


    report = """

==============================
 AARYA DIAGNOSTIC PANEL v2.2
==============================

"""


    for name, status in modules.items():

        if status == "ONLINE":

            online += 1


        report += (
            f"🟢 {name:<20}: {status}\n"
            if status == "ONLINE"
            else
            f"🔴 {name:<20}: {status}\n"
        )



    health = int(
        (online / len(modules)) * 100
    )


    system = full_status()


    report += f"""

==============================

Modules Online : {online}/{len(modules)}

AARYA Health   : {health}%

SYSTEM STATUS:

{system}


🤖 STATUS:
FULLY OPERATIONAL

==============================

"""


    module_box.delete(
        "1.0",
        tk.END
    )


    module_box.insert(
        tk.END,
        report
    )


    # System bars

    cpu_bar["value"] = 20
    ram_bar["value"] = 80
    battery_bar["value"] = 90



    root.after(
        2000,
        update_dashboard
    )



# ==============================
# Start AARYA
# ==============================

update_dashboard()

root.mainloop()