#!/usr/bin/bash

if ! command -v git > 2 > &1 > /dev/null; then
    echo "install git"
    sudo pacman -S git
fi

if ! command -v yay > 2 >&1 > /dev/null; then
    echo "installing yay"
    temp=`mktemp`
    cd $mktemp
    
    git clone https://aur.archlinux.org/yay-bin.git

    cd yay-bin
    makepkg -si
fi

sudo pacman -Syy

# Desktop usage
# Qtile


# Hyprland


# Office / Productivity


# Theming


# Utility


# Web


# Game



# 2. Development
# Text editor


# Python development


# C development


# Rust development