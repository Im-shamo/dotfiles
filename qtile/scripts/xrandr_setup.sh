#!/usr/bin/env bash
external=$(xrandr | grep -i  "HDMI" | cut -d " " -f1)
laptop=$(xrandr | grep -i "eDP" | cut -d " " -f1)
rate=144
res=1920x1080

if [[ -z "$laptop" ]]; then
xrandr --output $external --mode $res --rate $rate
else
xrandr --output $laptop --mode  $res --rate $rate --output $external --mode $res --rate $rate --right-of $laptop
fi
