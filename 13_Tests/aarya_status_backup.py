# ==============================
# AARYA System Status Checker v1.0
# ==============================

import os


modules = {

"Brain Core":
"02_Core/brain.py",

"Command Center":
"05_Commands/commands.py",

"System Monitor":
"06_System/system_monitor.py",

"File Automation":
"09_Automation/file_control.py",

"Project Builder":
"09_Automation/project_builder.py",

"Voice Module":
"04_Voice",

"Memory System":
"05_Memory",

"Vision System":
"08_Vision",

"GUI System":
"10_GUI",

"Hardware System":
"11_Hardware"

}


print("\n==============================")
print(" AARYA SYSTEM STATUS REPORT")
print("==============================\n")


completed = 0
total = len(modules)


for name,path in modules.items():

    if os.path.exists(path):

        print("✅",name,"ONLINE")

        completed += 1

    else:

        print("❌",name,"NOT READY")



print("\n==============================")

percentage = int(
    (completed/total)*100
)

print(
    f"AARYA Completion: {percentage}%"
)

print("==============================")