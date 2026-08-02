# ==============================
# AARYA Diagnostic Engine v1.0
# Final Base Release
# System Health Check
# ==============================


import sys
import os



# ==============================
# Base Path
# ==============================

BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)



# ==============================
# Check Module
# ==============================

def check_module(
    name,
    path
):

    if os.path.exists(path):

        print(
            f"✅ {name:<20}: ONLINE"
        )

        return True


    else:

        print(
            f"❌ {name:<20}: OFFLINE"
        )

        return False



# ==============================
# Header
# ==============================

print(
"""
================================
     AARYA DIAGNOSTIC ENGINE
          FINAL BASE v1.0
================================
"""
)



# ==============================
# Modules
# ==============================

modules = [

    (
        "Brain Core",
        "02_Core"
    ),

    (
        "Assistant",
        "03_Assistant"
    ),

    (
        "Command Center",
        "05_Commands"
    ),

    (
        "System Monitor",
        "06_System"
    ),

    (
        "Automation",
        "09_Automation"
    ),

    (
        "GUI System",
        "10_GUI"
    ),

    (
        "Voice Module",
        "04_Voice"
    ),

    (
        "Memory System",
        "05_Memory"
    ),

    (
        "Vision System",
        "08_Vision"
    ),

    (
        "Hardware System",
        "11_Hardware"
    )

]



online = 0



for name, folder in modules:


    path = os.path.join(
        BASE_PATH,
        folder
    )


    if check_module(
        name,
        path
    ):

        online += 1



# ==============================
# Result
# ==============================

total = len(modules)


health = int(
    (online / total) * 100
)



print(
"""
================================
"""
)


print(
    f"Modules Online : {online}/{total}"
)


print(
    f"AARYA Health   : {health}%"
)



print(
"""
================================
"""
)



if health == 100:

    print(
        "🤖 AARYA STATUS: FULLY OPERATIONAL"
    )


elif health >= 70:

    print(
        "⚠ AARYA STATUS: PARTIALLY OPERATIONAL"
    )


else:

    print(
        "❌ AARYA STATUS: SYSTEM CHECK REQUIRED"
    )



print(
"""
================================
"""
)