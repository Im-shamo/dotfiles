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
~/.config/qtile/scripts/xrandr_setup.sh &

# +--------------------+
# |                    |
# |      Programs      |
# |                    |
# +--------------------+
/usr/lib/polkit-kde-authentication-agent-1 &
dunst &             # Notification
picom &             # Compositor
udiskie -t &        # Disk mounting
clipse -listen &    # Clipboard manager
xautolock -detectsleep -time 3 -locker "i3lock -c 000000" &

