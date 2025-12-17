#!/usr/bin/env bash
if [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
  waypaper --backend swww --random
else
  waypaper --backend feh --random
fi
exit