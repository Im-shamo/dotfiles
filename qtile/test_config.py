from libqtile import qtile
from libqtile.backend.wayland import InputConfig

from configuration import *

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = False
auto_minimize = False
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True
wl_xcursor_theme = "Hikari"
wl_xcursor_size = 24
wl_input_rules = {
    "type:touchpad": InputConfig(tap=True)
}
idle_timers = []  # type: list
idle_inhibitors = []  # type: list
wmname = "LG3D"
