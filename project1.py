"""
This project to hand on Opencv toolbox by develop the color tracking.
"""
import cv2
import numpy as np
from chapter6 import stackImages

myColor = []


def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lowerb=lower,upperb=upper)
    cv2.imshow("HSV image", imgHSV)


def main():
    frameWidth = 640
    frameHeigth = 480
    cap = cv2.VideoCapture(0)
    cap.set(3,frameWidth)
    cap.set(4,frameHeigth)
    cap.set(10,130)
    while True:
        succees, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(500) and 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()