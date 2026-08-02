# ==============================
# AARYA File Automation v1.0
# Final Base Release
# File + Folder Control
# ==============================


import os



# ==============================
# Open Folder
# ==============================

def open_folder(path):

    try:

        path = path.strip()


        if os.path.exists(path):

            os.startfile(path)

            return (
                f"Opening folder {path}"
            )


        return "Folder not found."


    except:

        return "Unable to open folder."



# ==============================
# Create Folder
# ==============================

def create_folder(name):

    try:

        name = name.strip()


        if name == "":

            return "Folder name missing."


        if os.path.exists(name):

            return "Folder already exists."


        os.mkdir(name)


        return (
            f"Folder {name} created."
        )


    except:

        return "Unable to create folder."



# ==============================
# Create File
# ==============================

def create_file(name):

    try:

        name = name.strip()


        if name == "":

            return "File name missing."


        with open(
            name,
            "w"
        ) as file:

            file.write("")


        return (
            f"File {name} created."
        )


    except:

        return "Unable to create file."



# ==============================
# Search File
# ==============================

def search_file(
    filename,
    location="."
):

    filename = filename.strip()


    for root, dirs, files in os.walk(location):


        for file in files:


            if file.lower() == filename.lower():


                return (
                    "File found at "
                    +
                    os.path.join(
                        root,
                        file
                    )
                )


    return "File not found."



# ==============================
# Rename File
# ==============================

def rename_file(
    old_name,
    new_name
):

    try:


        if os.path.exists(old_name):


            os.rename(
                old_name,
                new_name
            )


            return (
                f"File renamed to {new_name}"
            )


        return "Old file not found."



    except:


        return "Unable to rename file."



# ==============================
# Delete File
# ==============================

def delete_file(filename):

    try:


        if os.path.exists(filename):


            os.remove(filename)


            return (
                f"File {filename} deleted."
            )


        return "File not found."



    except:


        return "Unable to delete file."



# ==============================
# List Files
# ==============================

def list_files(
    location="."
):

    try:


        items = os.listdir(location)


        if len(items) == 0:

            return "Folder is empty."



        result = (
            "Files and folders:\n"
        )


        for item in items:

            result += (
                f"- {item}\n"
            )


        return result



    except:


        return "Unable to list files."



# ==============================
# Open File
# ==============================

def open_file(filename):

    try:


        if os.path.exists(filename):


            os.startfile(filename)


            return (
                f"Opening file {filename}"
            )


        return "File not found."



    except:


        return "Unable to open file."



# ==============================
# Read File
# ==============================

def read_file(filename):

    try:


        if os.path.exists(filename):


            with open(
                filename,
                "r"
            ) as file:


                content = file.read()



            if content == "":

                return "File is empty."



            return (
                f"File content:\n{content}"
            )



        return "File not found."



    except:


        return "Unable to read file."