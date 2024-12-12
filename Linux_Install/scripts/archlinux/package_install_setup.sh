#!/usr/bin/bash

while test $# -gt 0; do
    case "$1" in
        -h | --help )
        echo "This script install packages for archlinux"
        echo " "
        echo "package_instal_setup.sh [options]"
        echo ""
        echo "options:"
        echo "-h, --help                Show help"
        echo "-i, --install <parts>     To install parts. Accepts a comma list."
        echo "                          To install a whole section just type in the section name."
        echo "                          Here are the available parts:"
        echo " "
        echo "                          desktop: qtile, hyprland"
        echo " "
        echo "                          programs: utility, bluetooth_printer, office"
        echo "                                    theming, multimedia, game, communication"
        echo "                                    password, fonts "
        echo " "
        echo "                          dev: code_clients, editor, c, python, rust, node"
        echo " "
        echo "                          virtualiztion: virtualbox "
        exit 0
    ;;
    esac
done

# https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux
# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White

# Underline
UBlack='\033[4;30m'       # Black
URed='\033[4;31m'         # Red
UGreen='\033[4;32m'       # Green
UYellow='\033[4;33m'      # Yellow
UBlue='\033[4;34m'        # Blue
UPurple='\033[4;35m'      # Purple
UCyan='\033[4;36m'        # Cyan
UWhite='\033[4;37m'       # White

# Background
On_Black='\033[40m'       # Black
On_Red='\033[41m'         # Red
On_Green='\033[42m'       # Green
On_Yellow='\033[43m'      # Yellow
On_Blue='\033[44m'        # Blue
On_Purple='\033[45m'      # Purple
On_Cyan='\033[46m'        # Cyan
On_White='\033[47m'       # White

# High Intensity
IBlack='\033[0;90m'       # Black
IRed='\033[0;91m'         # Red
IGreen='\033[0;92m'       # Green
IYellow='\033[0;93m'      # Yellow
IBlue='\033[0;94m'        # Blue
IPurple='\033[0;95m'      # Purple
ICyan='\033[0;96m'        # Cyan
IWhite='\033[0;97m'       # White

# Bold High Intensity
BIBlack='\033[1;90m'      # Black
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIBlue='\033[1;94m'       # Blue
BIPurple='\033[1;95m'     # Purple
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White

# High Intensity backgrounds
On_IBlack='\033[0;100m'   # Black
On_IRed='\033[0;101m'     # Red
On_IGreen='\033[0;102m'   # Green
On_IYellow='\033[0;103m'  # Yellow
On_IBlue='\033[0;104m'    # Blue
On_IPurple='\033[0;105m'  # Purple
On_ICyan='\033[0;106m'    # Cyan
On_IWhite='\033[0;107m'   # White

if ! command -v git 2>&1 >/dev/null; then
    echo "install git"
    sudo pacman -S git
fi

if ! command -v yay 2>&1 >/dev/null; then
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
echo -e "\n${Red}Qtile Specific${Color_Off}"
sudo pacman -S --noconfirm --needed \
    picom rofi pavucontrol nitrogen dbus libnotify xorg-server-xephyr python-dbus-next
yay -S --noconfirm --needed qtile-extras 


# Hyprland
echo -e "\n${Red}Hyprland Specific${Color_Off}"
yay -S --noconfirm --needed \
    hyprland-meta-git waybar


# Utility
echo -e "\n${Red}Installing Utility${Color_Off}"

# basic, polkit / keyring, termimal,
# file manager / archiving / partitioning, application,
sudo pacman -S --noconfirm --needed \
    wget vim curl udiskie conky man xorg-xrandr arandr \
    polkit polkit-gnome polkit-kde-agent gnome-keyring \
    kitty alacritty fastfetch \
    nemo file-roller gnome-disk-utility exfat-utils ntfs-3g\
    flatpak 


# bluetooth and printers
echo -e "\n${Red}Bluetooth and Printers${Color_Off}"
sudo pacman -S --noconfirm --needed \
    bluez bluez-utils \
    cups cups-pdf cups-pk-helper system-config-printer \

sudo usermod -aG lp $USER
sudo systemctl enable bluetooth.service cups.socket


# Office and Productivity
echo -e "\n${Red}Office and Productivity Software${Color_Off}"
sudo pacman -S --noconfirm --needed \
    libreoffice-fresh


# Theming
echo -e "\n${Red}Theming${Color_Off}"
sudo pacman -S --noconfirm --needed \
    nwg-look breeze-gtk
yay -S --noconfirm --needed \
    gradience

# Multimedia
echo -e "\n${Red}Multimedia Software${Color_Off}"
sudo pacman -S --noconfirm --needed \
    firefox vlc \
    eog loupe curtail


# Game
echo -e "\n${Red}Games${Color_Off}"
sudo pacman -S --noconfirm --needed \
    steam lutris


# Communication
echo -e "\n${Red}Communication Software${Color_Off}"
flatpak --noninteractive install flathub io.github.spacingbat3.webcord


# Password
echo -e "\n${Red}Secrets${Color_Off}"
flatpak --noninteractive install flathub org.keepassxc.KeePassXC


# Fonts
echo -e "\n${Red}Fonts${Color_Off}"
sudo pacman -S --noconfirm --needed \
    gnome-font-viewer \
    noto-fonts noto-fonts-cjk noto-fonts-emoji otf-droid-nerd ttf-hack-nerd


# 2. Development
# Code forge clients
echo -e "\n${Red}Code forge clients${Color_Off}"
sudo pacman -S --noconfirm --needed \
    github-cli


# Text editor
echo -e "\n${Red}Test editor${Color_Off}"
yay -S --noconfirm --needed \
    visual-studio-code-bin


# Python development
echo -e "\n${Red}Python Development${Color_Off}"
sudo pacman -S --noconfirm --needed \
    python python-pip python-pipx 


# C development
echo -e "\n${Red}C Development${Color_Off}"
sudo pacman -S --noconfirm --needed \
    gcc gdb


# Rust development
echo -e "\n${Red}Rust Development${Color_Off}"
sudo pacman -S --noconfirm --needed \
    rustup


# Node.js
echo -e "\n${Red}Node.js${Color_Off}"
yay -S --noconfirm --needed \
    nvm npm

nvm install node


# 3. Virtualization
# VirtualBox
echo -e "\n${Red}VirtualBox${Color_Off}"
sudo pacman -S --noconfirm --needed \
    virtualbox virtualbox-host-modules-lts virtualbox-guest-iso 
yay -S --noconfirm --needed \
    virtualbox-ext-oracle
