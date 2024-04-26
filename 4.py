import cv2
import numpy as np

# Load the image
img = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator for edge detection
sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)

# Combine the x and y gradients
abs_sobel_x = np.absolute(sobel_x)
abs_sobel_y = np.absolute(sobel_y)
sobel_combined = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

# Threshold the combined image to obtain edges
thresh = 50
edges = cv2.threshold(sobel_combined, thresh, 255, cv2.THRESH_BINARY)[1]

# Display and save the segmented image
cv2.imshow('Segmented Image', edges)
cv2.imwrite('segmented_image.jpg', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
