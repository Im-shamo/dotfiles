from libqtile.config import Screen
from libqtile import qtile

from configuration.bars import my_bars
from configuration.helper_functions import is_desktop, get_display_resolutions

display_resolutions = get_display_resolutions(qtile)

# TODO: Add wayland
if qtile.core.name == "x11":
    screens = [
        Screen(top = my_bars.main_bar_x11_desktop()),
    ]

elif qtile.core.name == "wayland":
     if len(display_resolutions) == 0:
         if is_desktop():
             screens = [Screen(top = my_bars.main_bar_wayland_desktop())]
         else:
             screens = [Screen(top = my_bars.main_bar_wayland())]

     for name, resolution in display_resolutions.items():
         if resolution[0] > 1000:
             if is_desktop:
                 screens = [Screen(top = my_bars.main_bar_wayland_desktop())]
             else:
                 screens = [Screen(top = my_bars.main_bar_wayland())]
         else:
             if is_desktop:
                 screens = [Screen(top = my_bars.main_bar_wayland_small_desktop())]
             else:
                 screens = [Screen(top = my_bars.main_bar_wayland_small)]

else:
    screens = []