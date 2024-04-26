#pip install PyWavelets


import cv2
import pywt
import numpy as np

# Load the original image
original_img = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

# Apply DWT transformation
coeffs = pywt.dwt2(gray_img, 'haar')

# Extract the approximation coefficients (low frequency) and detail coefficients (high frequency)
cA, (cH, cV, cD) = coeffs

# Apply inverse DWT transformation
idwt_img = pywt.idwt2((cA, (cH, cV, cD)), 'haar')

# Convert the IDWT image back to uint8
idwt_img = np.uint8(idwt_img)

# Calculate the PSNR value between the original and IDWT images
psnr_value = cv2.PSNR(gray_img, idwt_img)

# Display the original and IDWT images
cv2.imshow('Original Image', gray_img)
cv2.imshow('IDWT Image', idwt_img)

print(f"PSNR value: {psnr_value} dB")

cv2.waitKey(0)
cv2.destroyAllWindows()



#OR 

# import cv2
# import numpy as np

# def haar_transform(image):
#     h, w = image.shape
#     transformed_image = np.zeros((h, w), dtype=np.float32)

#     for i in range(0, h, 2):
#         for j in range(0, w, 2):
#             avg = (image[i, j] + image[i, j + 1] + image[i + 1, j] + image[i + 1, j + 1]) / 4
#             diff1 = image[i, j] - avg
#             diff2 = image[i, j + 1] - avg
#             diff3 = image[i + 1, j] - avg
#             diff4 = image[i + 1, j + 1] - avg

#             transformed_image[i // 2, j // 2] = avg
#             transformed_image[i // 2, w // 2 + j // 2] = diff1
#             transformed_image[h // 2 + i // 2, j // 2] = diff2
#             transformed_image[h // 2 + i // 2, w // 2 + j // 2] = diff3

#     return transformed_image

# def inverse_haar_transform(transformed_image):
#     h, w = transformed_image.shape
#     image = np.zeros((2 * h, 2 * w), dtype=np.float32)

#     for i in range(0, h):
#         for j in range(0, w):
#             avg = transformed_image[i, j]
#             diff1 = transformed_image[i, w + j]
#             diff2 = transformed_image[h + i, j]
#             diff3 = transformed_image[h + i, w + j]

#             image[2 * i, 2 * j] = avg + diff1 + diff2 + diff3
#             image[2 * i, 2 * j + 1] = avg + diff1 - diff2 - diff3
#             image[2 * i + 1, 2 * j] = avg - diff1 + diff2 - diff3
#             image[2 * i + 1, 2 * j + 1] = avg - diff1 - diff2 + diff3

#     return image

# # Load the original image
# original_img = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# # Apply DWT transformation
# dwt_img = haar_transform(original_img)

# # Apply inverse DWT transformation
# idwt_img = inverse_haar_transform(dwt_img)

# # Convert the IDWT image back to uint8
# idwt_img = np.uint8(idwt_img)

# # Calculate the PSNR value between the original and IDWT images
# psnr_value = cv2.PSNR(original_img, idwt_img)

# # Display the original and IDWT images
# cv2.imshow('Original Image', original_img)
# cv2.imshow('IDWT Image', idwt_img)

# print(f"PSNR value: {psnr_value} dB")

# cv2.waitKey(0)
# cv2.destroyAllWindows()
