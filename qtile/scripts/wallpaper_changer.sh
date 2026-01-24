#!/usr/bin/env bash
if ! command -v waypaper; then
    exit 1
fi
if [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
    if command -v swww; then
        waypaper --backend swww --random
    elif command -v swaybg; then
        waypaper --backend swaybg --random
    fi
else
    if command -v feh; then
        waypaper --backend feh --random
    fi
fi
exit
