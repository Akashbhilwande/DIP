import cv2

# Load the image
img = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_img, threshold1=100, threshold2=200)

# Display and save the segmented image
cv2.imshow('Segmented Image', edges)
cv2.imwrite('segmented_image_canny.jpg', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
