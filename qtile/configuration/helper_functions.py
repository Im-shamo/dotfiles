from libqtile.lazy import lazy
from libqtile import qtile

@lazy.function
def swap_screens(qtile):
    group_0 = qtile.screens[0].group
    group_1 = qtile.screens[1].group

    group_0.toscreen(screen=1)
    group_1.toscreen(screen=0)