from libqtile import layout
from libqtile.config import Match, Drag, Click
from libqtile.lazy import lazy

from configuration.variables import *

floating_layout = layout.Floating(
    border_focus=border_focus_colour,
    border_normal=border_normal_colour,
    border_width=border_width,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),             # gitk
        Match(wm_class="makebranch"),               # gitk
        Match(wm_class="maketag"),                  # gitk
        Match(wm_class="ssh-askpass"),              # ssh-askpass
        Match(title="branchdialog"),                # gitk
        Match(title="pinentry"),                    # GPG key password entry
        Match(wm_class="Conky-Sysinfo"),
        Match(wm_class="gnome-screenshot"),
        Match(wm_class="clipse")
    ]
)

