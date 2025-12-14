from libqtile.config import Screen
from libqtile import qtile

from configuration.bars import my_bars
from configuration.helper_functions import is_desktop, get_display_resolutions

display_resolutions = get_display_resolutions(qtile)

if qtile.core.name == "x11":
    if is_desktop():
        screens = [
            Screen(top = my_bars.main_bar_x11_desktop())
        ]
    else:
        screens = [
            Screen(top = my_bars.main_bar_x11())
        ]

elif qtile.core.name == "wayland":
    if is_desktop():
        screens = [
            Screen(top = my_bars.main_bar_wayland_desktop())
        ]
    else:
        screens = [
            Screen(top = my_bars.main_bar_wayland())
        ]

else:
    screens = []