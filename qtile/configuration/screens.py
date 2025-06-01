from libqtile.config import Screen
from libqtile import qtile

from configuration.bars import my_bars

# TODO: Add wayland
if qtile.core.name == "x11":
    screens = [
        Screen(top = my_bars.small_screen_bar_x11()),
    ]

elif qtile.core.name == "wayland":
    screens = [

    ]
