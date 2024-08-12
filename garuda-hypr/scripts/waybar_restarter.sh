#!/bin/bash

pkill --exact waybar
waybar -c $HOME/Clone/dotfiles/waybar/config.jsonc -s /home/shamokwok/Clone/dotfiles/waybar/style.css