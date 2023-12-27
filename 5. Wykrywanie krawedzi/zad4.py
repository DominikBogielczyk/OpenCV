import cv2 as cv
import numpy as np


def empty_callback(value):
    # print(f'Trackbar reporting for duty with value: {value}')
    pass


img = cv.imread("../images/shapes.jpg", cv.IMREAD_REDUCED_COLOR_2)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 15, 50)

cv.imshow("Input", img)
cv.imshow("Edges", edges)

thr = 30
min_length = 21
max_gap = 2
# cv.createTrackbar('threshold', 'Input', thr, 100, empty_callback)
# cv.createTrackbar('min_length', 'Input', min_length, 50, empty_callback)
# cv.createTrackbar('max_gap', 'Input', max_gap, 50, empty_callback)

while True:
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv.waitKey(20)
    if key_code == 27:
        # escape key pressed
        break

    # LINES
    # thr = cv.getTrackbarPos('threshold', 'Input')
    # min_length = cv.getTrackbarPos('min_length', 'Input')
    # max_gap = cv.getTrackbarPos('max_gap', 'Input')

    # cv.HoughLines(image, rho, theta, threshold, minLineLength, maxLineGap)
    result = img.copy()
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, thr, minLineLength=min_length, maxLineGap=max_gap)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(result, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # CIRCLES
    circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=50)
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        # draw the outer circle
        cv.circle(result, (i[0], i[1]), i[2], (255, 0, 0), 5)
        # draw the center of the circle
        cv.circle(result, (i[0], i[1]), 2, (0, 0, 255), 5)

    cv.imshow("Output", result)
