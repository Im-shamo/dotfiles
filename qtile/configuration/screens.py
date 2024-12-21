from libqtile.config import Screen

from configuration.bars import my_bars

# TODO: Add wayland
screens = [
    Screen(top = my_bars.secondary_bar),
    Screen(top = my_bars.main_bar),
]