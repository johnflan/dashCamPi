#!/usr/bin/python

import numpy as np
import cv2
from time import gmtime, strftime
import time

rolloverMinutes = 20
rollover = rolloverMinutes * 60


def show_webcam():
    print "Starting capture"
    while True:
        timestamp = int(round(time.time()))
        lastRollover = timestamp
        fourcc = cv2.cv.CV_FOURCC(*'XVID')
        filename=str(timestamp) + ".avi"
        print "writing to " + filename
        out = cv2.VideoWriter(filename,fourcc, 10.0, (640,480))
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        cam.set(4, 480)
        while True:
	    ret_val, img = cam.read()
            addText(img)
            out.write(img)
            if(timestamp != lastRollover and (timestamp % rollover) == 0):
                lastRollover = timestamp
                break
            timestamp = int(round(time.time()))
        cam.release()
        out.release()
        print "rolled over"

def addText(frame):
    cv2.rectangle(frame,(10,10),(630,40),(0,0,0),-1)
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'DashCam - ' + timestamp ,(180,30), font,
            .5,(255,255,255),1,cv2.CV_AA)
def main():
    show_webcam()

if __name__ == '__main__':
    main()
