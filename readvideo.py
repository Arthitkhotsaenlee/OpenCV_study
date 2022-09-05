import cv2


if __name__ == "__main__":
    video = cv2.VideoCapture("Resources/Videos/dog.mp4")
    while True:
        isTrue, frame = video.read()
        cv2.imshow("Video",frame)
        cv2.waitKey(1)

    video.release()
    cv2.destroyAllWindows()
    print("finish")