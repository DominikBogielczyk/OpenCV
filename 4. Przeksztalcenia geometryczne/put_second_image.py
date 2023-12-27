import cv2 as cv
import numpy as np


# mouse callback function
def mouse_handle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        points.append([x, y])

        if len(points) == 4:
            # pug image to new perspective
            fg_img = cv.imread("../images/pug.png")
            fg_height, fg_width = fg_img.shape[:2]
            pts1 = np.float32([[0, 0], [fg_width, 0], [0, fg_height], [fg_width, fg_height]])
            pts2 = np.float32(points)
            matrix = cv.getPerspectiveTransform(pts1, pts2)
            bk_height, bk_width = bk_img.shape[:2]
            dst = cv.warpPerspective(fg_img, matrix, (bk_width, bk_height))

            # thresholding - white background dst image
            ret, mask = cv.threshold(dst, 1, 255, cv.THRESH_BINARY)
            mask_inv = cv.bitwise_not(mask)

            # background && mask
            result = cv.bitwise_and(bk_img, mask_inv)

            # background || foreground perspective
            result = cv.bitwise_or(result, dst)

            cv.imshow('result', result)


bk_img = cv.imread("../images/gallery.png")
bk_img = cv.resize(bk_img, (0, 0), fx=0.7, fy=0.7, interpolation=cv.INTER_LINEAR)
cv.imshow('image', bk_img)
cv.setMouseCallback('image', mouse_handle)

points = []

while True:
    key = cv.waitKey(20)
    # ESCAPE
    if key == 27:
        break


cv.destroyAllWindows()
