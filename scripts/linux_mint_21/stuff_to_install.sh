#!/usr/bin/env bash
#   WARNGING ! this only works on linux mint 21 !
#   Copy my files
echo    "WARNGING ! this only works on linux mint 21 !"
read -p "Are you sure? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then

cd ~
tar -xf "/media/shamokwok/Old PC HDD/Backup/Documents.tar.gz" &
tar -xf "/media/shamokwok/Old PC HDD/Backup/Pictures.tar.gz" &
tar -xf "/media/shamokwok/Old PC HDD/Backup/Linux_scripts.tar.gz" &
tar -xf "/media/shamokwok/Old PC HDD/Backup/Iso.tar.gz" &

#   Install needed packages
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3 python3-pip udiskie picom rofi wget fish git vim steam pavucontrol nitrogen htop bashtop

#   Install flatpaks
flatpak install org.gnome.font-viewer io.github.spacingbat3.webcord keepassxc

#   Git configs
git config --global user.name "im-shamo"
git config --global user.email "samuelkwok2007@gmail.com"

#   Get my git repos
mkdir -p ~/Clone
cd ~/Clone
git clone https://github.com/im-shamo/dotfiles
cd ~/.config
ln -sf ~/Clone/dotfiles/qtile .
cd ~

#   Install qtile
sudo apt install -y dbus-x11 libnotify-bin python3-mypy xserver-xephyr python3-pytest
pip install qtile --user #--break-system-packages
echo """[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=qtile start
Type=Application
Keywords=wm;tiling""" | sudo tee /usr/share/xsessions/qtile.desktop > /dev/null
cd ~/Clone
git clone https://github.com/elParaguayo/qtile-extras.git
cd dotfiles/qtile
ln -s ~/Clone/qtile-extras/qtile_extras

#   Install fonts
cd ~/Downloads
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/DroidSansMono.zip
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hack.zip
sudo mkdir -p /usr/share/fonts/Hack
sudo unzip Hack.zip -d /usr/share/fonts/Hack
sudo mkdir -p /usr/share/fonts/DroidSansMono
sudo unzip DroidSansMono.zip -d /usr/share/fonts/DroidSansM
fc-list | grep Hack
fc-list | grep DroidSansM
rm ./DroidSansMono.zip ./Hack.zip

#   To install vscode 
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg
sudo apt update 
sudo apt install -y apt-transport-https
sudo apt install code -y

#   Install OpenTabletDriver
cd ~/Downloads
wget https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest/download/OpenTabletDriver.deb
sudo apt install ./OpenTabletDriver.deb -y
rm ./OpenTabletDriver.deb
#   Enable OpenTabletDriver at startup
sudo systemctl --user enable opentabletdriver.service --now

#   Install Osu
mkdir -p ~/Application
cd ~/Application
wget https://github.com/ppy/osu/releases/latest/download/osu.AppImage
chmod u+x ./osu.AppImage

#   Install wine
sudo dpkg --add-architecture i386
sudo mkdir -pm755 /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources
sudo apt update
sudo apt install --install-recommends winehq-stable -y
winecfg

#   Install virtual Machines
cd ~/Downloads
sudo apt-get install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
sudo adduser $USER libvirt
sudo adduser $USER kvm
sudo adduser $USER libvirt-qemu

#   https://www.linuxtechi.com/how-to-install-virtualbox-on-linuxmint/
sudo apt install dkms build-essential linux-headers-$(uname -r) -y
sudo apt install curl wget apt-transport-https gnupg2
curl -fsSL https://www.virtualbox.org/download/oracle_vbox_2016.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/vbox.gpg
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/vbox.gpg] http://download.virtualbox.org/virtualbox/debian jammy contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
sudo apt update
sudo apt install virtualbox-7.0 -y
sudo usermod -aG vboxusers $USER
wget https://download.virtualbox.org/virtualbox/7.0.12/Oracle_VM_VirtualBox_Extension_Pack-7.0.12.vbox-extpack
sudo vboxmanage extpack install Oracle_VM_VirtualBox_Extension_Pack-7.0.12.vbox-extpack
rm ./Oracle_VM_VirtualBox_Extension_Pack-7.0.12.vbox-extpack

#   Install nwg-look and xcur2png
sudo apt install -y golang libgtk-3-dev libcairo2-dev libglib2.0-dev libpng-dev libxcursor-dev

cd ~/Clone
wget https://github.com/eworm-de/xcur2png/releases/download/0.7.1/xcur2png-0.7.1.tar.gz
tar -xvf xcur2png-0.7.1.tar.gz
cd xcur2png-0.7.1
./configure
make
sudo make install

git clone https://github.com/nwg-piotr/nwg-look.git
cd nwg-look
make build
sudo make install

#   Install Factorio Foreman
cd ~/Downloads
wget https://github.com/DanielKote/Foreman2/releases/download/v2.0-dev.13alpha/Release.zip
mkdir -p ~/Application/Foreman
unzip Release.zip -d ~/Application/Foreman
rm Release.zip

fi
