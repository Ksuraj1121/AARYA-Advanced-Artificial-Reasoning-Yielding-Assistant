# ==============================
# AARYA System Status Module v0.6
# ==============================

import platform
import psutil


def get_system_status():

    # System information
    system = platform.system()
    version = platform.version()
    computer = platform.node()
    processor = platform.processor()


    # CPU and RAM
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent


    # Battery (Laptop)
    battery = psutil.sensors_battery()

    if battery:

        battery_percent = battery.percent

        if battery.power_plugged:
            charging = "charging"

        else:
            charging = "not charging"

    else:

        battery_percent = "Not available"
        charging = "Not available"



    # Final Response

    status = (
        f"System is {system}. "
        f"Computer name is {computer}. "
        f"Processor is {processor}. "
        f"CPU usage is {cpu} percent. "
        f"RAM usage is {ram} percent. "
        f"Battery is {battery_percent} percent and {charging}."
    )


    return status



# ==============================
# Test Mode
# ==============================

if __name__ == "__main__":

    print("AARYA System Status 🖥️")

    print(get_system_status())