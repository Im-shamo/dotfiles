#!/usr/bin/env bash

sudo pacman -S --needed --noconfirm base-devel git

if [[ $(pacman -Qq yay) != "yay" ]]; then
    mkdir -p ~/Clone
    cd Clone
    git clone https://aur.archlinux.org/yay.git

    cd yay
    makepkg -si --noconfirm
else
    echo yay is already installed.
fi
