from libqtile import hook, qtile
import os
import subprocess

from configuration.variables import *
from configuration.environment_varables import set_environment_varables

@hook.subscribe.startup_once
def startup_once():
    set_environment_varables()
    if qtile.core.name == "x11":
        subprocess.Popen(os.path.join(scripts_dir, "x11_startup.sh"))
    elif qtile.core.name == "wayland":
        subprocess.Popen(os.path.join(scripts_dir, "wayland_startup.sh"))
    else:
        pass
