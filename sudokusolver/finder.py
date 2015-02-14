#!/usr/bin/python
# encoding: utf-8
import cv2
import numpy as np


def pre_process(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (500, 500))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (1, 1), 0)
    mask = np.zeros(gray.shape, np.uint8)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))

    close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel1)
    div = np.float32(gray) / close
    res = np.uint8(cv2.normalize(div, div, 0, 255, cv2.NORM_MINMAX))
    return res


def find_square(res):

    # Finds the big sudoku square
    res2 = cv2.cvtColor(res, cv2.COLOR_GRAY2BGR)
    thresh = cv2.adaptiveThreshold(res, 255, 0, 1, 19, 2,)
    (contours, hierarchy) = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    biggest = find_biggest(contours)

    # Creates mask
    kernelx = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 10))
    dx = cv2.Sobel(res, cv2.CV_16S, 1, 0)
    dx = cv2.convertScaleAbs(dx)
    cv2.normalize(dx, dx, 0, 255, cv2.NORM_MINMAX)
    (ret, close) = cv2.threshold(dx, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    close = cv2.morphologyEx(close, cv2.MORPH_DILATE, kernelx, iterations=1)

    # Finds the grid in the x-axis
    (contour, hier) = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contour:
        (x, y, w, h) = cv2.boundingRect(cnt)
        if h / w > 5:
            cv2.drawContours(close, [cnt], 0, 255, -1)
        else:
            cv2.drawContours(close, [cnt], 0, 0, -1)
    close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, None, iterations=2)
    closex = close.copy()

    # Finds the grid in the y-axis
    kernely = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 2))
    dy = cv2.Sobel(res, cv2.CV_16S, 0, 2)
    dy = cv2.convertScaleAbs(dy)
    cv2.normalize(dy, dy, 0, 255, cv2.NORM_MINMAX)
    (ret, close) = cv2.threshold(dy, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    close = cv2.morphologyEx(close, cv2.MORPH_DILATE, kernely)

    # Merges the x-axis and y-axis to get vertices
    (contour, hier) = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contour:
        (x, y, w, h) = cv2.boundingRect(cnt)
        if w / h > 5:
            cv2.drawContours(close, [cnt], 0, 255, -1)
        else:
            cv2.drawContours(close, [cnt], 0, 0, -1)

    close = cv2.morphologyEx(close, cv2.MORPH_DILATE, None, iterations=2)
    closey = close.copy()
    res = cv2.bitwise_and(closex, closey)

    # Extracts vertices
    (contour, hier) = cv2.findContours(res, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    centroids = []
    for cnt in contour:
        mom = cv2.moments(cnt)
        (x, y) = (int(mom['m10'] / mom['m00']), int(mom['m01'] / mom['m00']))
        centroids.append((x, y))

    centroids = np.array(centroids, dtype=np.float32)
    print np.shape(centroids)
    c = centroids.reshape((102, 2))
    c2 = c[np.argsort(c[:, 1])]

    b = np.vstack([c2[i * 10:(i + 1) * 10][np.argsort(c2[i * 10:(i + 1) * 10, 0])] for i in xrange(10)])
    bm = b.reshape((10, 10, 2))

    output = np.zeros((450, 450, 3), np.uint8)
    for (i, j) in enumerate(b):
        ri = i / 10
        ci = i % 10
        if ci != 9 and ri != 9:
            # Calculates position of each vertex in new img, and warps each square to the exact position
            src = bm[ri:ri + 2, ci:ci + 2, :].reshape((4, 2))
            dst = np.array([[ci * 50, ri * 50], [(ci + 1) * 50 - 1, ri * 50], [ci * 50, (ri + 1) * 50 - 1], [(ci + 1) * 50 - 1, (ri + 1)
                           * 50 - 1]], np.float32)
            retval = cv2.getPerspectiveTransform(src, dst)
            warp = cv2.warpPerspective(res2, retval, (450, 450))
            output[ri * 50:(ri + 1) * 50 - 1, ci * 50:(ci + 1) * 50 - 1] = warp[ri * 50:(ri + 1) * 50 - 1, ci * 50:(ci + 1) * 50 - 1].copy()

            # Show the output in a window
            cv2.namedWindow('Output', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('Output', output)
            cv2.waitKey()
            cv2.destroyAllWindows()

    return output


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

# TODO implement this
def find_sudoku(path):
    return None # returns a list of lists the sudoku puzzle read from image at path)

if __name__ == '__main__':
    test_image = pre_process('../img/test_sudoku1.jpg')
    test_square = find_square(test_image)

