import os
from configuration.variables import *


def set_environment_varables(backend = "x11"):
    os.environ["PATH"] = f"{os.path.expanduser('~/.local/bin')}:{os.path.expanduser('~/.config/rofi/applets/bin')}:{os.path.expanduser('~/.config/rofi/scripts')}:{os.environ['PATH']}"

    # Theming
    os.environ["QT_QPA_PLATFORMTHEME"] = "qt6ct"

    # ssh
    os.environ["SSH_AUTH_SOCK"] = f"{os.path.join(os.environ['XDG_RUNTIME_DIR'], 'gcr', 'ssh')}"

    # Dolphin fix
    os.environ["XDG_MENU_PREFIX"] = "arch-"
