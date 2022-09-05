"""
This chapter is going to learn how to write the shape to the image.
"""
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img_shape = np.zeros((512,512,3),np.uint8)

print(img.shape)  # check the size of image.

# this session show how to write color to the image.
img[:] = 255,0,0  # Blue color (b,g,r)
img[200:500,100:300] = 0,255,0 # change color with defined session.

# Write line to the image.
img_shape = cv2.line(img_shape,(0,0),(img_shape.shape[1],img_shape.shape[0]),(0,255,0),3)

# write the rectangle
img_shape = cv2.rectangle(img_shape,(10,10),(500,500),(0,0,250),10,2)
# put circle to image
img_shape = cv2.circle(img_shape,(300,200),30,(0,255,0),3)
# put text on image.
img_shape = cv2.putText(img_shape,"Yed Hee",(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,250),3)

cv2.imshow("Image", img)
cv2.imshow("write shape image", img_shape)
cv2.waitKey(0)