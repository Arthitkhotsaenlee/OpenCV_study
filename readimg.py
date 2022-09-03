import cv2


if __name__ == "__main__":
    img = cv2.imread("Resources/Photos/cat_large.jpg")
    cv2.imshow("cat",img)
    cv2.waitKey(0)
    print("finish")