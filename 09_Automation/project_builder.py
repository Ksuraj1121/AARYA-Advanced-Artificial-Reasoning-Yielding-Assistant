import os


def create_project(name):

    name = name.strip()

    if name == "":
        return "Project name missing."

    if os.path.exists(name):
        return "Project already exists."

    folders = [
        "src",
        "data",
        "config",
        "docs",
        "tests",
        "assets",
        "logs"
    ]

    os.mkdir(name)

    for folder in folders:
        os.mkdir(
            os.path.join(name, folder)
        )

    with open(
        os.path.join(name, "README.md"),
        "w"
    ) as file:

        file.write(f"# {name}\n")

    with open(
        os.path.join(name, "requirements.txt"),
        "w"
    ) as file:

        file.write("")

    with open(
        os.path.join(name, "main.py"),
        "w"
    ) as file:

        file.write(
            'print("Hello from AARYA Project")'
        )

    return f"Project {name} created successfully."