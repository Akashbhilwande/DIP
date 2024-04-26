import cv2

# Load the two grayscale images
img1 = cv2.imread('input_image1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('input_image2.jpg', cv2.IMREAD_GRAYSCALE)

# Perform addition of the two images
result_addition = cv2.add(img1, img2)

# Display and save the result of addition
cv2.imshow('Result of Addition', result_addition)
cv2.imwrite('result_addition.jpg', result_addition)

cv2.waitKey(0)
cv2.destroyAllWindows()
