import numpy as np
import cv2 as cv


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global counter
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), 50, (0, 255, 0), -1)
        counter += 1
        cv.putText(img, "numer "+str(counter), (x-65, y-55), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255))
    elif event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x-50, y-25), (x+50, y+25), (255, 0, 0), -1)
        counter += 1
        cv.putText(img, "numer " + str(counter), (x - 65, y - 35), cv.FONT_HERSHEY_SIMPLEX, fontScale=1,
                   color=(0, 0, 255))


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
counter = 0
cv.setMouseCallback('image', draw_circle)


while True:
    cv.imshow('image', img)
    key = cv.waitKey(20)
    # ESCAPE
    if key == 27:
        break


cv.destroyAllWindows()
