if status is-interactive
    if test "$TERM" = "xterm-kitty"
        fastfetch --logo-width 35 --logo "$HOME/Clone/dotfiles/fish/images/firefly-3-nobg.png"
    else
        fastfetch
    end
end
set fish_greeting
