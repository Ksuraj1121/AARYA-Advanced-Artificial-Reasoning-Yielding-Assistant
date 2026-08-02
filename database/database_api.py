# ==============================
# AARYA Database API
# Version: v1.0
# Profile Access Layer
# ==============================


from profile import (
    get_founder,
    get_founder_name,
    get_aarya_status
)



# ==============================
# Get Full Founder Data
# ==============================

def get_profile():

    return get_founder()



# ==============================
# Get Founder Name
# ==============================

def get_name():

    return get_founder_name()



# ==============================
# Get AARYA Status
# ==============================

def get_status():

    return get_aarya_status()



# ==============================
# Test
# ==============================

if __name__ == "__main__":


    print(
        "=============================="
    )

    print(
        " AARYA DATABASE API ONLINE"
    )

    print(
        "=============================="
    )


    print()

    print(
        "Founder:",
        get_name()
    )


    print(
        "Status:",
        get_status()
    )


    print()

    print(
        get_profile()
    )