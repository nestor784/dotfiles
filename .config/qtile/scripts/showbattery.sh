#!/usr/bin/env bash

dunstify -u low -t 2000 -a "battery" $(upower -i /org/freedesktop/UPower/devices/battery_BAT1 | awk '/percentage/ {print }')

