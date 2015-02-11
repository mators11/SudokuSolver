import cv2
import numpy as np

def PreProcess(path):
    img = cv2.imread(path)
    img = cv2.resize(img,(500,500))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray,(9,9),0)
    return blr

def FindSquare(image):
    thresh = cv2.adaptiveThreshold(image,255,1,1,5,2)
    thresh,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    biggest = None
    max_area = 0
    for i in contours:
            area = cv2.contourArea(i)
            if area > 100:
                    peri = cv2.arcLength(i,True)
                    approx = cv2.approxPolyDP(i,0.02*peri,True)
                    if area > max_area and len(approx)==4:
                            biggest = approx
                            max_area = area

    cv2.drawContours(image,contours,-1,(0,0,255),3)
    cv2.namedWindow('Output',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Output',image)
    cv2.waitKey()
    cv2.destroyAllWindows()

    return image

image = PreProcess('test_sudoku1.jpg')
image = FindSquare(image)

