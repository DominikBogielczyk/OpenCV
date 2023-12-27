import cv2 as cv
import numpy as np


def empty_callback(value):
    # print(f'Trackbar reporting for duty with value: {value}')
    pass


img = cv.imread("../images/coins.jpg", cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# edges detect
edges = cv.Canny(gray, 255, 255)

kernel = np.ones((13, 13), np.uint8)
closing = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)
cv.imshow("Edges", edges)
cv.imshow("Closing", closing)
cv.imshow("Result", img)

# circles detect parameters
p1 = 50
p2 = 17
minR = 35
maxR = 106
# cv.createTrackbar('p1', 'Result', p1, 255, empty_callback)
# cv.createTrackbar('p2', 'Result', p2, 255, empty_callback)
# cv.createTrackbar('min', 'Result', minR, 100, empty_callback)
# cv.createTrackbar('max', 'Result', maxR, 200, empty_callback)

key_code = 0

while True:
    # trackbar update live
    result = img.copy()

    if key_code == 27:
        # escape key pressed
        break

    # CIRCLES
    # p1 = cv.getTrackbarPos('p1', 'Result')
    # p2 = cv.getTrackbarPos('p2', 'Result')
    # minR = cv.getTrackbarPos('min', 'Result')
    # maxR = cv.getTrackbarPos('max', 'Result')

    circles = cv.HoughCircles(closing, cv.HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=minR, maxRadius=maxR)
    circles = np.uint16(np.around(circles))

    value = 0
    for i in circles[0, :]:
        x, y, r = i

        # 10 gr
        if r in range(48, 100):
            cv.circle(result, (x, y), r, (0, 140, 255), 5)
            value += 0.1
        # 1 zl
        elif r in range(100, 112):
            cv.circle(result, (x, y), r, (0, 0, 255), 5)
            value += 1

    cv.putText(result, str('%.2f' % value) + " PLN", (result.shape[1] // 2, 50), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0))
    cv.imshow("Result", result)
    key_code = cv.waitKey(0)
    cv.imwrite("coins_count.png", result)

