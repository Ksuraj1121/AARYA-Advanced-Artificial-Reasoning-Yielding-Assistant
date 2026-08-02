# ==============================
# AARYA File Control v1.4
# ==============================

import os


BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


def open_folder(command):

    command = command.lower()


    if "aarya" in command:

        path = BASE_PATH


    elif "desktop" in command:

        path = os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )


    elif "documents" in command:

        path = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )


    else:

        return "Folder not found"



    if os.path.exists(path):

        os.startfile(path)

        return "Opening folder"


    return "Folder does not exist"



def create_folder(command):

    name = command.replace(
        "create folder",
        ""
    ).strip()


    if name == "":

        return "Please tell folder name"



    path = os.path.join(
        BASE_PATH,
        name
    )


    os.makedirs(
        path,
        exist_ok=True
    )


    return f"Folder {name} created"



def list_files():

    files = os.listdir(BASE_PATH)


    return (
        "Files are: "
        + ", ".join(files)
    )



def file_command(command):

    command = command.lower()


    if "create folder" in command:

        return create_folder(command)


    elif "list" in command:

        return list_files()


    else:

        return open_folder(command)