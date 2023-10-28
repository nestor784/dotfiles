#!/usr/bin/env bash

dunstify -u low -t 2000 -a "disk usage" $(df -h | awk '$NF=="/"{printf "%d/%dGB (%s)\n", $3,$2,$5}')

