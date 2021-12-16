import cv2 as cv

def main():
    cap = cv.VideoCapture(0)  # open the default camera

    key = ord('a')

    while key != ord('q'):
        # Capture frame-by-frame
        ret, frame = cap.read()

        img = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
        # Display the resulting frame
        cv.imshow('frame', img)

        # Wait for a space or 'q' press - new frame
        key  = cv.waitKey(0)

        while key != ord(' ') and key != ord('q'):
            pass

    # When everything done, release the capture
    cap.release()
    # and destroy created windows, so that they are not left for the rest of the program
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()