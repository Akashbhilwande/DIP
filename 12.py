import cv2
import numpy as np

# Load the original image
original_img = cv2.imread('input_image.jpg')

# Define the compression quality (0-100, higher is better quality but larger file size)
compression_quality = 90

# Encode the image using JPEG compression
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), compression_quality]
result, encoded_img = cv2.imencode('.jpg', original_img, encode_param)

# Decode the compressed image
decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

# Calculate the PSNR value between the original and decompressed images
psnr_value = cv2.PSNR(original_img, decoded_img)

# Display the original and decompressed images
cv2.imshow('Original Image', original_img)
cv2.imshow('Decompressed Image', decoded_img)

print(f"PSNR value: {psnr_value} dB")

cv2.waitKey(0)
cv2.destroyAllWindows()
