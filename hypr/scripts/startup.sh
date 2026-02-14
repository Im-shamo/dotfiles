#!/usr/bin/env bash

scripts="$HOME/.config/hypr/scripts"

systemctl --user start hyprpolkitagent &        # Polkit Agent
dunst &                                         # Notification
swayidle -w \
  timeout 300 'swaylock -f -i ~/Pictures/current-wallpaper' \
  timeout 600 'hyprctl dispatch dpms off' resume 'hyprctl dispatch dpms on' \
  timeout 660 'systemctl suspend' \
  before-sleep 'swaylock -f -i ~/Pictures/current-wallpaper' &
$scripts/wallpaper_changer.sh &  # Waypaper

# Applets
udiskie -t --appindicator && sleep 1 &          # Disk mounting
nm-applet && sleep 1 &                          # Network Manager
blueman-applet && sleep 1 &                     # Bluetooth
$scripts/waybar_restarter.sh &

# Cursor
hyprctl setcursor TachibanaHikariver100 24 &
