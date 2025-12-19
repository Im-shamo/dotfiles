source /usr/share/cachyos-fish-config/cachyos-config.fish
:
set fish_greeting
oh-my-posh init fish --config ~/Clone/dotfiles/shamo.omp.jsonc| source

fish_add_path --path ~/.config/rofi/applets/bin ~/.config/rofi/scripts
set -gx SSH_SSH_SOCK $XDG_RUNTIME_DIR/gcr/ssh
set -gx EDITOR nvim
set -gx PAGER less
set -gx VISUAL $EDITOR
set -gx BROWSER brave
set -gx XDG_MENU_PREFIX arch-
