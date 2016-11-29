#!/usr/bin/env bash

mpc clear
mpc listall | shuf | head -n 10 | mpc add
mpc play
