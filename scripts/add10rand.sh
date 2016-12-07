#!/usr/bin/env bash

amixer set Master 40%

mpc clear
mpc listall | shuf | head -n 10 | mpc add
mpc play
