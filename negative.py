import cv2

cv2.namedWindow("Input image")
cv2.namedWindow("Output image")

img = cv2.imread("funny_image.png", cv2.IMREAD_REDUCED_COLOR_2)
img_not = cv2.bitwise_not(img)

cv2.imshow("Input image", img)
cv2.imshow("Output image", img_not)

cv2.waitKey(0)
cv2.destroyAllWindows()


