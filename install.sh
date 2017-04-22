#!/usr/bin/env bash

mkdir /home/pi/repo
cd /home/pi/repo
git clone https://github.com/qeni/room-raspberry
apt-get update
apt-get install python python3 python3-feedparser mpd mpc cron mpg123 python3-pip
pip3 install pyowm stravalib
systemctl enable cron
systemctl start cron
mkdir -o /home/pi/.config/mpd
cp /home/pi/repo/room-raspberry/configs/mpd.conf /home/pi/.config/mpd/mpd.conf
echo "/home/pi/repo/room-raspberry/scripts/init.sh" >> ~/.bashrc
echo "sleep 3" >> ~/.bashrc
echo "/home/pi/repo/room-raspberry/controller.py" >> ~/.bashrc
