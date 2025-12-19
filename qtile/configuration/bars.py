from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from configuration.variables import *
from configuration.widgets import arrow_right, my_widgets
from configuration.helper_functions import run_script

class MyBars:
    def main_bar_x11_desktop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
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
                my_widgets.volume(),
                my_widgets.microphone(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )
    def main_bar_x11(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
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
                my_widgets.volume(),
                my_widgets.microphone(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
                widget.Battery(format="  {percent:.0%}",emoji=True,background=colours["BLUE"], **arrow_right),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )
    def secondary_bar_x11(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.TextBox(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background="1d6ac9", **arrow_right),   # Light blue
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )
    
    def small_screen_bar_x11(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                my_widgets.volume(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
                widget.Battery(format="  {percent:.0%}",emoji=True,background=colours["BLUE"], **arrow_right),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )

    def virt_bar(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.TextBox(**arrow_right),
                my_widgets.volume(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )

    # TODO: Add wayland
    def main_bar_wayland(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.StatusNotifier(), # As systray is no available in wayland
                widget.TextBox(**arrow_right),
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
                my_widgets.volume(),
                my_widgets.microphone(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
                widget.Battery(format="  {percent:.0%}",emoji=True,background=colours["BLUE"], **arrow_right),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )

    def main_bar_wayland_desktop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.StatusNotifier(), # As systray is not available in wayland
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
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
                my_widgets.volume(),
                my_widgets.microphone(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )

    def secondary_bar_wayland(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.TextBox(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background="1d6ac9", **arrow_right),   # Light blue
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )

    def main_bar_wayland_small(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.StatusNotifier(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                my_widgets.volume(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
                widget.Battery(format="  {percent:.0%}",emoji=True,background=colours["BLUE"], **arrow_right),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )

    def main_bar_wayland_small_desktop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.StatusNotifier(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                my_widgets.volume(**arrow_right),
                widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=colours["LIGHT_BLUE"], **arrow_right),   # cyan
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            26,
            opacity = 1,
            margin = bar_margin
        )

my_bars = MyBars()

