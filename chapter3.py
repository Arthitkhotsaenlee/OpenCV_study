"""
This chapter will going to learn how to resize and rescale the image.
"""
import cv2

img = cv2.imread("Resources/Photos/cats.jpg")
print(img.shape)
# this session to learn how to resize the image
imgResize = cv2.resize(img,(300, 200))  # (width,height)
print(imgResize.shape)

# this session  to learn how to crop the image.
imCroped = img[0:200,200:500]  # (Height_start:Height_end, Width_start:Width_end)

cv2.imshow("Image", img)
cv2.imshow("Image resize", imgResize)
cv2.imshow("Image Croped", imCroped)
cv2.waitKey(0)