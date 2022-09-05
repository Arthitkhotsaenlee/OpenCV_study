import cv2


def rescale(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(img,dimensions,interpolation=cv2.INTER_AREA)


if __name__ == "__main__":
    img = cv2.imread("Resources/Photos/cat_large.jpg")
    img = rescale(img,scale=0.2)
    cv2.imshow("cat",img)
    cv2.waitKey(0)
    print("finish")