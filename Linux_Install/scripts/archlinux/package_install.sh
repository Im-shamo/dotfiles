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

# python development

# c development

# rust development

# fonts
echo "installing fonts"
sudo pacman -S --noconfirm noto-fonts noto-fonts-cjk noto-fonts-emoji otf-droid-nerd ttf-hack-nerd