#!/usr/bin/env bash
if [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
  waypaper --backend swaybg --random
else
  waypaper --backend feh --random
fi
