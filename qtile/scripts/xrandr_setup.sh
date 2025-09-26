#!/usr/bin/env bash
external=$(xrandr | grep -i  "HDMI" | cut -d " " -f1 | head -n 1)
laptop=$(xrandr | grep -i "eDP" | cut -d " " -f1 | head -n 1)
virtual=$(xrandr | grep -i "Virtual" | cut -d " " -f1 | head -n 1)
rate=144
res=1920x1080

if [[ -n "$virtual" ]]; then
echo "Set display: $virtual to $res@60"
xrandr --output "$virtual" --mode "$res" --rate 60
elif [[ -n "$laptop" ]]; then
echo "Set display: $laptop to $res@$rate"
xrandr --output "$laptop" --mode "$res" --rate $rate
elif [[ -n "$laptop" ]] && [[ -n $external ]]; then
echo "Set display: $laptop to $res@$rate $external to $res@$external"
xrandr --output "$laptop" --mode  "$res" --rate $rate --output "$external" --mode $res --rate $rate --right-of "$laptop"
else
echo "No display set"
fi
