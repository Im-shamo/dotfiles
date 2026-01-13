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
swayidle -w \
    timeout 300 'swaylock -f -c 000000' \
    before-sleep 'swaylock -f -c 000000' &
# deskflow &

