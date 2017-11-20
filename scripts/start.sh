#!/bin/sh

/usr/bin/python3 /home/pi/Desktop/dev/python/robotcontroller/app.py &
/home/pi/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -o "/home/pi/mjpg-streamer/mjpg-streamer-experimental/output_http.so -w ./www" -i "/home/pi/mjpg-streamer/mjpg-streamer-experimental/input_raspicam.so" &
