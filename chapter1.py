import cv2

# Import and show image. using open cv2
# img = cv2.imread("Resources/Photos/cat.jpg")
# cv2.imshow("pic",img)
# cv2.waitKey(0)

# import and show Video files.
# cap = cv2.VideoCapture("/Users/arthitkhotsaenlee/pythonProject/OpenCV_study/Resources/Videos/kitten.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     # print(success) # check whether Video playing or not.
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# Using wabcam
cap = cv2.VideoCapture(0)
cap.set(3,640) # set wide
cap.set(4,480) # set height
cap.set(10,1000) # set brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    # print(success) # check whether Video playing or not.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break