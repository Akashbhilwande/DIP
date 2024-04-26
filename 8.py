import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform histogram equalization
equalized_img = cv2.equalizeHist(gray_img)

# Compute and plot the histograms
hist_gray = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([equalized_img], [0], None, [256], [0, 256])

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')

plt.figure(figsize=(8, 6))
plt.plot(hist_gray, color='blue', label='Original Histogram')
plt.plot(hist_equalized, color='red', label='Equalized Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Histograms')
plt.legend()
plt.grid()
plt.show()
