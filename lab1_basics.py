import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt


def main():
    #IMAGE READ
    img = cv.imread(cv.samples.findFile("AdditiveColor.png"), cv.IMREAD_REDUCED_COLOR_2)
    if img is None:
        sys.exit("Could not read the image.")

    #G=0, R=0
    #img[:,:,1] = 0
    #img[:,:,2] = 0

    padding = cv.copyMakeBorder(img, 300, 0, 0, 0, cv.BORDER_REFLECT)

    #head = img[:500, 980:1400]
    #img[:500, 480:900] = head
    #img[:500, 0:420] = head

    #b, g, r = cv.split(img)
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    #IMAGE SHOW
    cv.imshow("b window", b)
    cv.imshow("g window", g)
    cv.imshow("r window", r)
    cv.imshow("img window", img)

    #plt.imshow(head)
    #plt.show()

    #IMAGE MATRIX SIZE
    print(np.shape(img))
    print(img.shape)

    print(f'Pixel [200, 200]: {img[200,200]}')

    k = cv.waitKey(0)

    #IMAGE SAVE
    if k == ord('s'):
        cv.imwrite("boss_blue.png", img)


if __name__ == '__main__':
    main()