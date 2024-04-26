import cv2
import numpy as np

# Load the image
img = cv2.imread('input_image.jpg')

# Define the translation matrix for shifting right by 20 units and downwards by 10 units
tx = 20
ty = 10
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the translation to the image
translated_img = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))

# Display and save the translated images
cv2.imshow('Shifted Right Image', translated_img)
cv2.imwrite('shifted_right_image.jpg', translated_img)

# Reset the translation matrix for downwards shift
translation_matrix_downwards = np.float32([[1, 0, 0], [0, 1, ty]])

# Apply the downwards translation to the image
translated_img_downwards = cv2.warpAffine(img, translation_matrix_downwards, (img.shape[1], img.shape[0]))

# Display and save the translated images
cv2.imshow('Shifted Downwards Image', translated_img_downwards)
cv2.imwrite('shifted_downwards_image.jpg', translated_img_downwards)

cv2.waitKey(0)
cv2.destroyAllWindows()
