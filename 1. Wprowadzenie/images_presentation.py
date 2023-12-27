import cv2
import os


def main():
    images = os.listdir("../images")
    i = 0
    # image read
    img = cv2.imread(cv2.samples.findFile("../images/" + images[i]), cv2.IMREAD_COLOR)
    img1 = cv2.resize(img, (0, 0), fx=512 / img.shape[0], fy=512 / img.shape[1], interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Display window", img1)

    key = ord('a')

    while key != ord('e'):
        if key == ord('w'):
            i += 1

        elif key == ord('q'):
            i -= 1

        i %= len(images)

        print('update')
        img = cv2.imread(cv2.samples.findFile("../images/" + images[i]), cv2.IMREAD_COLOR)
        img1 = cv2.resize(img, (0, 0), fx=512 / img.shape[0], fy=512 / img.shape[1], interpolation=cv2.INTER_LINEAR)

        # image show
        cv2.imshow("Display window", img1)
        key = cv2.waitKey(0)


if __name__ == '__main__':
    main()