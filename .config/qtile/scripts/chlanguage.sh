#!/usr/bin/env bash

lang=$(setxkbmap -print -verbose 10 | awk '/layout:/ {print  $2}')

if [ $lang == "us" ];then
	setxkbmap -layout latam -variant ",winkeys"
else
	setxkbmap -layout us
fi
