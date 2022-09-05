import cv2


if __name__ == "__main__":
    img = cv2.imread("Resources/Photos/cat.jpg")
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("CAT GAY",img_gray)
    cv2.imshow("cat",img)
    cv2.waitKey(0)
    print("finish")