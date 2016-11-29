#!/usr/bin/env bash

dir="/home/pi/repo/room-raspberry/sounds/hours"

hour=$(date +"%H")

if [ "$hour" -eq 13 ]; then
    mpg123 $dir/hours_one.mp3
    exit;
elif [ "$hour" -eq 14 ]; then
    mpg123 $dir/hours_two.mp3
    exit;
elif [ "$hour" -eq 15 ]; then
    mpg123 $dir/hours_three.mp3
    exit;
elif [ "$hour" -eq 16 ]; then
    mpg123 $dir/hours_four.mp3
    exit;
elif [ "$hour" -eq 17 ]; then
    mpg123 $dir/hours_five.mp3
    exit;
elif [ "$hour" -eq 18 ]; then
    mpg123 $dir/hours_six.mp3
    exit;
elif [ "$hour" -eq 19 ]; then
    mpg123 $dir/hours_seven.mp3
    exit;
elif [ "$hour" -eq 8 || "$hour" -eq 20 ]; then
    mpg123 $dir/hours_eight.mp3
    exit;
elif [ "$hour" -eq 9 || "$hour" -eq 21 ]; then
    mpg123 $dir/hours_nine.mp3
    exit;
elif [ "$hour" -eq 10 ]; then
    mpg123 $dir/hours_ten.mp3
    exit;
elif [ "$hour" -eq 11 ]; then
    mpg123 $dir/hours_eleven.mp3
    exit;
elif [ "$hour" -eq 12 ]; then
    mpg123 $dir/hours_twelve.mp3
    exit;
fi
