import os
from configuration.variables import *


def set_environment_varables(backend = "x11"):
    # Theming
    os.environ["QT_QPA_PLATFORMTHEME"] = "qt6ct"
    # Session
    os.environ["XDG_SESSION_DESKTOP"] = "qtile"
