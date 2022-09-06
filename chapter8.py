"""
This chapter is going to learn about How to operation with contour and shape.
"""
import cv2
import numpy as np
from chapter6 import stackImages

img = cv2.imread("Resources/Photos/shapes-basic-color.png")
img = cv2.resize(img,(400,400))
imgBlank = np.zeros((400,400,3))

imgGray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
# Use canny to fine the edged of the shape.
imgCanny = cv2.Canny(imgBlur,50,50)

stack_img = stackImages(([img,imgGray,imgBlur],[imgCanny]),
                        scale=0.6)
cv2.imshow("Image",stack_img)
cv2.waitKey(0)
