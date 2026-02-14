test -e /usr/share/cachyos-fish-config/cachyos-config.fish && source /usr/share/cachyos-fish-config/cachyos-config.fish
set fish_greeting
test -e /usr/bin/oh-my-posh && oh-my-posh init fish --config ~/Clone/dotfiles/shamo.omp.jsonc | source

fish_add_path --path ~/.config/rofi/applets/bin ~/.config/rofi/scripts
set -gx SSH_SSH_SOCK "$XDG_RUNTIME_DIR/gcr/ssh"
set -gx EDITOR "vim"
set -gx PAGER "less"
set -gx LESSOPEN "| /usr/bin/src-hilite-lesspipe.sh %s"
set -gx LESS " -R"
set -gx VISUAL "$EDITOR"
set -gx BROWSER "brave"
set -gx XDG_MENU_PREFIX "arch-"

if test "$XDG_SESSION_DESKTOP" = "sway"
    set -gx QT_QPA_PLATFORMTHEME "qt6ct"
end

