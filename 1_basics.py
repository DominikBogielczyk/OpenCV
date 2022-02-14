import cv2 as cv
import sys
import numpy as np

def main():
    #IMAGE READ
    img = cv.imread(cv.samples.findFile("AdditiveColor.png"), cv.IMREAD_REDUCED_COLOR_2)
    if img is None:
        sys.exit("Could not read the image.")

    #G=0, R=0
    #img[:,:,1] = 0
    #img[:,:,2] = 0

    padding = cv.copyMakeBorder(img, 300, 0, 0, 0, cv.BORDER_REFLECT)
    #b, g, r = cv.split(img)
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    #IMAGE SHOW
    cv.imshow("b window", b)
    cv.imshow("g window", g)
    cv.imshow("r window", r)
    cv.imshow("img window", img)

    #IMAGE MATRIX SIZE
    print(np.shape(img))
    print(img.shape)

    print(f'Pixel [200, 200]:{img[200,200]}')

    k = cv.waitKey(0)

    #IMAGE SAVE
    if k == ord('s'):
        cv.imwrite("img1.png", img)

if __name__ == '__main__':
    main()