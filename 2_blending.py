import cv2


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')


cv2.namedWindow('Images blending', cv2.WINDOW_AUTOSIZE)

first_img = cv2.imread(cv2.samples.findFile("funny_image.png"), cv2.IMREAD_COLOR)
second_img = cv2.imread(cv2.samples.findFile("logo.png"), cv2.IMREAD_COLOR)

img1 = cv2.resize(first_img, (0, 0), fx=512/first_img.shape[0], fy=512/first_img.shape[1], interpolation=cv2.INTER_LINEAR)
img2 = cv2.resize(second_img, (0, 0), fx=512/second_img.shape[0], fy=512/second_img.shape[1], interpolation=cv2.INTER_LINEAR)
cv2.createTrackbar('alpha [%]', 'Images blending', 0, 100, empty_callback)


def main():
    while True:
        key_code = cv2.waitKey(10)
        if key_code == 27:
            # escape key pressed
            break
        v = cv2.getTrackbarPos('alpha [%]', 'Images blending')
        alpha = v/100
        dst = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)

        cv2.imshow('Images blending', dst)


if __name__ == '__main__':
    main()