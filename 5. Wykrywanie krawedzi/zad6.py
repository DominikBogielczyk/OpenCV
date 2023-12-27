import cv2 as cv
import numpy as np


def empty_callback(value):
    # print(f'Trackbar reporting for duty with value: {value}')
    pass


img = cv.imread("../images/fruit.jpg", cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# edges detect
edges = cv.Canny(gray, 200, 255)

cv.imshow("Result", img)
cv.imshow("Edges", edges)

# circles detect parameters
p1 = 50
p2 = 25
minR = 97
maxR = 142
# cv.createTrackbar('p1', 'Result', p1, 255, empty_callback)
# cv.createTrackbar('p2', 'Result', p2, 255, empty_callback)
# cv.createTrackbar('min', 'Result', minR, 100, empty_callback)
# cv.createTrackbar('max', 'Result', maxR, 200, empty_callback)

# apple filtering - threshold
ret, threshApple = cv.threshold(gray, 140, 255, cv.THRESH_BINARY_INV)

while True:
    # trackbar update live
    result = img.copy()

    key_code = cv.waitKey(1000)
    if key_code == 27:
        # escape key pressed
        break

    # CIRCLES
    # p1 = cv.getTrackbarPos('p1', 'Result')
    # p2 = cv.getTrackbarPos('p2', 'Result')
    # minR = cv.getTrackbarPos('min', 'Result')
    # maxR = cv.getTrackbarPos('max', 'Result')

    circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=minR, maxRadius=maxR)
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        x, y, r = i
        # apple because threshApple detect middle of the apple
        if threshApple[y][x] > 200:
            cv.circle(result, (x, y), r, (0, 255, 0), 5)
        # orange
        else:
            cv.circle(result, (x, y), r, (0, 140, 255), 5)

    cv.imshow("Result", result)



