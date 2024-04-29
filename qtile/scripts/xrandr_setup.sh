#!/bin/bash

desktop=$(xrandr | grep -i  "HDMI" | cut -d " " -f1)
external=$(xrandr | grep -i "eDP" | cut -d " " -f1)
rate=144.00
res=1920x1080

xrandr --output $external --mode  $res --rate $rate --output $desktop --mode $res --rate $rate --right-of $external