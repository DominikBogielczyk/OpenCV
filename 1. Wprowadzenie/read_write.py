import cv2 as cv
import sys


def main():
    # image read
    img = cv.imread("../images/AdditiveColor.png", cv.IMREAD_REDUCED_COLOR_2)
    img_grayscale = cv.imread("../images/AdditiveColor.png", cv.IMREAD_REDUCED_GRAYSCALE_2)
    if img is None:
        sys.exit("Could not read the image.")

    # G=0, R=0
    # img[:,:,1] = 0
    # img[:,:,2] = 0

    # padding = cv.copyMakeBorder(img, 300, 0, 0, 0, cv.BORDER_REFLECT)
    # b, g, r = cv.split(img) - split is not optimal solution
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    img256 = img[:256, :256, :]

    # IMAGE SHOW
    cv.imshow("b window", b)
    cv.imshow("g window", g)
    cv.imshow("r window", r)

    img[256:512, :256, :] = img256
    cv.imshow("img window", img)
    cv.imshow("img256 window", img256)

    # IMAGE MATRIX SIZE
    print('Color shape: ', img.shape)
    print('Grayscale shape: ', img_grayscale.shape)

    print(f'Pixel [220, 270]:{img[220, 270]}')
    print(f'Pixel grayscale [220, 270]:{img_grayscale[220, 270]}')

    k = cv.waitKey(0)

    # IMAGE SAVE
    if k == ord('s'):
        cv.imwrite("img1.png", img)


if __name__ == '__main__':
    main()
