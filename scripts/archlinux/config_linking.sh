#!/usr/bin/bash

config="$HOME/.config"
dots="$HOME/Clone/dotfiles"

configLinks=(
    "alacritty" "awesome" "dunst" "fish" "hypr" "hyprlock" "i3" "kitty" "picom"
    "qtile" "waybar" "wofi" "nvim" "icewm"
)

homeLinks=(".vimrc" ".Xresources")

if [[ ! -d $dots ]]; then
    echo "$dots folder does not exist."
    exit 1
fi

if [[ ! -d $config ]]; then
    echo "$config folder does not exist."
    exit 1
fi

cd $config

for linkname in "${configLinks[@]}"; do
    target="$dots/$linkname"
    link="$config/$linkname"

    # If the link location already exists, then rename it
    if ( [[ -d "$link" ]] || [[ -f "$link" ]] ) && [[ ! -h "$link" ]]; then
        mv -v "$link" "${link}".bak
    fi

    if [[ -d "$target" ]] || [[ -f "$target" ]]; then
        ln -sv "$target" "$link"
    else
        echo "error: $target does not exist!"
    fi
done

cd $HOME
for linkname in "${homeLinks[@]}"; do
    target="$dots/$linkname"
    link="$HOME/$linkname"

    # If the link location already exists, then rename it
    if ( [[ -d "$link" ]] || [[ -f "$link" ]] ) && [[ ! -h "$link" ]]; then
        mv -v "$link" "${link}".bak
    fi

    if [[ -d "$target" ]] || [[ -f "$target" ]]; then
        ln -sv "$target" "$link"
    else
        echo "error: $target does not exist!"
    fi
done
