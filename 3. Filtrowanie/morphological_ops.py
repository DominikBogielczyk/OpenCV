import cv2


def callback(value):
    erosion = cv2.erode(thresh, (5, 5), iterations=1)
    cv2.imshow("After erosion", erosion)

    dilation = cv2.dilate(thresh, (5, 5), iterations=1)
    cv2.imshow("After dilation", dilation)

    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, (5, 5))
    cv2.imshow("Closing", closing)


cv2.namedWindow("After erosion")
cv2.moveWindow("After erosion", 600, 0)
cv2.namedWindow("After dilation")
cv2.moveWindow("After dilation", 0, 500)
cv2.namedWindow("Closing")
cv2.moveWindow("Closing", 1200, 0)
img = cv2.imread("../images/funny_image.png", cv2.IMREAD_REDUCED_GRAYSCALE_4)

cv2.namedWindow('Input image')
cv2.createTrackbar('Threshold', 'Input image', 0, 255, callback)

while True:
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key
        break

    thr = cv2.getTrackbarPos('Threshold', 'Input image')
    ret, thresh = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY)
    cv2.imshow('Input image', thresh)


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()
