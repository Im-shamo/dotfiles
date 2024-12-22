#!/usr/bin/bash

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

sections=("desktop" "programs" "drivers" "dev" "virtualization")
parts=("qtile" "hyprland" "kde" "utility" "office" "theming"
        "multimedia" "file_sharing" "game" "communication" "password" "fonts" "backup" "wine" "bluetooth" "printer" "audio" "nvidia" "code_forge_clients"
        "editor" "c" "python" "rust" "node" "virtualbox")

skip=false
declare -a downloaded
declare -a install_list


function install_git {
    echo -e "${Green}Install git${Color_Off}"
    sudo pacman -S --noconfirm --needed git
}

function install_yay {
    echo -e "${Green}Install yay${Color_Off}"
    sudo pacman -S --noconfirm --needed base-devel
    temp=`mktemp -d`
    cd $temp
    git clone https://aur.archlinux.org/yay-bin.git

    cd yay-bin
    makepkg -si --needed --noconfirm
    cd ~
}


function update_mirror {
    sudo pacman -S --noconfirm --needed reflector
    sudo reflector -c HK --sort rate -p https --save /etc/pacman.d/mirrorlist
}

# Desktop usage


function install_qtile {
    downloaded+=("qtile")
    echo -e "\n${Green}Qtile Specific${Color_Off}"

    # Dependances 
    sudo pacman -S --noconfirm --needed \
        qtile alsa-utils canto-daemon cmus jupyter_console khal libinput libpulse\
        lm_sensors moc python-bowler python-dbus-fast python-iwlib python-keyring\
        python-libcst python-mpd2 python-psutil python-pywayland python-pywlroots\
        python-setproctitle python-xdg python-xkbcommon xorg-xwayland xcb-util-cursor

    # Development 
    sudo pacman -S --noconfirm --needed \
        python-pytest pre-commit python-gobject xorg-server-xephyr mypy\
        imagemagick gtk-layer-shell libnotify xorg-server-xvfb

    # My applications
    sudo pacman -S --noconfirm --needed \
        picom rofi pavucontrol nitrogen dunst cava
    
    yay -S --noconfirm --needed qtile-extras 
}

function install_hyprland {
    downloaded+=("hyprland")
    # Hyprland
    echo -e "\n${Green}Hyprland Specific${Color_Off}"
    yay -S --noconfirm --needed \
        hyprland-meta-git waybar mako slurp grim
}

function install_kde {
    downloaded+=("kde")
    echo -e "\n${Green}KDE plasma${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        kde-utilities-meta kde-system-meta kde-network-meta tesseract-data-eng \
        systemsettings plasma-desktop filelight

}


function install_desktop_all {
    install_qtile
    install_hyprland
    install_kde
}

function install_utility {
    downloaded+=("utility")
    # Utility
    echo -e "\n${Green}Installing Utility${Color_Off}"

    # basic, polkit / keyring, termimal,
    # file manager / archiving / partitioning, application,
    sudo pacman -S --noconfirm --needed \
        vim udiskie conky man xorg-xrandr arandr man less \
        polkit polkit-gnome polkit-kde-agent gnome-keyring \
        kitty alacritty fastfetch \
        nemo file-roller gnome-disk-utility exfat-utils ntfs-3g\
        flatpak \
        tk
        
    
    yay -S --noconfirm --needed \
        clipse
}    

function install_office {
    downloaded+=("office")
    # Office and Productivity
    echo -e "\n${Green}Office and Productivity Software${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        libreoffice-fresh
}

function install_theming {
    downloaded+=("theming")
    # Theming
    echo -e "\n${Green}Theming${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        nwg-look breeze-gtk
    yay -S --noconfirm --needed \
        gradience
}

function install_multimedia {
    downloaded+=("multimedia")
    # Multimedia
    echo -e "\n${Green}Multimedia Software${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        firefox vlc \
        eog loupe curtail 
}
function install_file_sharing {
    downloaded+=("file_sharing")

    echo -e "\n${Green}File sharing${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        qbittorrent curl wget
    
}
function install_game {
    downloaded+=("game")
    # Game
    echo -e "\n${Green}Games${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        steam lutris
}

