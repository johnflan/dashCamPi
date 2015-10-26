#!/bin/bash
nohup python /home/pi/dashCamPi/capture.py &
nohup python /home/pi/dashCamPi/removeOldestFiles.py &
