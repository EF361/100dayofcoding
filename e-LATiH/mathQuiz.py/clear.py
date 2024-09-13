import os
import platform


def clear():
    # Get the name of the operating system
    os_name = platform.system()

    # For Windows
    if os_name == "Windows":
        os.system("cls")
    # For Linux and macOS
    else:
        os.system("clear")
