#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lcd_i2c

import os
import sys
import tty
import termios
import pyowm
import time
import threading
import feedparser
import datetime
from stravalib import Client

owm = pyowm.OWM('')
USERNAME = ""
PASSWORD = ""
client = Client(access_token="")
athlete = client.get_athlete()


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


def get_first_line():
    while True:
        result = datetime.datetime.today().strftime("%d.%m/%H:%M") + " "
        result += "G:" + str(checkmail(True))
        lcd_i2c.lcd_string(result, lcd_i2c.LCD_LINE_1)
        time.sleep(60)


def get_second_line():
    global empty_line

    while True:
        observation = owm.weather_at_place('Zmigrod,pl')
        w = observation.get_weather()
        result = "T:" + str(w.get_temperature('celsius')['temp']) + " "
        result += "W:" + str(int(w.get_wind()['speed'])) + " "
        # result += str(w.get_pressure()['press'])
        # result += str(w.get_clouds()) + " "
        # result += str(w.get_humidity())

        today = datetime.date.today()
        monday = str(today - datetime.timedelta(days=today.weekday()))
        monday += "T00:00:00Z"
        distance = 0
        for activity in client.get_activities(after = monday,  limit=15):
            # print("{0.name} {0.moving_time} {0.distance}".format(activity))
            distance += float(activity.distance)
        distance /= 1000
        distance = round(distance, 2)
        result += str(distance) + "km"

        lcd_i2c.lcd_string(result, lcd_i2c.LCD_LINE_2)

        time.sleep(120)


def checkmail(muted=True):
    response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
    unread_count = int(response["feed"]["fullcount"])

    if not muted:
        if unread_count == 1:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_1.mp3")
        elif unread_count == 2:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_2.mp3")
        elif unread_count == 3:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_3.mp3")
        elif unread_count == 4:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_4.mp3")
        elif unread_count == 5:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_5.mp3")
        elif unread_count == 6:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_6.mp3")
        elif unread_count == 7:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_7.mp3")
        elif unread_count == 8:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_8.mp3")
        elif unread_count == 9:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_9.mp3")
        elif unread_count == 10:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_10.mp3")
        elif unread_count > 10:
            run_command("mpg123 /home/pi/repo/room-raspberry/sounds/mails/mails_more.mp3")

    return unread_count


def standby():

    global empty_line

    getch = _getch()
    key = getch()
    while(key != " "):
        result = ""
        print(key)
        if ord(key) == 13:
            command = "killall mpg123"
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

        elif key == "5":
            observation = owm.weather_at_place('Zmigrod,pl')
            w = observation.get_weather()
            temperature = int(w.get_temperature('celsius')['temp'])

            command = "/home/pi/repo/room-raspberry/scripts/weather.sh" + " " + str(temperature)
            run_command(command)
            
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

    global empty_line
    empty_line = " " * 16

    lcd_i2c.lcd_init()

    thread_clock = threading.Thread(target=get_first_line, args=())
    thread_clock.setDaemon(True)

    thread_temp = threading.Thread(target=get_second_line, args=())
    thread_temp.setDaemon(True)

    thread_standby = threading.Thread(target=standby, args=())

    thread_clock.start()
    thread_temp.start()
    thread_standby.start()


if __name__ == "__main__":
    main()
