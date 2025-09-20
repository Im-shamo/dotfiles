#!/usr/bin/env bash
external=$(xrandr | grep -i  "HDMI" | cut -d " " -f1)
rate=60
res=1920x1080

wlr-randr --output "$external" --custom-mode "$res"@"$rate"
