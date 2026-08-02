# ==============================
# AARYA GUI Dashboard v2.3
# Real System Monitor
# ==============================

import tkinter as tk
from tkinter import ttk

import os
import sys
from datetime import datetime


# ==============================
# Import System Monitor
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
# Import Core Status
# ==============================

GUI_PATH = os.path.dirname(__file__)

sys.path.insert(
    0,
    GUI_PATH
)


from core_status import check_core



# ==============================
# Import psutil
# ==============================

try:

    import psutil

    PSUTIL = True

except:

    PSUTIL = False



# ==============================
# Window
# ==============================

root = tk.Tk()

root.title(
    "AARYA CORE v2.3"
)

root.geometry(
    "800x700"
)



# ==============================
# Title
# ==============================

title = tk.Label(
    root,
    text="🤖 AARYA CORE v2.3",
    font=("Arial",26)
)

title.pack(
    pady=15
)



clock = tk.Label(
    root,
    font=("Arial",14)
)

clock.pack()



# ==============================
# Status Panel
# ==============================

status_box = tk.Text(
    root,
    height=20,
    width=70,
    font=("Consolas",12)
)

status_box.pack(
    pady=15
)



# ==============================
# System Bars
# ==============================

cpu_label = tk.Label(root,text="CPU")
cpu_label.pack()

cpu_bar = ttk.Progressbar(
    root,
    length=500,
    maximum=100
)

cpu_bar.pack()



ram_label = tk.Label(root,text="RAM")
ram_label.pack()

ram_bar = ttk.Progressbar(
    root,
    length=500,
    maximum=100
)

ram_bar.pack()



battery_label = tk.Label(root,text="Battery")
battery_label.pack()

battery_bar = ttk.Progressbar(
    root,
    length=500,
    maximum=100
)

battery_bar.pack()



# ==============================
# Update Function
# ==============================

def update_dashboard():


    clock.config(
        text=datetime.now().strftime(
            "%d-%m-%Y  %I:%M:%S %p"
        )
    )


    modules = check_core()


    online = 0


    report = """

==============================
 AARYA DIAGNOSTIC ENGINE v2.3
==============================

"""


    for module,status in modules.items():

        if status == "ONLINE":
            online += 1


        icon = "🟢" if status=="ONLINE" else "🔴"


        report += (
            f"{icon} {module:<22}: {status}\n"
        )


    health = int(
        (online / len(modules))*100
    )


    report += f"""

==============================

Modules Online : {online}/{len(modules)}

AARYA Health : {health}%


SYSTEM:

{full_status()}


STATUS:
FULLY OPERATIONAL

==============================

"""


    status_box.delete(
        "1.0",
        tk.END
    )


    status_box.insert(
        tk.END,
        report
    )



    # Real values

    if PSUTIL:


        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent


        battery = psutil.sensors_battery()


        cpu_bar["value"] = cpu

        ram_bar["value"] = ram


        if battery:

            battery_bar["value"] = battery.percent



    root.after(
        2000,
        update_dashboard
    )



# ==============================
# Start
# ==============================

update_dashboard()

root.mainloop()