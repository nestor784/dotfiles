#!/usr/bin/env bash

dunstify -u low -t 2000 -a "memory usage" $(free -h | awk 'NR==2{printf "%s/%s (%.2f%%)\n", $3,$2,$3*100/$2 }')

