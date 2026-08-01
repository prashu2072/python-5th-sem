import cv2
import numpy as np

# Create a blank color image (300x400)
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Different color bands
img[0:50, :] = (0, 0, 0)          # Black
img[50:100, :] = (200, 255, 255)  # White
img[100:150, :] = (0, 165, 255)   # Orange
img[150:200, :] = (128, 0, 128)   # Purple
img[200:250, :] = (42, 42, 165)   # Brown
img[250:300, :] = (203, 192, 255) # Pink

# Display the image
cv2.imshow("Different Colors", img)

cv2.waitKey(0)
cv2.destroyAllWindows()