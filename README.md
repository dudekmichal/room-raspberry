# Raspberry Pi Room

![N|Solid](https://raw.github.com/qeni/room-raspberry/master/img/powered_by.png)

This is project for my own room. It includes Raspberry Pi 2B, speakers, lcd 16x2 I2C display, control panel with keyboard.

  - Checking for new e-mails
  - Alarm clock with cron
  - MPD music server
  - Voice information about current time
  - Weather information from OWM (Open Weather Map) API

> LCD dysplay shows the most important informations.
> Panel controls playing music, alarm clocks
> Each key on keyboard do something (e.g. shows temperature, song info)
> Alarm clock gets random track from tracks named like alarm*.mp3 in ~/music


### Installation

If you want to use this stuff you will need to change a few things:
In file room-system.py set variable owm to pyowm.OWM('<your key>').
In file checkmail.py set USERNAME to your e-mail address.
In file checkmail.py set PASSWORD to your e-mail password.

Then install all dependencies on your RPi:

```sh
$ mkdir /home/pi/repo
$ cd /home/pi/repo
$ git clone https://github.com/qeni/room-raspberry
# pip install pyowm RPLCD
# apt-get install python python3 python-feedparser mpd mpc cron mpg123
# systemctl enable cron
# systemctl start cron
$ mkdir -o /home/pi/.config/mpd
$ cp /home/pi/repo/room-raspberry/configs/mpd.conf /home/pi/config/mpd/mpd.conf
$ echo "mpd ~/.config/mpd/mpd.conf" >> ~/.bashrc
$ crontab -e
Add line:
0 * * * * /home/pi/repo/room-raspberry/scripts/readhour.sh;sleep 1; /home/pi/repo/room-raspberry/scripts/checkmail.py
And lines for your alarm clocks.
# reboot
```

### Todos

 - Get case and connect all that stuff
 - Tests on Raspberry Pi 2B

### License
GNU GPL v3.0
Just do what you wish.

**Free Software, hell yeah**
