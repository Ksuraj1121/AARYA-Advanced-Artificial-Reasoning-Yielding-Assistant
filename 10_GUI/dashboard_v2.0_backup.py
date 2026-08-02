# ==============================
# AARYA GUI Dashboard v2.0
# Core Status Interface
# ==============================

import tkinter as tk
import sys
import os


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
# Dashboard Window
# ==============================

root = tk.Tk()

root.title(
    "AARYA CORE v2.0"
)

root.geometry(
    "600x500"
)



# ==============================
# Title
# ==============================

title = tk.Label(
    root,
    text="🤖 AARYA CORE v2.0",
    font=("Arial", 22)
)

title.pack(
    pady=20
)



# ==============================
# Status Area
# ==============================

status_text = tk.Text(
    root,
    height=15,
    width=55,
    font=("Consolas", 12)
)

status_text.pack(
    pady=10
)



# ==============================
# Load Status
# ==============================

def update_status():

    status_text.delete(
        "1.0",
        tk.END
    )


    status = full_status()


    report = f"""
================================

🧠 Brain          ONLINE

⚙ Commands       ONLINE

💻 System         ONLINE

📂 Automation     ONLINE

🎙 Voice          ONLINE

💾 Memory         ONLINE


SYSTEM STATUS:

{status}


Status:

FULLY OPERATIONAL

================================
"""


    status_text.insert(
        tk.END,
        report
    )



# ==============================
# Button
# ==============================

button = tk.Button(
    root,
    text="Check AARYA Status",
    command=update_status,
    font=("Arial", 12)
)

button.pack(
    pady=10
)



# Initial Load

update_status()



# ==============================
# Start GUI
# ==============================

root.mainloop()