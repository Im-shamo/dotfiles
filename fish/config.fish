if status is-interactive
    if test "$TERM" = "xterm-kitty"
        fastfetch --logo-width 35 --logo "/home/shamokwok/Pictures/Anime/Honkai_Star_Rail/firefly-3-nobg.png"
    else
        fastfetch
    end
end
set fish_greeting
