import cv2


img = cv2.imread("../images/lenna_noise.bmp")


def callback(n):
    # n have to be odd
    if n % 2 == 0:
        n += 1

    aver = cv2.blur(img, (n, n))
    cv2.imshow("Averaging filter", aver)

    gaussian = cv2.GaussianBlur(img, (n, n), 0)
    cv2.imshow("Gaussian filter", gaussian)

    median = cv2.medianBlur(img, n)
    cv2.imshow("Median filter", median)


cv2.namedWindow("Averaging filter")
cv2.moveWindow("Averaging filter", 500, 0)
cv2.namedWindow("Gaussian filter")
cv2.moveWindow("Gaussian filter", 1000, 0)
cv2.namedWindow("Median filter")
cv2.moveWindow("Median filter", 500, 400)

cv2.namedWindow("Input image")
cv2.moveWindow("Input image", 0, 0)
cv2.imshow("Input image", img)
cv2.createTrackbar('Filter size', 'Input image', 1, 10, callback)


while True:
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key
        break

    cv2.getTrackbarPos("Filter size", "Input image")


cv2.destroyAllWindows()
