if status is-interactive
    if test "$TERM" = "xterm-kitty"
        fastfetch --logo-width 35 --logo "/home/shamokwok/Downloads/1024px-Archlinux-logo-only.svg.png"
    else
        fastfetch
    end
end
set fish_greeting
