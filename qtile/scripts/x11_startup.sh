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
dunst &             # Notification
picom &             # Compositor
udiskie -t &        # Disk mounting
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
clipse -listen &    # Clipboard manager
