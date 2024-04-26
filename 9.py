import cv2

# Load the image
img = cv2.imread('input_image.jpg')

# Scaling by factor 2
scaled_up = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Scaling by factor 0.5
scaled_down = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# Display and save the scaled images
cv2.imshow('Scaled Up Image', scaled_up)
cv2.imshow('Scaled Down Image', scaled_down)
cv2.imwrite('scaled_up_image.jpg', scaled_up)
cv2.imwrite('scaled_down_image.jpg', scaled_down)

cv2.waitKey(0)
cv2.destroyAllWindows()
