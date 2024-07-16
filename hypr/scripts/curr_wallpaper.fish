#!/usr/bin/env fish
set cur_wall ''
set past_wall ''

while true
    set cur_wall "$(cat ~/.cache/swww/HDMI-A-1)"
    if test "$cur_wall" != "$past_wall"
        ln -sf $cur_wall ~/Pictures/curr_wall_paper
    end
    set past_wall "$cur_wall"
    sleep 60
end