import os
from configuration.variables import *


def set_environment_varables(backend = "x11"):
    os.environ["PATH"] = f"{os.path.expanduser("~/.local/bin")}:{os.path.expanduser("~/.config/rofi/applets/bin")}:{os.path.expanduser("~/.config/rofi/scripts")}:{os.environ["PATH"]}"
    os.environ["EDITOR"] = "vim"
    os.environ["VISUAL"] = "vim"
    os.environ["BROWSER"] = browser
    
    # Theming
    os.environ["QT_QPA_PLATFORMTHEME"] = "kde"
    os.environ["XCURSOR_PATH"] = os.path.expanduser("~/.local/share/icons")
    # ssh
    os.environ["SSH_AUTH_SOCK"] = f"{os.path.join(os.environ["XDG_RUNTIME_DIR"], "gcr", "ssh")}"

    # Dolphin fix
    os.environ["XDG_MENU_PREFIX"] = "arch-"