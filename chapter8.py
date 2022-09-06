"""
This chapter is going to learn about How to operation with contour and shape.
"""
import cv2
import numpy as np
from chapter6 import stackImages

def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(0,255,0),3)  # Draw contour edge image
            peri = cv2.arcLength(cnt,True)  # get the arc-length of the contour
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)  # This will give the conner points of each contour.
            print(len(approx))  # Print How many conner point of the shape.

img = cv2.imread("Resources/Photos/shapes-basic-color.png")
# img = cv2.resize(img,(400,400))
imgBlank = np.zeros((400,400,3))
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
# Use canny to fine the edged of the shape.
imgCanny = cv2.Canny(imgGray,50,50)
get_contours(imgCanny)

stack_img = stackImages(([img,imgGray,imgBlur],[imgCanny,imgContour]),
                        scale=0.6)
cv2.imshow("Image",stack_img)
cv2.waitKey(0)
