from modules.time_module import get_time, get_date
from modules.commands import process_command
from modules.memory import save_memory, load_memory
from modules.logger import log_activity
from modules.config import load_config


config = load_config()

print("================================")
print("Hello, I am AARYA AI System")
print("System:", config["assistant_name"])
print("Version:", config["version"])
print("================================")


memory = load_memory()

if memory["name"] == "":
    name = input("Your name: ")
    save_memory(name)
else:
    name = memory["name"]
    print("I remember you,", name)


print("Welcome", name)
print("AARYA is ready 🚀")

log_activity(f"AARYA started. User: {name}")


while True:

    command = input("\nEnter command: ").lower()

    log_activity(f"Command used: {command}")


    if command == "time":
        print("Current time is", get_time())


    elif command == "date":
        print("Today's date is", get_date())


    elif command == "exit":
        print("AARYA shutting down")
        log_activity("AARYA shutdown")
        break


    else:
        response = process_command(command, name)
        print(response)