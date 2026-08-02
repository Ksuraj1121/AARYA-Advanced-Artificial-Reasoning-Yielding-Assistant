# ==============================
# AARYA System Monitor v1.0
# CPU + RAM + Battery + Windows Info
# ==============================

import psutil
import platform


# ==============================
# CPU Status
# ==============================

def cpu_status():

    cpu = psutil.cpu_percent(
        interval=1
    )

    return f"CPU usage is {cpu}%"



# ==============================
# RAM Status
# ==============================

def ram_status():

    ram = psutil.virtual_memory()

    used = ram.percent

    return f"RAM usage is {used}%"



# ==============================
# Battery Status
# ==============================

def battery_status():

    battery = psutil.sensors_battery()

    if battery:

        return (
            f"Battery level is "
            f"{battery.percent}%"
        )

    return "Battery information not available."



# ==============================
# System Information
# ==============================

def system_info():

    system = platform.system()

    version = platform.version()

    return (
        f"System is {system}. "
        f"Version {version}"
    )



# ==============================
# Full Status
# ==============================

def full_status():

    return (
        cpu_status()
        + ". "
        + ram_status()
        + ". "
        + battery_status()
        + ". "
        + system_info()
    )