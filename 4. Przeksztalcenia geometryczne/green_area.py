import cv2 as cv


# mouse callback function
def draw_circle(event, x, y, flags, param):
    # rectangle 2 points choose
    if event == cv.EVENT_LBUTTONDOWN:
        x_points.append(x)
        y_points.append(y)

    # output image calculations and display
    if len(x_points) == 2:
        image_out = img.copy()
        x1 = min(x_points[-2:])
        x2 = max(x_points[-2:])
        y1 = min(y_points[-2:])
        y2 = max(y_points[-2:])
        image_out[y1:y2, x1:x2, 0] = 0
        image_out[y1:y2, x1:x2, 2] = 0
        cv.imshow('output', image_out)

    # update area at input image
    if event == cv.EVENT_MOUSEMOVE:
        if len(x_points) in range(1, 2):
            img_copy = img.copy()
            cv.rectangle(img_copy, (x_points[-1], y_points[-1]), (x, y), (0, 255, 0), 3)
            cv.imshow('image', img_copy)


# Create a black image, a window and bind the function to window
img = cv.imread("../images/funny_image.png", cv.IMREAD_REDUCED_COLOR_4)
cv.imshow('image', img)
x_points = []
y_points = []
cv.setMouseCallback('image', draw_circle)

while True:
    key = cv.waitKey(20)
    # ESCAPE
    if key == 27:
        break


cv.destroyAllWindows()
