import cv2


def every3white():
    img = cv2.imread("../images/funny_image.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
    img2 = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if j % 3 == 0:
                img2[i][j] = 0

    cv2.imshow("Input image", img)
    cv2.imshow("Output image", img2)


if __name__ == "__main__":
    every3white()
    # wait for press any key
    key_code = cv2.waitKey(0)

cv2.destroyAllWindows()
