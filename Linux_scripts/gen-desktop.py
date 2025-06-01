#!/bin/python3
import os
import argparse

def create_desktop_file(executable_location, name, icon_path=None):
    """
    Creates a Linux .desktop file with the given inputs.

    Args:
        executable_location (str): The path to the executable file.
        name (str): The name of the application.
        icon_path (str, optional): The path to the application's icon file. If not provided, the .desktop file will not have an icon.
    """
    desktop_file_content = f"""
[Desktop Entry]
Name={name}
Exec={executable_location}
Type=Application
"""

    if icon_path:
        desktop_file_content += f"Icon={icon_path}\n"

    desktop_file_path = os.path.join(os.path.expanduser("~"), ".local", "share", "applications", f"{name.replace(' ', '-')}.desktop")
    if os.path.isfile(desktop_file_path):
        raise FileExistsError

    with open(desktop_file_path, "w") as file:
        file.write(desktop_file_content.strip())

    print(f"Desktop file created: {desktop_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Linux .desktop file.")
    parser.add_argument("executable_location", help="The path to the executable file.")
    parser.add_argument("name", help="The name of the application.")
    parser.add_argument("--icon", dest="icon_path", help="The path to the application's icon file (optional).")

    args = parser.parse_args()

    create_desktop_file(args.executable_location, args.name, args.icon_path)
