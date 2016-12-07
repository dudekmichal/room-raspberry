# Raspberry Pi Room

![N|Solid](https://raw.github.com/qeni/room-raspberry/master/img/powered_by.png)

This is project for my own room. It includes Raspberry Pi 2B, speakers, lcd 16x2 I2C display, control panel with keyboard.

  - Checking for new e-mails
  - Alarm clock with cron
  - MPD music server
  - Voice information about current time
  - Counting number of kilometers in Strava (weekly)
  - Weather information from OWM (Open Weather Map) API

> LCD dysplay shows the most important informations. Panel controls playing
> music, alarm clocks. Each key on keyboard do something (e.g. shows
> temperature, song info). Alarm clock gets random track from tracks named like alarm*.mp3 in ~/music


### Installation

If you want to use this stuff you will need to change a few things in file
room-system.py:
  - set variable owm to pyowm.OWM('<your key>').  
  - set USERNAME to your e-mail address.  
  - set PASSWORD to your e-mail password.  
  - set access token to your strava account.  

Then install all dependencies on your RPi:

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
$ echo "sleep 2" >> ~/.bashrc
$ echo "/home/pi/repo/room-raspberry/room-system.py" >> ~/.bashrc
$ crontab -e
Add line:
0 * * * * /home/pi/repo/room-raspberry/scripts/readhour.sh; /home/pi/repo/room-raspberry/scripts/checkmail.py
And lines for your alarm clocks.
# reboot
$ mpd ~/.config/mpd/mpd.conf
```

### Todos

 - Nothing now

### License
GNU GPL v3.0
Just do what you wish.

**Free Software, hell yeah**
