#!/usr/bin/env bash

mpc clear
mpc search filename "alarm" | shuf | head -n 2 | mpc add
mpc play
