# ==========================================
# AARYA AI v2.6
# API Connector Core
# ==========================================

from datetime import datetime
import json


# ==========================================
# AARYA System Status
# ==========================================

def get_status():

    status = {

        "system": "AARYA AI",

        "version": "v2.6",

        "status": "ONLINE",

        "brain_core": "READY",

        "voice_module": "READY",

        "memory_system": "ACTIVE",

        "automation_engine": "READY",

        "time": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    }

    return status



# ==========================================
# Test Response
# ==========================================

if __name__ == "__main__":

    response = get_status()

    print(
        json.dumps(
            response,
            indent=4
        )
    )