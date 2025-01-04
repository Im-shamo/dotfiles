from libqtile import qtile

if qtile.core.name == "x11":
    from configuration import *

    dgroups_key_binder = None
    dgroups_app_rules = []
    follow_mouse_focus = True
    bring_front_click = False
    floats_kept_above = True
    cursor_warp = False
    auto_minimize = False
    wl_input_rules = False
    wmname = "LG3D"

elif qtile.core.name == "wayland":
    from configuration.default_config import *