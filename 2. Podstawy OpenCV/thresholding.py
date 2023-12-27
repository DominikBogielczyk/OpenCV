import cv2
import os


def empty_callback(value):
    # print(f'Trackbar reporting for duty with value: {value}')
    pass


# image read
img = cv2.imread("../images/fruit.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2)

cv2.namedWindow('image')
cv2.createTrackbar('Threshold1', 'image', 0, 255, empty_callback)
cv2.createTrackbar('Threshold2', 'image', 0, 255, empty_callback)
cv2.createTrackbar('Type', 'image', 0, 4, empty_callback)

while True:
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break

    thr1 = cv2.getTrackbarPos('Threshold1', 'image')
    thr2 = cv2.getTrackbarPos('Threshold2', 'image')
    threshold_type = cv2.getTrackbarPos('Type', 'image')

    if threshold_type == 0:
        ret, thresh = cv2.threshold(img, thr1, thr2, cv2.THRESH_BINARY)
    elif threshold_type == 1:
        ret, thresh = cv2.threshold(img, thr1, thr2, cv2.THRESH_BINARY_INV)
    elif threshold_type == 2:
        ret, thresh = cv2.threshold(img, thr1, thr2, cv2.THRESH_TRUNC)
    elif threshold_type == 3:
        ret, thresh = cv2.threshold(img, thr1, thr2, cv2.THRESH_TOZERO)
    else:
        ret, thresh = cv2.threshold(img, thr1, thr2, cv2.THRESH_TOZERO_INV)
    cv2.imshow('image', thresh)


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()