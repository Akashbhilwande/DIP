import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Compute the negative of the image
neg_img = 255 - img

# Display and save the negative image
cv2.imshow('Negative Image', neg_img)
cv2.imwrite('negative_image.jpg', neg_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
