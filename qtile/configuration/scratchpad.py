from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy

from configuration.variables import *
from configuration.keybinds import keys
from configuration.groups import groups

terminal_scratch_pad = {
    "scratch_pad": ScratchPad(
        "terminal_apps_scratch_pad",
        [
            DropDown(
                "clipse",
                f"{terminal} --class clipse 'clipse'",
                on_focus_lost_hide = False,
                height = 0.4,
                width = 0.4,
                x = 0.3,
                y = 0.3,
            )
        ]
    ),
    "keys": [
        Key([mod], "v", lazy.group["terminal_apps_scratch_pad"].dropdown_toggle("clipse"))
    ]
}

groups.append(terminal_scratch_pad["scratch_pad"])
keys.extend(terminal_scratch_pad["keys"])
