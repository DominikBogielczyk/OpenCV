import cv2
import numpy as np

def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')


cv2.namedWindow('image')

img = cv2.imread(cv2.samples.findFile("boss.png"), cv2.IMREAD_REDUCED_GRAYSCALE_2)

cv2.createTrackbar('Threshold', 'image', 0, 255, empty_callback)
cv2.createTrackbar('Type', 'image', 0, 4, empty_callback)

while True:
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break

    thr = cv2.getTrackbarPos('Threshold', 'image')
    type = cv2.getTrackbarPos('Type', 'image')
    if type == 0:
        ret, thresh = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY)
    elif type == 1:
        ret, thresh = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY_INV)
    elif type == 2:
        ret, thresh = cv2.threshold(img, thr, 255, cv2.THRESH_TRUNC)
    elif type == 3:
        ret, thresh = cv2.threshold(img, thr, 255, cv2.THRESH_TOZERO)
    else:
        ret, thresh = cv2.threshold(img, thr, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('image', thresh)


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()