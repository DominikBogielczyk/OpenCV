import numpy as np
import cv2 as cv


# mouse callback function
def get_x_y(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        points.append([x, y])

        if len(points) == 4:
            pts1 = np.float32(points)
            pts2 = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])
            matrix = cv.getPerspectiveTransform(pts1, pts2)
            dst = cv.warpPerspective(img, matrix, (600, 600))
            cv.imshow("output", dst)


# Create a black image, a window and bind the function to window
img = cv.imread("../images/road.jpg", cv.IMREAD_REDUCED_COLOR_4)
cv.namedWindow('image')
cv.setMouseCallback('image', get_x_y)

points = []

while True:
    cv.imshow('image', img)
    key = cv.waitKey(20)
    # ESCAPE
    if key == 27:
        break

cv.destroyAllWindows()
