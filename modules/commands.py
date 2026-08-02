def process_command(command, name):

    if command == "hello":
        return f"Hello {name}, I am AARYA"

    elif command == "status":
        return "All systems are running"

    elif command == "help":
        return "Commands: hello, status, time, date, exit"

    elif command == "about":
        return "AARYA is a personal AI assistant project"

    else:
        return "Command not recognized"