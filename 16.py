import cv2
import numpy as np

# Load the original image
original_img = cv2.imread('input_image.jpg')

# Convert the image to float32 for normalization
normalized_img = original_img.astype(np.float32) / 255.0

# Display and save the normalized image
cv2.imshow('Normalized Image', normalized_img)
cv2.imwrite('normalized_image.jpg', normalized_img * 255)

cv2.waitKey(0)
cv2.destroyAllWindows()
