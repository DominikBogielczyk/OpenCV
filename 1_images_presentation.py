import cv2


def main():
    images = ["AdditiveColor.png", "funny_image.png", "logo.png", "qr.jpg"]
    i = 0
    img = cv2.imread(cv2.samples.findFile(images[i]), cv2.IMREAD_COLOR)
    img1 = cv2.resize(img, (0, 0), fx=512 / img.shape[0], fy=512 / img.shape[1], interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Display window", img1)

    key = ord('a')

    while key != ord('e'):
        if key == ord('w'):
            i += 1
            if i >= len(images):
                i = 0
            # IMAGE READ
            img = cv2.imread(cv2.samples.findFile(images[i]), cv2.IMREAD_COLOR)
            img1 = cv2.resize(img, (0, 0), fx=512/img.shape[0], fy=512/img.shape[1], interpolation=cv2.INTER_LINEAR)

        elif key == ord('q'):
            i -= 1
            if i < 0:
                i = len(images) - 1
            img = cv2.imread(cv2.samples.findFile(images[i]), cv2.IMREAD_COLOR)
            img1 = cv2.resize(img, (0, 0), fx=512 / img.shape[0], fy=512 / img.shape[1], interpolation=cv2.INTER_LINEAR)

        #IMAGE SHOW
        cv2.imshow("Display window", img1)
        key = cv2.waitKey(0)

if __name__ == '__main__':
    main()