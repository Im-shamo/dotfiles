from libqtile import hook, qtile
import os
import subprocess

from configuration.variables import *

if qtile.core.name == "x11":

    @hook.subscribe.startup_once
    def startup_once():
        subprocess.Popen(os.path.json(scripts_dir, "x111_starup.sh"))

        ### Environment Variables ###
        # TODO: add environment variables
        os.environ["PATH"] = f"{os.path.expanduser("~/.local/bin")}:{os.environ["PATH"]}"
        os.environ["EDITOR"] = "vim"
        os.environ["VISUAL"] = "vim"
        os.environ["BROWSER"] = browser

        # hack to get qt apps to look correct
        os.environ["QT_QPA_PLATFORMTHEME"] = "kde"

        # ssh
        os.environ["SSH_AUTH_SOCK"] = f"{os.path.join(os.environ["XDG_RUNTIME_DIR"], "gcr", "ssh")}"