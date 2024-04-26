import cv2
import numpy as np

# Load the image
img = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Prewitt operator for edge detection
prewitt_kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

prewitt_x = cv2.filter2D(gray_img, -1, prewitt_kernel_x)
prewitt_y = cv2.filter2D(gray_img, -1, prewitt_kernel_y)

# Combine the x and y gradients
abs_prewitt_x = np.absolute(prewitt_x)
abs_prewitt_y = np.absolute(prewitt_y)
prewitt_combined = cv2.addWeighted(abs_prewitt_x, 0.5, abs_prewitt_y, 0.5, 0)

# Threshold the combined image to obtain edges
thresh = 50
edges = cv2.threshold(prewitt_combined, thresh, 255, cv2.THRESH_BINARY)[1]

# Display and save the segmented image
cv2.imshow('Segmented Image', edges)
cv2.imwrite('segmented_image.jpg', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
