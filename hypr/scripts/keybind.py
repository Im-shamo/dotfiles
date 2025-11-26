#!/usr/bin/env python
import os
def keybinds(file_path: str) -> list[list]:
    MOD_KEYS = ["super", "alt", "ctrl", "shift"]
    with open(os.path.expanduser("~/Clone/dotfiles/hypr/hyprland.conf"), "r") as text:
        lines = text.readlines()
        keybind_lines = [ line for line in lines if "bind" in line ]
        # to strip away to bind, binde, =, \n
        parsed_keybind_lines: list[list[str]] = []
        for line in keybind_lines:
            temp = line.rstrip('\n').split("=")[1:]
            temp = temp[0].split(",") if len(temp) >= 1 else []
            parsed_keybind_lines.append(temp)

        # Structure is [[mod keys], [keys], [dispatcher], ... ]
        binds = []
        for line in parsed_keybind_lines:
            temp = []
            if len(line) == 0:
                continue
            temp_mod = line[0].strip().lower()
            temp_key = line[1].strip()
            temp_dispatcher = line[2].strip()
            if len(line) > 3:
                temp_arguments = line[3:]
                temp_arguments = [ string.strip() for string in temp_arguments ]
            else:
                temp_arguments = []

            mod = []
            if "$mainmod" in temp_mod:
                # temp_mod = temp_mod.replace("$mainmod", "")
                mod.append(MOD_KEYS[0])
            if MOD_KEYS[1] in temp_mod:
                # temp_mod = temp_mod.replace(MOD_KEYS[1], "")
                mod.append(MOD_KEYS[1])
            if MOD_KEYS[2] in temp_mod:
                # temp_mod = temp_mod.replace(MOD_KEYS[2], "")
                mod.append(MOD_KEYS[2])
            if MOD_KEYS[3] in temp_mod:
                # temp_mod = temp_mod.replace(MOD_KEYS[3], "")
                mod.append(MOD_KEYS[3])


            temp.append(mod)
            temp.append([temp_key])
            temp.append([temp_dispatcher])
            temp.append(temp_arguments)
            binds.append(temp)
    return binds


def main():
    [ print(line) for line in keybinds(os.path.expanduser("~/.config/hypr/hyprland.conf"))]

if __name__ == "__main__":
    main()