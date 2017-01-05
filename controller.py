#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import tty
import termios
import time
import datetime


class _getch:
    def __init__(self):
        pass

    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def run_command(command):
    os.environ["command"] = command
    os.system("$command")


def standby():
    getch = _getch()
    key = getch()
    while(key != " "):
        result = ""
        print(key)
        if ord(key) == 13:
            ommand = "killall mpg123"
            run_command(command)
            command = "mpc stop"
            run_command(command)

        elif key == "0":
            lcd_i2c.LCD_BACKLIGHT = 0x00  # Off

        elif key == "1":
            lcd_i2c.LCD_BACKLIGHT  = 0x08  # On

        elif key == "-":
            command = "amixer -c 0 set PCM 2dB-"
            run_command(command)

        elif key == "+":
            command = "amixer -c 0 set PCM 2dB+"
            run_command(command)

        elif key == "/":
            pass

        elif key == "8":
            command = "mpc toggle"
            run_command(command)

        elif key == "9":
            command = "mpc next"
            run_command(command)

        elif key == "7":
            command = "mpc prev"
            run_command(command)

        elif key == "4":
            command = "/home/pi/repo/room-raspberry/scripts/add10rand.sh"
            run_command(command)

        key = getch()


def main():
    command = "amixer set PCM -- 95%"
    run_command(command)

    standby()


if __name__ == "__main__":
    main()
