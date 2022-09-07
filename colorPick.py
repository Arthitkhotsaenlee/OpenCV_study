"""
This python script are going to develop the function to detect color from wab cam
"""
import cv2
import numpy as np
from chapter6 import stackImages

def get_parameter():
   pass

def camera():
    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    cam.set(10,150)
    return cam


# creaate TrackBars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,640)
cv2.createTrackbar("Hue min","TrackBars",0,179,get_parameter) # onChane = It will call the function while the value changed
cv2.createTrackbar("Hue max","TrackBars",179,179,get_parameter)
cv2.createTrackbar("Sat min","TrackBars",0,255,get_parameter)
cv2.createTrackbar("Sat max","TrackBars",255,255,get_parameter)
cv2.createTrackbar("Val min","TrackBars",0,255,get_parameter)
cv2.createTrackbar("Val max","TrackBars",255,255,get_parameter)



def main():
    cam = camera()
    while True:
        _, img = cam.read()

        # Get trackBars Values
        h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val max", "TrackBars")
        print(h_min,h_max,s_min,s_max,v_min,v_max)
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])
        # Convert HSV image and color threshold
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV,lowerb=lower, upperb=upper)
        imgResult = cv2.bitwise_and(img,img,mask=mask)
        #stack images
        imgStack = stackImages(imgArray=([img,imgHSV],[mask,imgResult]),scale=0.6)
        cv2.imshow("Stack Images", imgStack)
        if cv2.waitKey(100) and 0xFF == ord("q"):
            break

if __name__ == "__main__":
    main()