from libqtile.config import Group, Key
from libqtile.lazy import lazy

from configuration.keybinds import keys
from configuration.variables import *

groups = []

my_groups = [
    ({"name": " ",     "matches": [], "spawn": []}, "1"),
    ({"name": " ",     "matches": [], "spawn": []}, "2"),
    ({"name": " ",     "matches": [], "spawn": []}, "3"),
    ({"name": " ",     "matches": [], "spawn": []}, "4"),
    ({"name": " ",     "matches": [], "spawn": []}, "5"),
    ({"name": " ",     "matches": [], "spawn": []}, "6"),
    ({"name": " ",     "matches": [], "spawn": []}, "7"),
    ({"name": "8",      "matches": [], "spawn": []}, "8"),
    ({"name": "9",      "matches": [], "spawn": []}, "9"),
    ({"name": "0",      "matches": [], "spawn": []}, "0"),
]

for my_group in my_groups:
    group_key = my_group[1]

    group = Group(**my_group[0])
    groups.append(group)
    keys.extend(
        [
            Key(
                [mod],
                group_key,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name), 
            ),

            Key(
                [mod, "shift"], 
                group_key,
                lazy.window.togroup(group.name, switch_group=True),
                desc="move focused window to group {}".format(group.name)
            ),

            Key(
                [mod, "mod1"], 
                group_key,
                lazy.window.togroup(group.name),
                desc="move focused window to group {}".format(group.name)
            ),
        ]
    )


