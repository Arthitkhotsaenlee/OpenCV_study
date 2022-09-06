"""
This chapter is going to study How to color detection.
"""
import cv2
import numpy as np
from chapter6 import stackImages

def get_parameter():
   pass

# import image.
img = cv2.imread("Resources/Photos/car.jpg")

# creaate TrackBars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,640)
cv2.createTrackbar("Hue min","TrackBars",0,179,get_parameter) # onChane = It will call the function while the value changed
cv2.createTrackbar("Hue max","TrackBars",179,179,get_parameter)
cv2.createTrackbar("Sat min","TrackBars",0,255,get_parameter)
cv2.createTrackbar("Sat max","TrackBars",255,255,get_parameter)
cv2.createTrackbar("Val min","TrackBars",0,255,get_parameter)
cv2.createTrackbar("Val max","TrackBars",255,255,get_parameter)


while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
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
    mask =cv2.inRange(imgHSV,lowerb=lower, upperb=upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    imgStack = stackImages(imgArray=([img,imgHSV,mask,imgResult],),scale=0.6)


    # cv2.imshow("Image",img)
    # cv2.imshow("HSV Image",imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Mask", imgResult)
    cv2.imshow("Stack Images", imgStack)
    cv2.waitKey(2000)
