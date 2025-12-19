#!/usr/bin/env bash
rate=144
res=1920x1080

xrandr --output HDMI-A-0 --mode $res --rate $rate
