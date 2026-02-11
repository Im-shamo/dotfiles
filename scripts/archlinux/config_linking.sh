#!/usr/bin/bash

userHome="$HOME"
dots="$HOME/Clone/dotfiles"

if [[ "$1" = "-t" ]]; then
    mkdir -pv /tmp/configtest/.config/
    userHome="/tmp/configtest"
fi

config="$userHome/.config"

configLinks=(
    "alacritty" "awesome" "dunst" "fish" "foot" "hypr" "hyprlock"
    "i3" "kitty" "nvim" "picom" "qtile" "sway" "waybar" "wofi" "icewm"
)

homeLinks=(".vimrc" ".Xresources" ".icewm" ".zshrc" ".p10k.zsh")

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
        ln -sv "$target"
    else
        echo "error: $target does not exist!"
    fi
done

cd $userHome
for linkname in "${homeLinks[@]}"; do
    target="$dots/$linkname"
    link="$userHome/$linkname"

    # If the link location already exists, then rename it
    if ( [[ -d "$link" ]] || [[ -f "$link" ]] ) && [[ ! -h "$link" ]]; then
        mv -v "$link" "${link}".bak
    fi

    if [[ -d "$target" ]] || [[ -f "$target" ]]; then
        ln -sv "$target"
    else
        echo "error: $target does not exist!"
    fi
done
