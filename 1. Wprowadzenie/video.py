import cv2 as cv
import os
import sys


def main():
    # current path
    path = os.getcwd()
    # to parent dir and then /video
    file = os.path.dirname(path) + "/video/Wildlife.mp4"
    cap = cv.VideoCapture(file)  # open video

    key = ord('a')

    while key != ord('q'):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            img = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
            if img is None:
                sys.exit("Could not read the image.")

        else:
            print('End of video')
            cap.set(cv.CAP_PROP_POS_FRAMES, 0)

        # Display the resulting frame
        cv.imshow('Wildlife video', img)

        # Wait for a key press, SPACE to open new frame, 'q' to quit
        key = cv.waitKey(0)

        while key != ord(' ') and key != ord('q'):
            pass

    # When everything done, release the capture
    cap.release()
    # and destroy created windows, so that they are not left for the rest of the program
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()