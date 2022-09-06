"""
Warp perspective "Bird eyes view"
"""
import cv2
import numpy as np

width, height = 250,350
img = cv2.imread("Resources/Photos/pokemon_card.jpg")
pts1 = np.float32([[111,300],[287,188],[154,482],[352,440]])  # declare 4 conner point of interesting
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])  # The referent tranfrom points
metrix = cv2.getPerspectiveTransform(pts1,pts2)

imgoutput = cv2.warpPerspective(img,metrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output Image",imgoutput)
cv2.waitKey(0)