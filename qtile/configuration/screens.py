from libqtile.config import Screen
from libqtile import qtile

from configuration.bars import my_bars

# TODO: Add wayland
if qtile.core.name == "x11":
    screens = [
        Screen(top = my_bars.main_bar_x11_desktop()),
    ]

elif qtile.core.name == "wayland":
    screens = [
        Screen(top = my_bars.main_bar_wayland_desktop()),
    ]
