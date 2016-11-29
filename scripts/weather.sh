#!/usr/bin/env bash

dir="/home/pi/repo/room-raspberry/sounds/temperatures"

abs () {
    # Check for numeric input
    if expr $1 + 0 2>/dev/null 1>&2 ; then
    # Is the number negative?
    if [ $1 -lt 0 ] ; then
        echo `expr 0 - $1`
    else
        echo $1
    fi
        return 0 # OK
    else
        return 1 # Not a number
    fi
}

temperature="$1"

if [[ "$temperature" -lt 0 ]]; then
    a=$(expr 0 - $temperature)
    mpg123 $dir/minus_$a.mp3
else
    mpg123 $dir/plus_$temperature.mp3
fi
