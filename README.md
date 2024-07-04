run these commands to install system
```bash
cd Downloads
wget https://raw.githubusercontent.com/Im-shamo/dotfiles/main/Linux_Install_script/stuff_to_install.sh
wget https://raw.githubusercontent.com/Im-shamo/dotfiles/main/Linux_Install_script/post_install.sh
chmod u+x ./stuff_to_install.sh post_install.sh
./stuff_to_install.sh
```
after that reboot and then run these
```bash
cd Downloads
./post_install.sh
rm ./stuff_to_install.sh ./post_install.sh
```
