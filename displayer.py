#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import lcd_i2c

import os
import sys
import tty
import termios
import pyowm
import time
import feedparser
import datetime
from stravalib import Client

owm = pyowm.OWM('')
USERNAME = ""
PASSWORD = ""
client = Client(access_token="")
athlete = client.get_athlete()


def main():

    # First line
    response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
    unread_count = int(response["feed"]["fullcount"])

    # result = datetime.datetime.today().strftime("%d.%m/%H:%M") + " "
    result_1 = datetime.datetime.today().strftime("%H:%M") + " "
    result_1 += "G:" + str(unread_count) + " "
    observation = owm.weather_at_place('Zmigrod,pl')
    w = observation.get_weather()
    result_1 += "T:" + str(int(w.get_temperature('celsius')['temp'])) + "/"
    # result_1 += "W:" + str(int(w.get_wind()['speed'])) + " "
    # result_1 += "P:" + str(w.get_pressure()['press'])
    # result_1 += str(w.get_clouds()) + " "
    result_1 += str(w.get_humidity())

    # Second line

    # Kudos count
    kudos_count = 0
    for activity in client.get_activities():
        # print("{0.name} {0.moving_time} {0.distance}".format(activity))
        kudos_count += activity.kudos_count
    result_2 = "K:" + str(kudos_count) + " "

    # Followers count
    result_2 += "F:" + str(athlete.follower_count) + " "

    # Distance in this week
    today = datetime.date.today()
    monday = str(today - datetime.timedelta(days=today.weekday()))
    monday += "T00:00:00Z"
    distance = 0
    for activity in client.get_activities(after = monday,  limit=15):
        # print("{0.name} {0.moving_time} {0.distance}".format(activity))
        distance += float(activity.distance)
    distance /= 1000
    distance = round(distance, 1)
    result_2 += str(distance) + "km"

    lcd_i2c.lcd_init()
    lcd_i2c.lcd_string(result_1, lcd_i2c.LCD_LINE_1)
    lcd_i2c.lcd_string(result_2, lcd_i2c.LCD_LINE_2)


if __name__ == "__main__":
    main()
