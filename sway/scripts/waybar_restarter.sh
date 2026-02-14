#!/bin/bash
waybar_dir=~/.config/waybar
pkill --exact waybar
waybar -c $waybar_dir/config-sway.jsonc
