#!/usr/bin/bash
curl -s https://ohmyposh.dev/install.sh | bash -s # Install ohmyposh
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim' # Install vimplug

# Rofi applets
cd ~/Clone
git clone --depth=1 https://github.com/adi1090x/rofi.git
cd rofi
chmod u+x setup.sh
./setup.sh