function install_communication {
    downloaded+=("communication")
    # Communication
    echo -e "\n${Green}Communication Software${Color_Off}"
    flatpak --noninteractive install flathub io.github.spacingbat3.webcord
}

function install_password {
    downloaded+=("password")
    # Password
    echo -e "\n${Green}Secrets${Color_Off}"
    flatpak --noninteractive install flathub org.keepassxc.KeePassXC
}

function install_fonts {
    downloaded+=("fonts")
    # Fonts
    echo -e "\n${Green}Fonts${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        gnome-font-viewer \
        noto-fonts noto-fonts-cjk noto-fonts-emoji otf-droid-nerd ttf-hack-nerd
}

function install_backup {
    downloaded+=("backup")
    echo -e "\n${Green}Backup${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        timeshift
}

function install_wine {
    downloaded+=("wine")
    echo -e "\n${Green}Wine${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        wine wine-gecko wine-mono winetricks\
        lib32-pipewire lib32-libpulse lib32-alsa-lib lib32-alsa-plugins
}

function install_programs_all {
    install_utility
    install_office
    install_theming
    install_multimedia
    install_game
    install_communication
    install_password
    install_fonts
    install_backup
    install_wine
}

# 2. Drivers
function install_bluetooth {
    downloaded+=("bluetooth")
    sudo pacman -S --noconfirm --needed \
        bluez bluez-utils blueman
    sudo usermod -aG lp $USER
    sudo systemctl enable bluetooth.service
}

function install_printer {
    downloaded+=("printer")
    sudo pacman -S --noconfirm --needed \
        cups cups-pdf cups-pk-helper system-config-printer
    sudo usermod -aG lp $USER
    sudo systemctl enable cups.socket
}

function install_audio {
    downloaded+=("audio")
    sudo pacman -S --noconfirm --needed \
        pipewire lib32-pipewire wireplumber pipewire-audio pipewire-alsa pipewire-pulse \
        pipewire-v4l2

    systemctl --user enable pipewire-pulse.service
}

function install_nvidia {
    downloaded+=("nvidia")
    sudo pacman -S --noconfirm --needed \
        dkms linux-headers nvidia-open-dkms nvidia-utils lib32-nvidia-utils
}

function install_nvidia_closed {
    downloaded+=("nvidia")
    sudo pacman -S --noconfirm --needed \
        dkms linux-headers nvidia-dkms nvidia-utils lib32-nvidia-utils
}

function install_amd {
    downloaded+=("amd")
    sudo pacman -S --noconfirm --needed \
	xf86-video-amdgpu mesa lib32-mesa vulkan-radeon lib32-vulkan-radeon
}

function install_drivers {
    install_bluetooth
    install_printer
    install_audio
}


# 3. Development
function install_code_forge_clients {
    downloaded+=("code_clients")
    # Code forge clients
    echo -e "\n${Green}Code forge clients${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        github-cli
}

function install_text_editors {
    downloaded+=("editor")
    # Text editor
    echo -e "\n${Green}Test editor${Color_Off}"
    yay -S --noconfirm --needed \
        visual-studio-code-bin
}

function install_python_dev {
    downloaded+=("python")
    # Python development
    echo -e "\n${Green}Python Development${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        python python-pip python-pipx 
}

function install_c_dev {
    downloaded+=("c")
    # C development
    echo -e "\n${Green}C Development${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        gcc gdb
}

function install_rust_dev {
    downloaded+=("rust")
    # Rust development
    echo -e "\n${Green}Rust Development${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        rustup
}

function install_node_dev {
    downloaded+=("node")
    # Node.js
    echo -e "\n${Green}Node.js${Color_Off}"
    yay -S --noconfirm --needed \
        nvm npm

}

function install_dev_all {
    install_code_forge_clients
    install_c_dev
    install_python_dev
    install_rust_dev
    install_node_dev
}

# 3. Virtualization
function install_virtualbox {
    downloaded+=("virtualbox")
    # VirtualBox
    echo -e "\n${Green}VirtualBox${Color_Off}"
    sudo pacman -S --noconfirm --needed \
        virtualbox virtualbox-host-modules-lts virtualbox-guest-iso 
    yay -S --noconfirm --needed \
        virtualbox-ext-oracle
}

# TODO: add kvm/quem


function install_virtualization_all {
    install_virutalbox
}


