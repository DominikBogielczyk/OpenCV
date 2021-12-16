import cv2 as cv

def main():
    cap = cv.VideoCapture("lama.mp4")  # open video

    key = ord('a')

    while key != ord('q'):
        # Capture frame-by-frame

        ret, frame = cap.read()

        if ret != False:
            img = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

        else:
            print('End of video')
            cap.set(cv.CAP_PROP_POS_FRAMES, 0)

        # Display the resulting frame
        cv.imshow('Funny lama', img)

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