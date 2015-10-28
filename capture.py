#!/usr/bin/python

import numpy as np
import cv2
from time import gmtime, strftime
import time
import signal
import sys

rolloverMinutes = 15
rollover = rolloverMinutes * 60

shutdownRequest = False
log = open('/home/pi/dashCamPi/dashcam.log','a')

def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        timestamp = int(round(time.time()))
        lastRollover = timestamp
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        filename="/home/pi/dashCamPi/" + str(timestamp) + ".avi"
        log.write("\nRolled over " + filename + "\n")
        out = cv2.VideoWriter(filename,fourcc, 10.0, (640,480))
        log.write("\nVideoWriter status: " + str(out.isOpened()) + "\n")
        while True:
            ret_val, img = cam.read()
            addText(img)
            if (out.isOpened() == False):
                log.write("Error VideoWriter is not open\n")
                break
            out.write(img)
            if(timestamp != lastRollover and (timestamp % rollover) == 0):
                lastRollover = timestamp
                break
            timestamp = int(round(time.time()))
            if (shutdownRequest == True):
                out.release()
                cam.release()
                log.write("\nShutting down at " + str(timestamp) + "\n")
                log.close()
                sys.exit(0)
        out.release()
    cam.release()
    log.close()

def addText(frame):
    cv2.rectangle(frame,(10,10),(630,40),(0,0,0),-1)
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'DashCam - ' + timestamp ,(180,30), font, .5,(255,255,255),1,cv2.LINE_AA)

def signal_handler(signal, frame):
    log.write("\nStop requested\n")
    global shutdownRequest
    shutdownRequest = True

def main():
    show_webcam()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
