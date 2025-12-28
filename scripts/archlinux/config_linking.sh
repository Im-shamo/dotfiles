#!/usr/bin/bash

config="$HOME/.config"
dots="$HOME/Clone/dotfiles"

folders=(
    "alacritty" "awesome" "dunst" "fish" "hypr" "hyprlock" "i3" "kitty"
    "picom" "qtile" "waybar" "wofi" "nvim"
    )

files=(".vimrc" ".Xresources")

if [[ ! -d $dots ]]; then
    echo "$dots folder does not exist."
    exit 1
fi

if [[ ! -d $config ]]; then
    echo "$config folder does not exist."
    exit 1
fi

cd $config

for foldername in "${folders[@]}"; do
    target="$dots/$foldername"
    config_location="$config/$foldername"

    # If the config file already exists, then rename it
    if ( [[ -d "$config_location" ]] || [[ -f "$config_location" ]] ) && [[ ! -h "$config_location" ]]; then
        mv -v "$config_location" "${config_location}".bak
    fi

    if [[ -d "$target" ]] || [[ -f "$target" ]]; then
        ln -sv "$target"
    else
        echo "error: $target does not exist!"
    fi
done

cd $HOME
for filename in "${files[@]}"; do
    target="$dots/$filename"
    config_location="$HOME/$filename"

    # If the config file already exists, then rename it
    if ( [[ -d "$config_location" ]] || [[ -f "$config_location" ]] ) && [[ ! -h "$config_location" ]]; then
        mv -v "$config_location" "${config_location}".bak
    fi

    if [[ -d "$target" ]] || [[ -f "$target" ]]; then
        ln -sv "$target"
    else
        echo "error: $target does not exist!"
    fi
done
