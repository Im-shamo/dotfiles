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
~/.config/qtile/scripts/wlr-randr_setup.sh &

# +--------------------+
# |                    |
# |      Programs      |
# |                    |
# +--------------------+
dunst &             # Notification
udiskie -t &        # Disk mounting
/usr/lib/polkit-gnome/polkit-kde-authentication-agent-1 &
clipse -listen &    # Clipboard manager
