import cv2
import numpy as np

# Load the original image
original_img = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

# Apply DCT transformation
dct_img = cv2.dct(np.float32(gray_img))

# Apply inverse DCT transformation
idct_img = cv2.idct(dct_img)

# Convert the IDCT image back to uint8
idct_img = np.uint8(idct_img)

# Calculate the PSNR value between the original and IDCT images
psnr_value = cv2.PSNR(gray_img, idct_img)

# Display the original and IDCT images
cv2.imshow('Original Image', gray_img)
cv2.imshow('IDCT Image', idct_img)

print(f"PSNR value: {psnr_value} dB")

cv2.waitKey(0)
cv2.destroyAllWindows()
