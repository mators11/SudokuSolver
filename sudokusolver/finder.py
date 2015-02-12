import cv2
import numpy as np

def pre_process(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (500, 500))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (3, 3), 0)
    return blr


def find_square(image):
    thresh = cv2.adaptiveThreshold(image, 255, 1, 1, 5, 2)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    biggest = find_biggest(contours)
    

    cv2.drawContours(image, biggest, -1, (255, 255, 255), 10)
    cv2.namedWindow('Output', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Output', image)
    cv2.waitKey()
    cv2.destroyAllWindows()

    return image

def find_biggest(contours):
    biggest = None
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 100:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest

if __name__ == "__main__":
    test_image = pre_process('../img/test_sudoku1.jpg')
    test_square = find_square(test_image)

