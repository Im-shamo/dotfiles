#!/usr/bin/env bash
#   Install needed packages
sudo apt update
sudo apt upgrate -y
sudo apt intsall -y python3 python3-pip udiskie picom rofi wget gpg fish git vim keepassxc steam pavucontrol nitrogen

#   Install flatpaks
flatpak install org.gnome.font-viewer io.github.spacingbat3.webcord

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
sudo apt install dbus-x11 libnoify-bin python3-mypy xserver-xephyr python3-pytest
pip install qtile[all] --break-system-packages
sudo echo """\
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=qtile start
Type=Application
Keywords=wm;tiling""" > /usr/share/xsessions
cd ~/Clone
git clone https://github.com/elParaguayo/qtile-extras.git
cd qtile-extras
pip install --user .

#   Install fonts
cd Downloads
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/DroidSansMono.zip
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hack.zip
sudo mkdir -p /usr/share/fonts/Hack
sudo unzip DroidSansMono.zip -d /usr/share/fonts/Hack
sudo mkdir -p /usr/share/fonts/DroidSansMono
sudo unzip DroidSansMono.zip -d /usr/share/fonts/DroidSansM
fc-list | grep Hack
fc-list | grep DroidSansM
rm DroidSansMono.zip Hack.zip

#   To install vscode 
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg
sudo apt install apt-transport-https
sudo apt update
sudo apt install code

#   Install OpenTabletDriver
cd ~/Downloads
sudo apt update
wget https://github.com/OpenTabletDriver/OpenTabletDriver/releases/latest/download/OpenTabletDriver.deb
sudo apt install ./OpenTabletDriver.deb
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
sudo apt install qemu-kvm libvirt-bin bridge-utils virt-manager -y
sudo adduser $USER libvirt

#   https://www.linuxtechi.com/how-to-install-virtualbox-on-linuxmint/
sudo apt install dkms build-essential linux-headers-$(uname -r) -y
sudo apt install curl wget apt-transport-https gnupg2
curl -fsSL https://www.virtualbox.org/download/oracle_vbox_2016.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/vbox.gpg
echo deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/vbox.gpg] http://download.virtualbox.org/virtualbox/debian jammy contrib | sudo tee /etc/apt/sources.list.d/virtualbox.list
sudo apt update
sudo apt install virtualbox-7.0 -y
sudo usermod -aG vboxusers $USER
wget https://download.virtualbox.org/virtualbox/7.0.12/Oracle_VM_VirtualBox_Extension_Pack-7.0.12.vbox-extpack
sudo vboxmanage extpack install Oracle_VM_VirtualBox_Extension_Pack-7.0.12.vbox-extpack

#   Install nwg-look
sudo apt install golang libgtk-3-dev libcairo2-dev libglib2.0-dev

cd ~/Clone
git clone https://github.com/nwg-piotr/nwg-look.git
cd nwg-look
make build
sudo make install

#   Install Factorio Foreman
cd ~/Downloads
wget https://github.com/DanielKote/Foreman2/releases/download/v2.0-dev.13alpha/Release.zip
mkdir -p ~/Application/Foreman
unzip Release.zip -d ~/Application/Foreman

#   Copy my files
cd ~
tar -xvf "/media/shamokwok/Old PC HDD/Backup/Documents.tar.gz"
tar -xvf "/media/shamokwok/Old PC HDD/Backup/Pictures.tar.gz"
tar -xvf "/media/shamokwok/Old PC HDD/Backup/Linux_scripts.tar.gz"
tar -xvf "/media/shamokwok/Old PC HDD/Backup/Iso.tar.gz"
