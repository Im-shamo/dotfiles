#!/usr/bin/env bash

# +-------------------+
# |                   |
# |      Applets      |
# |                   |
# +-------------------+
command -v nm-applet && nm-applet &
command -v blueman-applet && blueman-applet &

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
command -v dunst && dunst &             # Notification
command -v picom && picom &             # Compositor
command -v udiskie && udiskie -t &        # Disk mounting
command -v clipse && clipse -listen &    # Clipboard manager
command -v powerkit && powerkit &
command -v deskflow && deskflow &

