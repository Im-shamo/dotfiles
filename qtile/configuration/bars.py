from libqtile import bar, widget
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
import os

from configuration.variables import *


widget_defaults = {
    "font": mono_font,
    "fontsize": 12,
    "padding": 3,
    "background": "181e23"
}

extension_default = widget_defaults.copy()

arrow_right = {
    "decorations": [PowerLineDecoration(path = "arrow_right")]
}

def volume(**kwargs):
    return widget.Volume(
        font=mono_font,
        fmt="  {:^2}",
        background=colours["YELLOW"],
        mouse_callbacks={"Button3": lazy.spawn("pavucontrol --tab=3")},
        mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
        check_mute_command="pactl get-sink-mute @DEFAULT_SINK@",
        check_mute_string="Mute: yes",
        get_volume_command="pactl get-sink-volume @DEFAULT_SINK@ | grep -P -o '[0-9]+%' | head -1",
        volume_down_command="pactl set-sink-volume @DEFAULT_SINK@ -1%",
        volume_up_command="pactl set-sink-volume @DEFAULT_SINK@ +1%",
        **kwargs
    )

def microphone(**kwargs):
    return widget.Volume(
        font=mono_font,
        fmt="  {:^2}",
        background=colours["YELLOW"],
        mouse_callbacks={"Button3": lazy.spawn("pavucontrol --tab=4")},
        mute_command="pactl set-source-mute @DEFAULT_SOURCE@ toggle",
        check_mute_command="pactl get-source-mute @DEFAULT_SOURCE@",
        check_mute_string="Mute: yes",
        get_volume_command="pactl get-source-volume @DEFAULT_SOURCE@ | grep -P -o '[0-9]+%' | head -1",
        # volume_down_command="pactl set-source-volume @DEFAULT_SOURCE@ -1%",
        # volume_up_command="pactl set-source-volume @DEFAULT_SOURCE@ +1%",
        **kwargs
    )

def wallpaper_switcher(**kwargs):
    return widget.TextBox(
        fmt="Switch Wallpaper  ",
        mouse_callbacks={
            "Button1": lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/nitrogen_wallpaper_changer.sh")),
            "Button3": lazy.spawn("nitrogen")
            },
        background=colours["PURPLE"],
        **kwargs
    )

def group_box(**kwargs):
    internal_colours = {
        "active": "7cc942",
        "this_screen": colours["LIGHT_BLUE"],
        "not_this_screen": "6A6A6A",
        "highlight": ['223538', '223538'],
    }
    return widget.GroupBox(
        hide_unused = True,
        borderwidth = 3,
        disable_drag = True,
        active = internal_colours["active"],
        inactive = internal_colours["not_this_screen"],
        highlight_method = "line",
        highlight_color = internal_colours["highlight"],
        this_screen_border = internal_colours["this_screen"],
        this_current_screen_border = internal_colours["this_screen"],
        other_screen_border = internal_colours["not_this_screen"],
        other_current_screen_border = internal_colours["not_this_screen"],
        foreground = internal_colours["not_this_screen"],
        **kwargs
    )

def power_button(**kwargs):
    return widget.TextBox(
        fmt="󰐥",
        fontsize=26,
        mouse_callbacks={"Button1": lazy.spawn("rofi -show power-menu -modi 'power-menu:~/Clone/dotfiles/qtile/scripts/rofi-power-menu --choices=shutdown/reboot/suspend/logout'")},
        #mouse_callbacks = {"Button1": lazy.spawn("nwgbar")},
        **kwargs
    )

# TODO: Add wayland
bars: dict[bar.Bar] = {
    "main": bar.Bar(
        [
            widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
            group_box(),
            widget.WindowName(),
            widget.Notify(),
            widget.Systray(),
            widget.TextBox(**arrow_right),
            wallpaper_switcher(**arrow_right),
            widget.Net(font=mono_font, format= " {down:^5.1f}{down_suffix:<2}", background=colours["BLUE"],**arrow_right),  # blue
            widget.Net(font=mono_font, format= " {up:^5.1f}{up_suffix:<2}", background=colours["DARK_GREEN"],**arrow_right),  # green
            widget.NetGraph(
                mouse_callbacks={"Button1": lazy.spawn("networkmanager_dmenu")},
                background=colours["GREEN"],
                graph_color="215578",
                type="line",
                line_width=2,
                **arrow_right,
            ),
            volume(),
            microphone(**arrow_right),
            widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
            widget.Battery(format="  {percent:.0%}",emoji=True,background=colours["BLUE"], **arrow_right),
            power_button(),
            widget.Spacer(length=5),
        ],
        26,
        opacity = 1,
        margin = bar_margin
    ),

    "secondary": bar.Bar(
        [
            widget.CurrentLayoutIcon(),
            group_box(),
            widget.WindowName(),
            widget.TextBox(**arrow_right),
            widget.Clock(format="%d/%m/%Y %a %I:%M %p", background="1d6ac9", **arrow_right),   # Light blue
            power_button(),
            widget.Spacer(length=5),
        ],
        26,
        opacity = 1,
        margin = bar_margin
    ),

    "virt": bar.Bar(
        [
            widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
            group_box(),
            widget.WindowName(),
            widget.Notify(),
            widget.Systray(),
            widget.TextBox(**arrow_right),
            volume(**arrow_right),
            widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
            power_button(),
            widget.Spacer(length=5),
        ],
        26,
        opacity = 1,
        margin = bar_margin
    )
}

