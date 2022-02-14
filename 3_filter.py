import cv2


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')


cv2.namedWindow("Input image")
cv2.namedWindow("Averaging filter")
cv2.moveWindow("Averaging filter", 500, 0)
cv2.namedWindow("Gaussian filter")
cv2.moveWindow("Gaussian filter", 1000, 0)
cv2.namedWindow("Median filter")
cv2.moveWindow("Median filter", 0, 500)

cv2.createTrackbar('Filter size', 'Input image', 1, 10, empty_callback)

while True:
    img = cv2.imread("images/lenna_salt_and_pepper.bmp")
    cv2.imshow("Input image", img)

    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key
        break

    n = cv2.getTrackbarPos("Filter size", "Input image")
    # n have to be odd
    if n % 2 == 0:
        n = n + 1

    aver = cv2.blur(img, (n, n))
    cv2.imshow("Averaging filter", aver)

    Gaussian = cv2.GaussianBlur(img, (n, n), 0)
    cv2.imshow("Gaussian filter", Gaussian)

    median = cv2.medianBlur(img, n)
    cv2.imshow("Median filter", median)

cv2.waitKey(0)
cv2.destroyAllWindows()
