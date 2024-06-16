# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile import hook
import subprocess
import os

normal_colors={
    "red": "881111",
    "dark_red": "220000",
    "orange": "#ff9933",
    "yellow": "#b97f18",
    "green": "#72b043",
    "dark_green": "#007f4e",
    "blue": "#194a7a",
    "dark_blue": "0c0f3f",
    "light_blue": "4682b4",
    "black": "000000",
    "light_gray": "d3d3d3",
    "silver": "c0c0c0",
    "purple": "9678b6",
}

# +----------------------------+
# |                            |
# |            Keys            |
# |                            |
# +----------------------------+

file_explorer = "nemo"
mod = "mod4"
terminal = "kitty"

@lazy.function
def swap_screens(qtile):
    group_0 = qtile.screens[0].group
    group_1 = qtile.screens[1].group

    group_0.toscreen(screen=1)
    group_1.toscreen(screen=0)


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Qtile Shutdown and Reload
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "mod1"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),


    # +-------------------+
    # |                   |
    # |      windows      |
    # |                   |
    # +-------------------+

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Move windows
    Key([mod], "grave", swap_screens, desc="Swap workspace"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize windows
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    # Move Cursor
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor'),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    
    # Windows Actions
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),


    # +------------------------------------+
    # |                                    |
    # |      Application and Controls      |
    # |                                    |
    # +------------------------------------+

    # app launches
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -i -show drun -modi drun -show-icons"), desc="Launch rofi"),
    Key([], "Print", lazy.spawn("gnome-screenshot"), desc="Take screenshot"),
    Key([mod], "Print", lazy.spawn("gnome-screenshot -i"), desc="Launch gnome screenshot"),
    Key([mod], "e", lazy.spawn(file_explorer), desc="Spawn the file explorer ({file_explorer})"),

    # Media Control
    # Source    https://askubuntu.com/questions/97936/terminal-command-to-set-audio-volume and https://www.reddit.com/r/qtile/comments/v718d8/how_to_setup_media_keys/
    # Audio
    Key([],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%"),
        desc="Lower Volume by 2%"
    ),
    Key([],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"),
        desc="Raise Volume by 2%"
    ),
    Key([],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Mute/Unmute"
    ),

    # Video and audio Play
    Key([],
        "XF86AudioPlay", 
        lazy.spawn("playerctl play-pause"),
        desc="Play/Pause player"
    ),
    Key([], 
        "XF86AudioStop", 
        lazy.spawn("playerctl stop"), 
        desc="Stop audio"
    ),
    Key([],
        "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Skip to next"
    ),
    Key([],
        "XF86AudioPrev", 
        lazy.spawn("playerctl previous"),
        desc="Skip to previous"
    ),
]

# +------------------------------+
# |                              |
# |            Groups            |
# |                              |
# +------------------------------+

my_groups = {
    "Web  ": "1",
    "Code  ": "2",
    "Term  ": "3",
    "Game  ": "4",
    "Chat  ": "5",
    "Music  ": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "0",
    "F1": "F1",
    "F2": "F2",
    "F3": "F3",
    "F4": "F4",
    "F5": "F5",
    "F6": "F6",
    "F7": "F7",
    "F8": "F8",
    "F9": "F9",
    "F10": "F10",
    "F11": "F11",
    "F12": "F12",
}

my_groups_no_icon = {
    " ": "1",
    " ": "2",
    " ": "3",
    " ": "4",
    " ": "5",
    " ": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "0",
    "F1": "F1",
    "F2": "F2",
    "F3": "F3",
    "F4": "F4",
    "F5": "F5",
    "F6": "F6",
    "F7": "F7",
    "F8": "F8",
    "F9": "F9",
    "F10": "F10",
    "F11": "F11",
    "F12": "F12",
}

groups = []
for group_name, group_key in my_groups_no_icon.items():
    group = Group(group_name)
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

# +-------------------------------+
# |                               |
# |            Layouts            |
# |                               |
# +-------------------------------+

margin = [4,4,4,4]
border_focus_colour = "0066cc"  #Light blue
border_normal_colour = "004d66" #Dark Blue
border_width = 3

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp( # type: ignore
        margin = margin, 
        margin_on_single = margin, 
        border_focus = border_focus_colour,
        border_normal = border_normal_colour, 
        border_on_single = True,
        border_width = border_width,
    ),
    layout.Max( # type: ignore
        margin = margin,
        border_focus = border_focus_colour,
        border_normal = border_normal_colour,
        border_width = border_width,
    ),
    # layout.Matrix( # type: ignore
    #     margin = margin,
    #     border_focus = border_focus_colour,
    #     border_normal = border_normal_colour,
    #     border_width = border_width,
    # ),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True

