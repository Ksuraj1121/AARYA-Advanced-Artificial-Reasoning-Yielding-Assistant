# ==============================
# AARYA Assistant Layer v1.0
# Final Base Release
# ==============================


import sys
import os



# ==============================
# Connect Core Brain
# ==============================

BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


CORE_PATH = os.path.join(
    BASE_PATH,
    "02_Core"
)


sys.path.insert(
    0,
    CORE_PATH
)


from brain import get_ai_reply



# ==============================
# AARYA Startup
# ==============================

def startup():

    print(
        """
================================
     AARYA ASSISTANT v1.0
================================

🧠 Brain Core Online
⚙ Command System Online
🤖 Assistant Layer Online

Welcome back, Boss.

================================
"""
    )



# ==============================
# Main Assistant Loop
# ==============================

def main():

    startup()


    while True:


        try:

            user_input = input(
                "You: "
            )


            if user_input.lower() in [
                "exit",
                "quit",
                "bye"
            ]:


                print(
                    "AARYA: Goodbye Suraj."
                )

                break



            response = get_ai_reply(
                user_input
            )


            print(
                "AARYA:",
                response
            )



        except KeyboardInterrupt:


            print(
                "\nAARYA: Shutdown by user."
            )

            break



        except Exception as error:


            print(
                "AARYA Error:",
                error
            )



# ==============================
# Run
# ==============================

if __name__ == "__main__":

    main()