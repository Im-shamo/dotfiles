from libqtile import hook, qtile
import os
import subprocess

from configuration.variables import *

if qtile.core.name == "x11":

    @hook.subscribe.startup_once
    def startup_once():
        subprocess.Popen(os.path.json(scripts_dir, "x111_starup.sh"))

        ### Environment Variables ###
        # Todo: add environment variables