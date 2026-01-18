#!/usr/bin/env bash
Xephyr -br -ac -noreset -screen 800x600 :1 &
export DISPLAY=:1
qtile start -c ~/Clone/dotfiles/qtile/configuration/default_config.py
