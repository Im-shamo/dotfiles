#!/usr/bin/env bash
external=$(xrandr | grep -i  "HDMI" | cut -d " " -f1)
laptop=$(xrandr | grep -i "eDP" | cut -d " " -f1)
rate=60
res=1920x1080

if [[ -z "$laptop" ]]; then
    xrandr --output "$external" --mode $res --rate $rate
elif [[ -z "$external" ]]; then
    xrandr --output "$laptop" --mode  $res --rate $rate --output "$external" --mode $res --rate $rate --right-of "$laptop"
else
    xrandr --output Virtual-1 --auto
fi
