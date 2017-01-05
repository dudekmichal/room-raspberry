# Raspberry Pi Room

![N|Solid](https://raw.github.com/qeni/room-raspberry/master/img/powered_by.png)

This is project for my own room. It includes Raspberry Pi 2B, speakers, lcd 16x2 I2C display, control panel with keyboard.

  - Checking for new e-mails
  - Alarm clock with cron
  - MPD music server
  - Voice information about current time
  - Counting number of kilometers on Strava (weekly)
  - Kudos and followers count on Strava
  - Weather information from OWM (Open Weather Map) API: temperature, wind,
    pressure, humidity etc.

LCD dysplay shows the most important informations. Panel controls playing music, alarm clocks. Each key on keyboard do something (e.g. shows temperature, song info). Alarm clock gets random track from tracks named like alarm*.mp3 in ~/music.


### Installation

If you want to use this stuff you will need to change a few things in file
room-system.py:
  - set variable owm to pyowm.OWM('<your key>').  
  - set USERNAME to your e-mail address.  
  - set PASSWORD to your e-mail password.  
  - set access token to your strava account.  

Then execute a few commands:

```
$ mkdir /home/pi/repo
$ cd /home/pi/repo
$ git clone https://github.com/qeni/room-raspberry
# apt-get update
# apt-get install python python3 python3-feedparser mpd mpc cron mpg123 python3-pip
# pip3 install pyowm stravalib
# systemctl enable cron
# systemctl start cron
$ mkdir -o /home/pi/.config/mpd
$ cp /home/pi/repo/room-raspberry/configs/mpd.conf /home/pi/.config/mpd/mpd.conf
$ echo "/home/pi/repo/room-raspberry/scripts/init.sh" >> ~/.bashrc
$ echo "sleep 3" >> ~/.bashrc
$ echo "/home/pi/repo/room-raspberry/controller.py" >> ~/.bashrc
$ crontab -e
Add lines:
0 8-21 * * * /home/pi/repo/room-raspberry/scripts/readhour.sh; /home/pi/repo/room-raspberry/scripts/checkmail.py
0 7 * * 1-5 /home/pi/repo/room-raspberry/scripts/alarmclock.sh # Alarm on 7.00 each day
* * * * * /home/pi/repo/room-raspberry/displayer.py

# reboot
```

### Todos

 - Nothing now

### License
GNU GPL v3.0
Just do what you wish.

**Free Software, hell yeah**
