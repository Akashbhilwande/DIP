import cv2

# Load the noisy 24-bit RGB image
noisy_img = cv2.imread('noisy_image.jpg')

# Apply Gaussian blur to smoothen the image (adjust kernel size as needed)
smooth_img = cv2.GaussianBlur(noisy_img, (5, 5), 0)

# Display and save the smooth image
cv2.imshow('Smooth Image', smooth_img)
cv2.imwrite('smooth_image.jpg', smooth_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
