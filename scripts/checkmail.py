#!/usr/bin/env python2

import os
import feedparser

USERNAME = ""
PASSWORD = ""


def run_command(command):
    os.environ["command"] = command
    os.system("$command")


response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
unread_count = int(response["feed"]["fullcount"])

# for i in range(0, unread_count):
    # print str((i+1)) + "/" + str(unread_count) + " " + response['items'][i].title

if unread_count == 1:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_1.mp3")
elif unread_count == 2:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_2.mp3")
elif unread_count == 3:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_3.mp3")
elif unread_count == 4:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_4.mp3")
elif unread_count == 5:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_5.mp3")
elif unread_count == 6:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_6.mp3")
elif unread_count == 7:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_7.mp3")
elif unread_count == 8:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_8.mp3")
elif unread_count == 9:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_9.mp3")
elif unread_count == 10:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_10.mp3")
elif unread_count > 10:
    run_command("mpg123 /home/qeni/repo/room-raspberry/sounds/mails/mails_more.mp3")
