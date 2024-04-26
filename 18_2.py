import cv2

# Load the two grayscale images
img1 = cv2.imread('input_image1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('input_image2.jpg', cv2.IMREAD_GRAYSCALE)

# Perform subtraction of the two images
result_subtraction = cv2.subtract(img1, img2)

# Display and save the result of subtraction
cv2.imshow('Result of Subtraction', result_subtraction)
cv2.imwrite('result_subtraction.jpg', result_subtraction)

cv2.waitKey(0)
cv2.destroyAllWindows()
