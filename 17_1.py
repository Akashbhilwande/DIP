import cv2
import numpy as np

# Load the grayscale image
gray_img = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Set the intensity range to highlight (you can adjust these values as needed)
low_intensity = 50
high_intensity = 200

# Create a mask to preserve the background within the intensity range
background_mask = cv2.inRange(gray_img, low_intensity, high_intensity)

# Highlight the intensity range in the image while preserving the background
highlighted_img_preserve_bg = cv2.bitwise_and(gray_img, gray_img, mask=background_mask)

# Display and save the image with preserved background
cv2.imshow('Image with Preserved Background', highlighted_img_preserve_bg)
cv2.imwrite('highlighted_image_preserve_bg.jpg', highlighted_img_preserve_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()
