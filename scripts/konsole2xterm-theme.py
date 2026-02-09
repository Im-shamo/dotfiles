#!/usr/bin/python3
import configparser
import argparse
from pathlib import Path

parser = argparse.ArgumentParser("Converts Konsole theme to xterm theme")
parser.add_argument("theme", help="File path of theme")
args = parser.parse_args()
filepath = Path(args.theme).expanduser()

with open(filepath) as f:
    conf = configparser.ConfigParser()
    conf.read_file(f)

themename = filepath.stem
print(f"!Theme: {themename}")

s = {
    "Background": "background",
    "Foreground": "foreground"
}

color_list = [
    "Black",
    "Red",
    "Green",
    "Yellow",
    "Blue",
    "Magenta",
    "Cyan",
    "White"
]

for i in range(0,8):
    s["Color" + str(i)] = "color" + str(i)
    s["Color" + str(i) + "Intense"] = "color" + str(i+8)

output = []
i = 0
for key,value in s.items():
    tmp = conf.get(key, "Color")
    tmp = tmp.split(",")
    tmp = [f"{int(v):x}" for v in tmp]
    output.append(f"*{value}: rgb: {'/'.join(tmp)}")

print("\n".join(output))
