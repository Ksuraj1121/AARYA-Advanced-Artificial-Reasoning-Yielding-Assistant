import psutil
import platform
import socket


def get_system_info():
    """
    Returns current system information.
    """

    return {
        "cpu": psutil.cpu_percent(interval=0.5),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,

        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.release(),

        "cpu_count": psutil.cpu_count(logical=True),

        "boot_time": psutil.boot_time(),

        "network_sent": psutil.net_io_counters().bytes_sent,
        "network_recv": psutil.net_io_counters().bytes_recv,
    }