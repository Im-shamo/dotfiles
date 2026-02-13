#!/usr/bin/env bash

/usr/lib/polkit-kde-authentication-agent-1 &    # Polkit Agent
dunst &                                         # Notification

swayidle -w \     # session lock
  timeout 300 'swaylock -f -i ~/Pictures/current-wallpaper' \
  before-sleep 'swaylock -f -i ~/Pictures/current-wallpaper' &

~/.config/sway/scripts/wallpaper_changer.sh &  # Waypaper

# Applets
udiskie -t --appindicator && sleep 1 &          # Disk mounting
nm-applet && sleep 1 &                          # Network Manager
blueman-applet && sleep 1 &                     # Bluetooth
~/.config/sway/scripts/waybar_restarter.sh &
