# ==============================
# AARYA Skill Router v1.3
# Calculator + App Control
# ==============================


from app_control import open_app
import re


# ==============================
# Calculator Engine
# ==============================

def calculate(expression):

    try:

        expression = expression.lower()


        expression = expression.replace(
            "is equal to",
            ""
        )

        expression = expression.replace(
            "equal to",
            ""
        )

        expression = expression.replace(
            "equals",
            ""
        )


        expression = expression.replace(
            "multiplied by",
            "*"
        )

        expression = expression.replace(
            "multiply",
            "*"
        )

        expression = expression.replace(
            "times",
            "*"
        )

        expression = expression.replace(
            "x",
            "*"
        )


        expression = expression.replace(
            "plus",
            "+"
        )

        expression = expression.replace(
            "minus",
            "-"
        )

        expression = expression.replace(
            "divided by",
            "/"
        )

        expression = expression.replace(
            "divide",
            "/"
        )


        expression = re.sub(
            r"[^0-9+\-*/().]",
            "",
            expression
        )


        result = eval(expression)

        return f"Answer is {result}"


    except:

        return "I cannot calculate this."



# ==============================
# Skill Router
# ==============================

def run_skill(skill, data=None):


    if skill == "calculator":

        return calculate(data)



    elif skill == "app_control":

        return open_app(data)



    elif skill == "greeting":

        return "Hello Boss. Skill system is online."



    elif skill == "about":

        return "AARYA Skill Router v1.3 is active."



    else:

        return "Skill not found."