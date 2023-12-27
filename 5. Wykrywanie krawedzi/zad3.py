import cv2 as cv
import numpy as np


def empty_callback(value):
    # print(f'Trackbar reporting for duty with value: {value}')
    pass


img = cv.imread("../images/coins.jpg", cv.IMREAD_GRAYSCALE)
# ret, img = cv.threshold(img, 160, 255, cv.THRESH_BINARY_INV)
cv.imshow("Input", img)
cv.createTrackbar('Threshold1', 'Input', 0, 255, empty_callback)
cv.createTrackbar('Threshold2', 'Input', 0, 255, empty_callback)

while True:
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv.waitKey(20)
    if key_code == 27:
        # escape key pressed
        break

    thr1 = cv.getTrackbarPos('Threshold1', 'Input')
    thr2 = cv.getTrackbarPos('Threshold2', 'Input')

    edges = cv.Canny(img, thr1, thr2)
    cv.imshow('Edges', edges)
