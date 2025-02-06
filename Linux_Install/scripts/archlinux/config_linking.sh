#!/usr/bin/bash

config="$HOME/.config"
# config=$(pwd)/test
dots="$HOME/Clone/dotfiles"

if [[ ! -d $dots ]]; then
    echo "$dots folder does not exist."
    exit 1
fi

if [[ ! -d $config ]]; then
    echo "$config folder does not exist."
    exit 1
fi

cd $config

folders=("alacritty" "awesome" "fish" "hypr" "hyprlock" "kitty" "picom" "qtile" "waybar" "wofi" "rofi")

for (( i=0; i<9; i++)); do
    target=$dots/${folders[$i]}
    location=$config/${folders[$i]}

    # If the config file already exists, then rename it
    if [[ -d $location ]]; then
        mv $location $location.bak
    fi
    if [[ ! -d $target ]]; then
        echo "$dots folder does not exists."
        exit 1
    fi
    echo "$location -> $target"
    ln -s $target
done

