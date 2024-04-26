import cv2
import numpy as np

# Load the 24-bit RGB image
rgb_img = cv2.imread('input_image.jpg')

# Split the image into individual channels (BGR order)
b, g, r = cv2.split(rgb_img)

# Define the enhancement factor and the color channel to enhance (e.g., red channel)
enhancement_factor = 1.5  # You can adjust this factor as needed
channel_to_enhance = r  # Choose the channel to enhance (r, g, or b)

# Apply enhancement by multiplying the chosen channel with the enhancement factor
enhanced_channel = np.clip(channel_to_enhance * enhancement_factor, 0, 255).astype(np.uint8)

# Merge the enhanced channel back with the original image
enhanced_rgb_img = cv2.merge([b, g, enhanced_channel])

# Display and save the enhanced image
cv2.imshow('Enhanced RGB Image', enhanced_rgb_img)
cv2.imwrite('enhanced_image.jpg', enhanced_rgb_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
