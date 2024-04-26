import cv2
import numpy as np

# Load the grayscale image
gray_img = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Set the intensity range to highlight (you can adjust these values as needed)
low_intensity = 50
high_intensity = 200

# Create a mask to highlight the intensity range without preserving the background
foreground_mask = cv2.inRange(gray_img, low_intensity, high_intensity)

# Invert the mask to obtain the foreground
background_mask = cv2.bitwise_not(foreground_mask)

# Highlight the intensity range in the image without preserving the background
highlighted_img_no_preserve_bg = cv2.bitwise_and(gray_img, gray_img, mask=foreground_mask)

# Display and save the image without preserving the background
cv2.imshow('Image without Preserved Background', highlighted_img_no_preserve_bg)
cv2.imwrite('highlighted_image_no_preserve_bg.jpg', highlighted_img_no_preserve_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()
