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
/usr/lib/polkit-kde-authentication-agent-1 &
dunst &             # Notification
udiskie -t &        # Disk mounting
clipse -listen &    # Clipboard manager
powerkit &
# deskflow &

