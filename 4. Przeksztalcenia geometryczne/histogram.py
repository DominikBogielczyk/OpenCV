import cv2 as cv
from matplotlib import pyplot as plt

img_color = cv.imread("../images/road.jpg", cv.IMREAD_REDUCED_COLOR_4)
hist_color = cv.calcHist([img_color], [0], None, [256], [0, 256])

# first image - histogram color image
plt.figure("Histogram - color image")
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    h1 = cv.calcHist([img_color], [i], None, [256], [0, 256])
    plt.plot(h1, color=col)
    plt.xlim([0, 256])

# second figure - histogram mono image
plt.figure("Histogram - mono image")
img_mono = cv.imread("../images/road.jpg", cv.IMREAD_REDUCED_GRAYSCALE_4)
plt.hist(img_mono.ravel(), 256, [0, 256])

# show plots
plt.show()
