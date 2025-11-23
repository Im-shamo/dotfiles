from libqtile.config import Key
from libqtile.lazy import lazy

from configuration.variables import *
from configuration.helper_functions import swap_screens

keys = [
    # Qtile shutdown and reload
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "mod1"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),


    ### Windows ###

    # Actions
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Movements
    Key([mod], "grave", swap_screens, desc="Swap workspace"),
    Key([mod], 'period', lazy.next_screen(), desc='Move cursor to next monitor'),

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    
    # Windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    # Spliting
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Layout switching
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),


    ### Application ###

    # App launchers
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn(menu), desc=f"Launch {menu.split(' ')[0]}"),
    Key([mod], "m", lazy.spawncmd()),
    Key([mod], "e", lazy.spawn(file_explorer), desc=f"Spawn the file explorer ({file_explorer})"),
    Key([mod], "c", lazy.spawn(code_editor)),
    Key([mod], "b", lazy.spawn(browser)),

    # Screenshots
    Key([], "Print", lazy.spawn("spectacle -m -b -c"), desc="Take screenshot"),
    Key([mod], "Print", lazy.spawn("spectacle -g"), desc="Launch spectacle screenshot"),

    # Wallpaper
    Key([mod], "w", lazy.spawn(f"bash {os.path.join(scripts_dir, 'wallpaper_changer.sh')}")),
    Key([mod, "shift"], "w", lazy.spawn("waypaper")),
    Key([mod], "s", lazy.spawn("selector")),
    Key([mod, "shift"], "s", lazy.spawn(f"bash {os.path.join(scripts_dir, 'safe_wallpaper.sh')}")),

    # Media Control
    # Source 
    #   https://askubuntu.com/questions/97936/terminal-command-to-set-audio-volume
    #   https://www.reddit.com/r/qtile/comments/v718d8/how_to_setup_media_keys/
    # Audio
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%"), desc="Lower Volume by 2%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"), desc="Raise Volume by 2%" ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute/Unmute"),

    # Playback
    Key([], "XF86AudioPlay",  lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioStop",  lazy.spawn("playerctl stop"),  desc="Stop audio"),
    Key([], "XF86AudioNext",  lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev",  lazy.spawn("playerctl previous"), desc="Skip to previous"),

    # Laptop display brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("blight set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("blight set -5%")),
    # TODO: Add the rest of the keyboard controls
]
