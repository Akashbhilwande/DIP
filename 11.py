import cv2

# Load the image
img = cv2.imread('input_image.jpg')

# Get the height and width of the image
height, width = img.shape[:2]

# Define the rotation angle (clockwise and anti-clockwise)
angle_clockwise = 90
angle_anticlockwise = -90

# Compute the rotation matrices
rotation_matrix_clockwise = cv2.getRotationMatrix2D((width / 2, height / 2), angle_clockwise, 1)
rotation_matrix_anticlockwise = cv2.getRotationMatrix2D((width / 2, height / 2), angle_anticlockwise, 1)

# Apply the rotation to the image
rotated_img_clockwise = cv2.warpAffine(img, rotation_matrix_clockwise, (width, height))
rotated_img_anticlockwise = cv2.warpAffine(img, rotation_matrix_anticlockwise, (width, height))

# Display and save the rotated images
cv2.imshow('Rotated Clockwise Image', rotated_img_clockwise)
cv2.imwrite('rotated_clockwise_image.jpg', rotated_img_clockwise)

cv2.imshow('Rotated Anti-clockwise Image', rotated_img_anticlockwise)
cv2.imwrite('rotated_anticlockwise_image.jpg', rotated_img_anticlockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()
