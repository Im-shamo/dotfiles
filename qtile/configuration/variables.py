import os
mod = "mod4"

file_explorer = "dolphin"

terminal = "alacritty"
terminal_name = terminal

#manu = "wofi --normal-window --show drun --allow-images"
manu = "rofi -show drun -show-icons"

browser = "firefox"
code_editor = "code"

mono_font = "DroidSansM Nerd Font"

colours = {
    "RED":          "#881111",
    "DARK_RED":     "#220000",
    "ORANGE":       "#ff9933",
    "YELLOW":       "#b97f18",
    "GREEN":        "#72b043",
    "DARK_GREEN":   "#007f4e",
    "BLUE":         "#194a7a",
    "DARK_BLUE":    "#0c0f3f",
    "LIGHT_BLUE":   "#4682b4",
    "BLACK":        "#000000",
    "LIGHT_GRAY":   "#d3d3d3",
    "SILVER":       "#c0c0c0",
    "PURPLE":       "#9678b6",
}

### Bar ###
bar_margin = [6,4,2,4]

### Layouts ### 
margin = [4,4,4,4]
border_focus_colour = "0066cc"  #Light blue
border_normal_colour = "004d66" #Dark Blue
border_width = 3

### Startups ###
scripts_dir = os.path.expanduser("~/.config/qtile/scripts")