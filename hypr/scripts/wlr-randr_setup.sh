#!/usr/bin/env bash
rate=144
res=1920x1080

wlr-randr --output HDMI-A-1 --custom-mode "$res"@"$rate"
