from libqtile.lazy import lazy
import subprocess
import os

from configuration.variables import *
@lazy.function
def swap_screens(qtile):
    group_0 = qtile.screens[0].group
    group_1 = qtile.screens[1].group

    group_0.toscreen(screen=1)
    group_1.toscreen(screen=0)