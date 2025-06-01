from libqtile import hook, qtile
import os
import subprocess

from configuration.variables import *
from configuration.environment_varables import set_environment_varables

if qtile.core.name == "x11":
    @hook.subscribe.startup_once
    def startup_once():
        subprocess.Popen(os.path.join(scripts_dir, "x11_startup.sh"))
        set_environment_varables()

elif qtile.core.name == "wayland":
    @hook.subscribe.startup_once
    def startup_once():
        set_environment_varables()