function install_list_from_exclude {
    for part in "${parts[@]}"; do
        if test "${#exclude_list[@]}" -eq 0; then
            install_list+=("${part}")
        else
            for ((i=0; i<"${#exclude_list[@]}"; i++)); do
                if test "${part}" != "${exclude_list[$i]}"; then
                    install_list+=("${part}")
                fi
            done
        fi
    done
}

function finished_success {
    echo -e "\n${Green}Finished Install!${Color_Off}"
}

function installation {
    if test "$skip" = false; then
        sudo pacman -Syy
        install_git
        install_yay
        update_mirror
        sudo pacman -Syy
    fi
    for part in ${install_list[@]}; do
        case "$part" in
            # section
            desktop )
                install_desktop_all
            ;;
            program )
                install_programs_all
            ;;
            drivers )
                install_drivers
            ;;
            dev )
                install_dev_all
            ;;
            virtualization )
                install_virtualization_all
            ;;

            # window manager
            qtile )
                install_qtile
            ;;
            hyprland )
                install_hyprland
            ;;
            kde )
                install_kde
            ;;
            # desktop section
            utility )
                install_utility
            ;;
            office )
                install_office
            ;;
            theming )
                install_theming
            ;;
            multimedia )
                install_multimedia
            ;;
            file_sharing )
                install_file_sharing
            ;;
            game )
                install_game
            ;;
            communication )
                install_communication
            ;;
            password )
                install_password
            ;;
            fonts )
                install_fonts
            ;;
            backup )
                install_backup
            ;;
            wine )
                install_wine
            ;;
            # drivers
            bluetooth )
                install_bluetooth
            ;;
            printer )
                install_printer
            ;;
            audio )
                install_audio
            ;;
            nvidia )
                install_nvidia
            ;;
	    nvidia_closed )
		install_nvidia_closed
	    ;;
            amd )
	    	install_amd
	    ;;
            # dev
            code_forge_clients )
                install_code_forge_clients
            ;;
            editor )
                install_text_editors
            ;;
            c )
                install_c_dev
            ;;
            python )
                install_python_dev
            ;;
            rust )
                install_rust_dev
                code_clients
            ;;
            node )
                install_node_dev
            ;;
            # virtualization
            virtualbox )
                install_virtualbox
            ;;
            
            # error
            * )
                echo -e "${Red}Unknown part: ${part}"
            ;;
        esac

    done
 
}

function help {
        echo "This script install packages for archlinux"
        echo " "
        echo "package_instal_setup.sh [options]"
        echo ""
        echo "options:"
        echo "-h, --help                Show help"
        echo " "
        echo "-a, --all"
        echo "                          Install all parts "
        echo "                          Here are the available parts:"
        echo " "
        echo "                          desktop: qtile, hyprland, kde"
        echo " "
        echo "                          programs: utility, bluetooth_printer, office"
        echo "                                    theming, multimedia, file_sharing, game, communication"
        echo "                                    password, fonts, backup"
        echo " "
        echo "                          drivers: bluetooth, printer, audio, nvidia, nvidia_closed, amd"
        echo " "
        echo "                          dev: code_forge_clients, editor, c, python, rust, node"
        echo " "
        echo "                          virtualization: virtualbox "
        echo " "
        echo "-i <parts>, --install <parts>"
        echo "                          Accepts a comma seperated list to install."
        echo " "
        echo "-e <parts>, --exclude <parts>"
        echo "                          Accepts a comma seperated list to exclude."
        echo " "
        echo "--skip                    Skips the setups"
}

if test $# -eq 0; then
    help
    exit 0
fi

while test $# -gt 0; do
    case "$1" in
        -h | --help )
        help
        exit 0
    ;;
        -i | --install )
        shift
        if test $# -gt 0; then
            IFS=',' read -r -a install_list <<< "$1"

            installation
            exit 0
        fi
    ;;
        -e | --exclude )
        shift
        if test $# -gt 0; then
            IFS=',' read -r -a exclude_list <<< "$1"

            install_list_from_exclude
            installation
            exit 0
        fi
    ;;
        -a | --all )
        shift
        install_list=("${parts[@]}")
        installation
        exit 0
    ;;
        --skip )
        shift
        skip=true
    ;;
    * )
        break
    ;;
    esac
done