cursor_warp = False
floating_layout = layout.Floating( # type: ignore
    border_focus=border_focus_colour,
    border_normal=border_normal_colour,
    border_width=border_width,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules, # type: ignore
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Conky-Sysinfo"),
        Match(wm_class="gnome-screenshot"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# +-------------------------------------+
# |                                     |
# |               Widgets               |
# |                                     |
# +-------------------------------------+

mono_font = "DroidSansM Nerd Font"

# from https://www.youtube.com/watch?v=mY1DFn8BLOU

arrow_right = {
    "decorations": [
        PowerLineDecoration(path="arrow_right")
    ]
}

def volume(**kwargs):
    return widget.Volume(
        font=mono_font,
        fmt="  {:^2}",
        background=normal_colors["yellow"],
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
        background=normal_colors["yellow"],
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
        background=normal_colors["purple"],
        **kwargs
    )

def group_box(**kwargs):
    colors = {
        "active": "7cc942",
        "this_screen": normal_colors["light_blue"],
        "not_this_screen": "6A6A6A",
        "highlight": ['223538', '223538'],
    }
    return widget.GroupBox(
        hide_unused = True,
        borderwidth = 3,
        disable_drag = True,
        active = colors["active"],
        inactive = colors["not_this_screen"],
        highlight_method = "line",
        highlight_color = colors["highlight"],
        this_screen_border = colors["this_screen"],
        this_current_screen_border = colors["this_screen"],
        other_screen_border = colors["not_this_screen"],
        other_current_screen_border = colors["not_this_screen"],
        foreground = colors["not_this_screen"],
        **kwargs
    )

def power_button(**kwargs):
    return widget.TextBox(
        fmt="󰐥",
        fontsize=26,
        mouse_callbacks={"Button1": lazy.spawn("rofi -show power-menu -modi power-menu:/home/shamokwok/Clone/dotfiles/qtile/scripts/rofi-power-menu")},
        **kwargs
    )

widget_defaults = dict(
    font='DroidSansM Nerd Font',
    fontsize=12,
    padding=3,
    background="181e23",
)

extension_defaults = widget_defaults.copy()

bar_margin = [6,4,2,4]

main_display_bar = bar.Bar(
    [
        widget.CurrentLayoutIcon(mouse_callbacks={"Button1": lazy.next_layout()}),
        group_box(),
        widget.WindowName(),
        widget.Notify(),
        widget.StatusNotifier(),
        widget.TextBox(**arrow_right),
        wallpaper_switcher(**arrow_right),
        widget.Net(font=mono_font, format= " {down:^5.1f}{down_suffix:<2}", background=normal_colors["blue"],**arrow_right),  # blue
        widget.Net(font=mono_font, format= " {up:^5.1f}{up_suffix:<2}", background=normal_colors["dark_green"],**arrow_right),  # green
        widget.NetGraph(
            mouse_callbacks={"Button1": lazy.spawn("networkmanager_dmenu")},
            background=normal_colors["green"],
            graph_color="215578",
            type="line",
            line_width=2,
            **arrow_right,
        ),
        volume(),
        microphone(**arrow_right),
        widget.Clock(format="%d/%m/%Y %a %I:%M %p", background=normal_colors["light_blue"], **arrow_right),   # cyan
        widget.Battery(format="  {percent:.0%}",emoji=True,background=normal_colors["blue"], **arrow_right),
        power_button(),
        widget.Spacer(length=5),
    ],
    26,
    opacity = 1,
    margin = bar_margin
)

desktop_display_bar = bar.Bar(
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
)

if qtile.core.name == "x11":
    screens = [
        # Disktop Display
        Screen(top=desktop_display_bar),
        # Main Display
        Screen(top=main_display_bar),
    ]
else:
    screens = [
        # Desktop Display
        Screen(top=desktop_display_bar),
        # Main Display
        Screen(top=main_display_bar)
    ]


# +-------------------------------+
# |                               |
# |            Startup            |
# |                               |
# +-------------------------------+

if qtile.core.name == "x11":

    @hook.subscribe.startup_once
    def auto_startup_x11_once():
        home = os.path.expanduser("~")
        
        script = [
            "picom",
            "nm-applet",
            "blueman-applet",
            "udiskie",
            f"{home}/.config/qtile/scripts/xrandr_setup.sh", 
            f"{home}/.config/qtile/scripts/nitrogen_wallpaper_changer.sh",
        ]

        for program in script:
            subprocess.Popen(program)

else:
    @hook.subscribe.startup_once
    def auto_startup_wayland_once():
        pass


# +-----------------------------+
# |                             |
# |            Other            |
# |                             |
# +-----------------------------+


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
