import cv2

# Load the grayscale image
gray_img = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Set the threshold value (you can adjust this value as needed)
threshold_value = 127

# Apply thresholding
_, binary_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)

# Display and save the binary image
cv2.imshow('Binary Image', binary_img)
cv2.imwrite('binary_image.jpg', binary_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
