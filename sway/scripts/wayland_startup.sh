#!/usr/bin/env bash

# +-------------------+
# |                   |
# |      Applets      |
# |                   |
# +-------------------+
nm-applet &
blueman-applet &

# +-------------------+
# |                   |
# |      Scripts      |
# |                   |
# +-------------------+
~/.config/qtile/scripts/wallpaper_changer.sh &

# +--------------------+
# |                    |
# |      Programs      |
# |                    |
# +--------------------+
/usr/lib/polkit-kde-authentication-agent-1 &
dunst &             # Notification
udiskie -t &        # Disk mounting
clipse -listen &    # Clipboard manager
swayidle -w \
    timeout 300 'swaylock -f -i ~/Pictures/current-wallpaper' \
    before-sleep 'swaylock -f -i ~/Pictures/current-wallpaper' &
waybar -c ~/.config/waybar/config-sway.jsonc -s ~/.config/waybar/style-sway.css
# deskflow &

