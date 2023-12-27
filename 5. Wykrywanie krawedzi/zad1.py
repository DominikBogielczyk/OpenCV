import cv2 as cv
import numpy as np


img = cv.imread("../images/funny_image.png", cv.IMREAD_REDUCED_GRAYSCALE_2)

kernel_prewitt = np.array([[1, 0, -1],
                    [1, 0, -1],
                    [1, 0, -1]])
prewitt = cv.filter2D(src=img, ddepth=-1, kernel=kernel_prewitt)

kernel_sobel = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])
sobel = cv.filter2D(src=img, ddepth=-1, kernel=kernel_sobel)

cv.imshow("img", img)
cv.imshow("prewitt", prewitt)
cv.imshow("sobel", sobel)
cv.waitKey(0)
