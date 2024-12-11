from libqtile.config import Screen

from configuration.bars import bars

# TODO: Add wayland
screens = [
    # Screen(top = bars["main"]),
    # Screen(top = bars["secondary"]),
    Screen(top = bars["virt"]),
]