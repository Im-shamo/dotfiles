#!/usr/bin/env bash

# +-------------------+
# |                   |
# |      Applets      |
# |                   |
# +-------------------+
nm-apple &
blueman-applet &
udiskie &
# /usr/lib/nvidia-prime-applet/nvidia-prime & # Very lazy TODO CHANGE

# +-------------------+
# |                   |
# |      Scripts      |
# |                   |
# +-------------------+
$HOME/.config/qtile/scripts/xrandr_setup.sh &
$HOME/.config/qtile/scripts/nitrogen_wallpaper_changer.sh  &

# +--------------------+
# |                    |
# |      Programs      |
# |                    |
# +--------------------+
# picom &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1