from libqtile.config import Screen

from configuration.bars import bars

# Todo: Add wayland
screens = [
    # Screen(top = bars["main"]),
    # Screen(top = bars["secondary"]),
    Screen(top = bars["virt"]),
]