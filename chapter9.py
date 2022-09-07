"""
This chapter is going to learn How to use the machine learning model to face detection.
"""
import cv2
import numpy as np

haarcascade = "/Users/arthitkhotsaenlee/opt/anaconda3/envs/OpenCV_study/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(haarcascade,)

img =cv2.imread("Resources/Photos/group 1.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

face = faceCascade.detectMultiScale(imgGray,10.1,1)

# create rectango Boxs
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)

cv2.imshow("Face detection", img)
cv2.waitKey(0)