from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile import qtile

from configuration.variables import *
from configuration.helper_functions import run_script

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

class MyWidgets:
    def __init__(self, colours: dict[str, str] = colours):
        self.colours = colours

    def volume(self, **kwargs):
        return widget.Volume(
            fmt="  {:^2}",
            background=self.colours["YELLOW"],
            mouse_callbacks={"Button3": lazy.spawn("pavucontrol --tab=3")},
            mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
            check_mute_command="pactl get-sink-mute @DEFAULT_SINK@",
            check_mute_string="Mute: yes",
            get_volume_command="pactl get-sink-volume @DEFAULT_SINK@ | grep -P -o '[0-9]+%' | head -1",
            volume_down_command="pactl set-sink-volume @DEFAULT_SINK@ -1%",
            volume_up_command="pactl set-sink-volume @DEFAULT_SINK@ +1%",
            **kwargs
        )

    def microphone(self, **kwargs):
        return widget.Volume(
            fmt="  {:^2}",
            background=self.colours["YELLOW"],
            mouse_callbacks={"Button3": lazy.spawn("pavucontrol --tab=4")},
            mute_command="pactl set-source-mute @DEFAULT_SOURCE@ toggle",
            check_mute_command="pactl get-source-mute @DEFAULT_SOURCE@",
            check_mute_string="Mute: yes",
            get_volume_command="pactl get-source-volume @DEFAULT_SOURCE@ | grep -P -o '[0-9]+%' | head -1",
            # volume_down_command="pactl set-source-volume @DEFAULT_SOURCE@ -1%",
            # volume_up_command="pactl set-source-volume @DEFAULT_SOURCE@ +1%",
            **kwargs
        )

    def wallpaper_switcher(self, **kwargs):
        if qtile.core.name == "x11":
            launch_waypaper = lazy.spawn("waypaper --backend feh")
        else:
            launch_waypaper = lazy.spawn("waypaper --backend swww")
        return widget.TextBox(
            fmt="Switch Wallpaper  ",
            mouse_callbacks={
                "Button1": lazy.spawn("waypaper --random"),
                "Button3": launch_waypaper
                },
            background=self.colours["PURPLE"],
            **kwargs
        )

    def group_box(self, **kwargs):
        internal_colours = {
            "active": "7cc942",
            "this_screen": self.colours["LIGHT_BLUE"],
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

    def power_button(self, **kwargs):
        return widget.TextBox(
            fmt="󰐥",
            fontsize=26,
            mouse_callbacks={"Button1": lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu/type-1/powermenu.sh"))},
            **kwargs
        )

my_widgets = MyWidgets()
