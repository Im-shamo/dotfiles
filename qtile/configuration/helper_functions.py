from libqtile.lazy import lazy
import subprocess
import json
import os.path

from configuration.variables import *

@lazy.function
def swap_screens(qtile):
    if len(qtile.screens) == 2:
        group_0 = qtile.screens[0].group
        group_1 = qtile.screens[1].group

        group_0.toscreen(screen=1)
        group_1.toscreen(screen=0)
    else:
        pass


def is_desktop():
    result = subprocess.run(["hostnamectl", "chassis"], capture_output = True, text=True)
    if result.stdout:
        return result.stdout[:-1] == "desktop"
    else:
        return False

@lazy.function
def run_script(qtile, script: str):
    result = subprocess.run([os.path.join(scripts_dir,script)], capture_output=True, text=True)
    return result
