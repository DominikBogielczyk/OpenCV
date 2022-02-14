import cv2
import time

img = cv2.imread(cv2.samples.findFile("qr.jpg"), cv2.IMREAD_COLOR)
img1 = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LINEAR)
img2 = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_NEAREST)
img3 = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_AREA)
img4 = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LANCZOS4)


def main():
    while True:
        key_code = cv2.waitKey(10)
        if key_code == 27:
            # escape key pressed
            break
        t1 = time.perf_counter()
        cv2.imshow('INTER_LINEAR', img1)
        t2 = time.perf_counter()
        cv2.imshow('INTER_NEAREST', img2)
        t3 = time.perf_counter()
        cv2.imshow('INTER_AREA', img3)
        t4 = time.perf_counter()
        cv2.imshow('INTER_LACZNOS4', img4)
        t5 = time.perf_counter()

        print(f'INTER_LINEAR:  {(t2 - t1)*1000:.2f}ms, ', f'INTER_NEAREST:  {(t3 - t2)*1000:.2f}ms, ',
              f'INTER_AREA:  {(t4 - t3)*1000:.2f}ms, ', f'INTER_LACZNOS4:  {(t5 - t4)*1000:.2f}ms')


if __name__ == '__main__':
    main()