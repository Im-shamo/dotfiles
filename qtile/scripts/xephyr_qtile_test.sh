#!/usr/bin/env bash
Xephyr -br -ac -noreset -screen 800x600 :1 &
export DISPLAY=:1
qtile start -c /home/shamokwok/Clone/dotfiles/qtile/testing.py
