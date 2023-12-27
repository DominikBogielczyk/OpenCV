import cv2
import time

# image read
img = cv2.imread("../images/qr.jpg", cv2.IMREAD_COLOR)
img1 = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LINEAR)
img2 = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_NEAREST)
img3 = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_AREA)
img4 = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LANCZOS4)


def main():
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

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
