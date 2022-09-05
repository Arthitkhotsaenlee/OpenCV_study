"""
This material going to teach basic functions.
"""
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv2.imread("Resources/Photos/cat.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7,),0)
imgCanny = cv2.Canny(img,100,200)
imgDialation = cv2.dilate(imgCanny,kernel=kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel=kernel,iterations=1)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroaded image", imgEroded)
cv2.waitKey(0)