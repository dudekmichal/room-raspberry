#!/usr/bin/env python3

import os
import sys
import tty
import termios
import pyowm
import time

from RPLCD import CharLCD
from RPLCD import Alignment, CursorMode
from RPLCD import cursor
from RPLCD import BacklightMode

owm = pyowm.OWM('')


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


def enable_lcd(lcd):
    lcd.display_enabled = True
    lcd.cursor_mode = CursorMode.hide
    lcd.text_align_mode = Alignment.left
    lcd.backlight = True
    lcd.clear()


def disable_lcd(lcd):
    lcd.clear()
    lcd.backlight = False
    lcd.close()


def standby(lcd):
    getch = _getch()
    key = getch()
    while(key != " "):
        print(key)
        if ord(key) == 13:
            command = "sudo killall mpg123"
            run_command(command)
            command = "mpc stop"
            run_command(command)
            lcd.clear()
            lcd.write_string('Playing\nis stopped.')

        elif key == "-":
            command = "amixer -q sset Master 3%-"
            run_command(command)
            lcd.clear()
            lcd.write_string('Volume down...')

        elif key == "+":
            command = "amixer -q sset Master 3%+"
            run_command(command)
            lcd.clear()
            lcd.write_string('Volume up...')

        elif key == "/":
            command = "amixer -q sset Master toggle"
            run_command(command)
            lcd.clear()
            lcd.write_string('Mute On/Off')

        elif key == "5":
            observation = owm.weather_at_place('Zmigrod,pl')
            w = observation.get_weather()
            wind = str(w.get_wind()['speed'])
            temperature = str(int(w.get_temperature('celsius')['temp']))

            command = "/home/pi/repo/room-raspberry/scripts/weather.sh" + " " + temperature
            run_command(command)
            lcd.clear()
            lcd.write_string(
                'Zmigrod: {}\nstopni Celsjusza'.format(temperature))

        elif key == "8":
            command = "mpc toggle"
            run_command(command)
            lcd.clear()
            lcd.write_string('Pause/Play')

        elif key == "9":
            command = "mpc next"
            run_command(command)
            lcd.clear()
            lcd.write_string('Playing\nnext track')

        elif key == "7":
            command = "mpc prev"
            run_command(command)
            lcd.clear()
            lcd.write_string('Playing\nprevious track')

        elif key == "1":
            command = "/home/pi/repo/room-raspberry/scripts/add10rand.sh"
            run_command(command)
            lcd.clear()
            lcd.write_string('Playing 10\nrandom tracks...')

        key = getch()


def main():
    lcd = CharLCD(cols=16, rows=2)
    lcd.enable_lcd()
    lcd.write_string('It\'s the time.\n')
    lcd.write_string('I\'m ready')
    time.sleep(10)
    # standby(lcd)
    lcd.disable_lcd()


if __name__ == "__main__":
    main()
