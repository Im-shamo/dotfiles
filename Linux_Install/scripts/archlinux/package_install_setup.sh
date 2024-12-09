#!/usr/bin/bash

if ! command -v git > 2 >&1 > /dev/null; then
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
sudo pacman -S --noconfirm --needed reflector
sudo reflector -c HK,TW --sort rate -p https --save /etc/pacman.d/mirrorlist
sudo pacman -Syyu

# Desktop usage
# Qtile
echo "Qtile specific"
sudo pacman -S --noconfirm --needed \
    picom rofi pavucontrol nitrogen dbus libnotify xorg-server-xephyr
yay -S --noconfirm --needed qtile-extras 


# Hyprland
yay -S --noconfirm --needed \
    hyprland-meta-git waybar


# Utility
echo "Installing Utility"

# basic, polkit / keyring, termimal,
# file manager / archiving / partitioning, application,
sudo pacman -S --noconfirm --needed \
    wget vim curl udiskie conky man xorg-xrandr arandr \
    polkit polkit-gnome polkit-kde-agent gnome-keyring \
    kitty alacarity \
    nemo file-roller gnome-disk-utility exfat-utils ntfs-3g\
    flatpak 


# bluetooth and printers
sudo pacman -S --noconfirm --needed \
    bluez bluez-utils \
    cups cups-pdf cups-pk-helper system-config-printer \

sudo usermod -aG lp $USER
systemctl --user enable bluetooth.service cups.socket


# Office and Productivity
sudo pacman -S --noconfirm --needed \
    libreoffice-fresh \ 


# Theming
sudo pacman -S --noconfirm --needed \
    nwg-look breeze-gtk
yay -S --noconfirm --needed \
    gradience

# Multimedia
sudo pacman -S --noconfirm --needed \
    firefox vlc \
    eog loupe cur


# Game
sudo pacman -S --noconfirm --needed \
    steam lutris


# Communication
flatpak --noninteractive install flathub io.github.spacingbat3.webcord


# Password
flatpak --noninteractive install flathub org.keepassxc.KeePassXC


# Fonts
echo "installing fonts"
sudo pacman -S --noconfirm --needed \
    gnome-font-viewer \
    noto-fonts noto-fonts-cjk noto-fonts-emoji otf-droid-nerd ttf-hack-nerd


# 2. Development
# Code forge clients
sudo pacman -S --noconfirm --needed \
    github-cli


# Text editor
yay -S --noconfirm --needed \
    visual-studio-code-bin


# Python development
sudo pacman -S --noconfirm --needed \
    python python-pip python-pipx 


# C development
sudo pacman -S --noconfirm --needed \
    gcc gdb


# Rust development
sudo pacman -S --noconfirm --needed \
    rustup


# Node.js
yay -S --noconfirm --needed \
    nvm npm

nvm install node


# 3. Virtualization
# VirtualBox
sudo pacman -S --noconfirm --needed \
    virtualbox virtualbox-host-modules-lts virtualbox-guest-iso 
yay -S --noconfirm --needed \
    virtualbox-ext-oracle