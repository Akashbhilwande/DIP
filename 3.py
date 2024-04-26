import cv2
import numpy as np

# Load the image
img = cv2.imread('input_image.jpg')

# Convert the image to float32 for CMY conversion
img_float32 = img.astype(np.float32) / 255.0

# Compute the CMY channels
C = 1 - img_float32[:, :, 2]  # Cyan
M = 1 - img_float32[:, :, 1]  # Magenta
Y = 1 - img_float32[:, :, 0]  # Yellow

# Merge the CMY channels into a single image
cmy_img = np.stack((C, M, Y), axis=2)

# Convert the CMY image back to uint8 for display and saving
cmy_img_uint8 = (cmy_img * 255).astype(np.uint8)

# Display and save the CMY image
cv2.imshow('CMY Image', cmy_img_uint8)
cv2.imwrite('cmy_image.jpg', cmy_img_uint8)

cv2.waitKey(0)
cv2.destroyAllWindows()
