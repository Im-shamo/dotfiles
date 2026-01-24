#!/usr/bin/env bash
rate=144
res=1920x1080

command -v xrandr && xrandr --output HDMI-A-0 --mode $res --rate $rate
