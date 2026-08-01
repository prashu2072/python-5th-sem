import cv2
import numpy as np

# Create a white canvas
img = np.ones((500, 500, 3), dtype=np.uint8) * 255
temp_img = img.copy()

drawing = False
start_point = (-1, -1)

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global drawing, start_point, img, temp_img

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    # Mouse is moving while button is pressed
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = img.copy()
            cv2.rectangle(temp_img, start_point, (x, y), (255, 0, 0), 2)

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, start_point, (x, y), (255, 0, 0), 2)
        temp_img = img.copy()

# Create window
cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

while True:
    cv2.imshow("Draw Rectangle", temp_img)

    key = cv2.waitKey(1) & 0xFF

    # Press 'r' to reset
    if key == ord('r'):
        img = np.ones((500, 500, 3), dtype=np.uint8) * 255
        temp_img = img.copy()

    # Press 'q' to quit
    elif key == ord('q'):
        break

cv2.destroyAllWindows()