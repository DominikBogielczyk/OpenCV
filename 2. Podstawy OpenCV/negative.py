import cv2

# image read
img = cv2.imread("../images/funny_image.png", cv2.IMREAD_REDUCED_COLOR_2)
img_not = cv2.bitwise_not(img)
img2 = cv2.imread("../images/funny_image.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
img2_not = cv2.bitwise_not(img2)

cv2.imshow("Input image color", img)
cv2.imshow("Input image mono", img2)
cv2.imshow("Negative color image", img_not)
cv2.imshow("Negative mono image", img2_not)

cv2.waitKey(0)
cv2.destroyAllWindows()


