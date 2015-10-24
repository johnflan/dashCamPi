#!/usr/bin/python

import numpy as np
import cv2
from time import gmtime, strftime

def show_webcam():
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    cam = cv2.VideoCapture(0)
    while True:
	    ret_val, img = cam.read()
            addText(img)
            out.write(img)
	    if cv2.waitKey(1) == 27: 
		break  # esc to quit
    cam.release()
    out.release()

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
