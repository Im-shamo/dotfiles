#!/usr/bin/bash

if ! command -v git > 2 > &1 > /dev/null; then
    echo "install git"
    sudo pacman -S git
fi

if ! command -v yay > 2 >&1 > /dev/null; then
    echo "installing yay"
    temp=`mktemp -d`
    cd $temp
    git clone https://aur.archlinux.org/yay-bin.git

    cd yay-bin
    makepkg -si
fi

sudo pacman -Syy

# Desktop usage
# Qtile
echo "Qtile specific"
sudo pacman -S --noconfirm --needed \
    picom rofi pavucontrol nitrogen dbus libnotify xorg-server-xephyr
cd $temp
git clone https://aur.archlinux.org/qtile-extras.git
cd qtile-extras
makepkg -si --noconfirm

# Hyprland
sudo pacman -S --noconfirm --needed \


# Utility
echo "Installing Utility"
sudo pacman -S --noconfirm --needed \
    kitty alacarity \
    wget curl vim udiskie \
    flatpak \

# Office / Productivity
sudo pacman -S --noconfirm --needed \
    libraoffice-fresh


# Theming
sudo pacman -S --noconfirm --needed \
    nwg-look breeze-gtk

# Multimedia
sudo pacman -S --noconfirm --needed \
    firefox vlc 

# Game
sudo pacman -S --noconfirm --needed \
    steam

# Communication



# Password
flatpak --noninteractive install flathub org.keepassxc.KeePassXC


# Fonts
echo "installing fonts"
sudo pacman -S --noconfirm --needed \
    gnome-font-viewer \
    noto-fonts noto-fonts-cjk noto-fonts-emoji otf-droid-nerd ttf-hack-nerd


# 2. Development
# Text editor


# Python development


# C development


# Rust development


# 3. Virtualization
