from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy

from configuration.variables import *
from configuration.keybinds import keys
from configuration.groups import groups

groups.extend([
    ScratchPad(
        "terminals",
        [
            DropDown(
                "clipse",
                f"{terminal} --class clipse -e clipse",
                on_focus_lost_hide = False,
                height = 0.4,
                width = 0.4,
                x = 0.3,
                y = 0.3,
            ),
            DropDown(
                "btop",
                f"{terminal} --class btop -e btop",
                on_focus_host_hide = False,
                height = 0.5,
                width = 0.5,
                x = 0.25,
                y = 0.25,
            )
        ]
    )
])

keys.extend([
    Key([mod], 'v', lazy.group["terminals"].dropdown_toggle("clipse")),
    Key([mod], 's', lazy.group["terminals"].dropdown_toggle("btop")),
])
