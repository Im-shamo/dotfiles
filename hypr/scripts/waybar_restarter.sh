#!/bin/bash
waybar_dir=~/.config/waybar
pkill --exact waybar
waybar -c $waybar_dir/config-hyprland.jsonc -s $waybar_dir/style-hyprland.css
