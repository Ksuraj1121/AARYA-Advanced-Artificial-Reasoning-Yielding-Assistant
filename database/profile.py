# ==============================
# AARYA Founder Profile System
# Version: v1.0
# ==============================


from datetime import datetime



# ==============================
# Founder Database
# ==============================

FOUNDER_PROFILE = {


    # Founder Identity

    "founder": {

        "name": "Suraj Kamble",

        "role": "Founder & Chief Architect",

        "project": "AARYA AI",

    },


    # Vision

    "vision": {

        "mission":
        "Building an intelligent AI ecosystem for innovation, security and assistance.",


        "goal":
        "Create an advanced personal AI assistant ecosystem.",

    },


    # AARYA Information

    "aarya": {

        "name": "AARYA AI",

        "release":
        "Final Base v1.0.0",

        "upgrade":
        "v10.x Development",

        "status":
        "Locked & Stable",

    },


    # Development Information

    "development": {

        "language":
        "Python",

        "architecture":
        "Modular AI System",

        "platform":
        "Windows",

    },


    # Creation

    "created": {

        "date":
        datetime.now().strftime("%d-%m-%Y"),

        "type":
        "AI Assistant Project"

    }

}



# ==============================
# Get Full Profile
# ==============================

def get_founder():

    return FOUNDER_PROFILE



# ==============================
# Get Founder Name
# ==============================

def get_founder_name():

    return FOUNDER_PROFILE["founder"]["name"]



# ==============================
# Get AARYA Status
# ==============================

def get_aarya_status():

    return FOUNDER_PROFILE["aarya"]["status"]



# ==============================
# Display Profile
# ==============================

def display_profile():


    print(
    """
================================
      AARYA FOUNDER PROFILE
================================
"""
    )


    for section, data in FOUNDER_PROFILE.items():

        print(
            f"\n[{section.upper()}]"
        )


        if isinstance(data, dict):

            for key, value in data.items():

                if isinstance(value, dict):

                    print(
                        f"{key}:"
                    )

                    for k, v in value.items():

                        print(
                            f"  {k}: {v}"
                        )

                else:

                    print(
                        f"{key}: {value}"
                    )


    print(
    """
================================
 AARYA PROFILE LOADED
================================
"""
    )



# ==============================
# Test Run
# ==============================

if __name__ == "__main__":

    display_profile()