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
$HOME/.config/qtile/scripts/xrandr_setup.sh &
$HOME/.config/qtile/scripts/nitrogen_wallpaper_changer.sh  &

# +--------------------+
# |                    |
# |      Programs      |
# |                    |
# +--------------------+
picom &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
clipse -listen &
xsettingsd &