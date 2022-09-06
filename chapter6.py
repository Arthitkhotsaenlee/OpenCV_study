"""
This chapter is going to learn join images.
"""
import cv2
import numpy as np
"""
In this method using numpy to stack the images quite simple, but there are some problem when the size of images stacked
are different e.i., one is black and write, and the one is RGB.
"""
# img = cv2.imread("Resources/Photos/cats.jpg")
#
# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("images",img)
# cv2.imshow("Horizental images",imgHor)
# cv2.imshow("Vertical images",imgVer)
# cv2.waitKey(0)

"""
Here is the solution to solve the problem follow the first problem.
"""
def stackImages(imgArray,scale,lables=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    sizeW = imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range (0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver
if __name__ == "__main__":
    img =cv2.imread("Resources/Photos/lady.jpg")
    imgStack = stackImages(imgArray=([img,img,img],),scale=0.5)
    cv2.imshow("Stack images",imgStack)
    cv2.waitKey(0)