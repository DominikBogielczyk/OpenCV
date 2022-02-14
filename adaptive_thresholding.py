import cv2

cv2.namedWindow('ADAPTIVE_THRESH_MEAN')
cv2.namedWindow('ADAPTIVE_GAUSSIAN_MEAN')

img = cv2.imread(cv2.samples.findFile("funny_image.png"), cv2.IMREAD_REDUCED_GRAYSCALE_2)

th1 = cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY,
                               blockSize=7, C=4)

th2 = cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                               thresholdType=cv2.THRESH_BINARY, blockSize=7, C=4)

cv2.imshow('ADAPTIVE_THRESH_MEAN', th1)
cv2.imshow('ADAPTIVE_GAUSSIAN_MEAN', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()