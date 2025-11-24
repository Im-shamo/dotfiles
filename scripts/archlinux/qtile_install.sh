#!/usr/bin/env bash
sudo pacman -Syu --needed --noconfirm           \
    qtile python-dbus-fast python-psutil        \
    picom gnome-keyring seahorse                \
    fastfetch git github-cli fish bash          \
    alacritty konsole code kate kwrite nvim     \
    dolphin ark dunst udiskie                   \
    networkmanager network-manager-applet       \
    blueman xorg xorg-apps wlr-randr wayland    \
    polkit-kde-agent rofi btop conky            \
    feh swww nwg-look ly                        \
    breeze breeze5 breeze-gtk breeze-icons      \
    playerctl pavucontrol alsa-utils spectacle  \
    pulseaudio pulseaudio-alsa pipewire         \
    wireplumber nerd-fonts ttf-hack ttf-dejavu  \
    noto-fonts noto-fonts-cjk noto-fonts-emoji  \
    archlinux-xdg-menu xdg-user-dirs            \
    qt6-multimedia-ffmpeg pipewire-jack

yay -S --needed --noconfirm                     \
    qtile-extras i3lock-color                   \
    brave-bin waypaper                          \
    xautolock clipse-bin qt5ct-kde qt6ct-kde    \
    blight github-desktop-bin oh-my-posh
