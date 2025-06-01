#!/bin/bash
Xephyr :2 -ac -br -noreset -screen 1600x900 &
sleep 1 # This is stupid but i guess Xephyr need some time to start up
DISPLAY=:2 awesome 