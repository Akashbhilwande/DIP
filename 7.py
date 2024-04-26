import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('input_image.jpg')

# Split the image into RGB channels
r_hist = cv2.calcHist([img], [2], None, [256], [0, 256])
g_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
b_hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot the histograms
plt.figure(figsize=(8, 6))
plt.plot(r_hist, color='red', label='Red')
plt.plot(g_hist, color='green', label='Green')
plt.plot(b_hist, color='blue', label='Blue')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('RGB Histogram')
plt.legend()
plt.grid()
plt.show()
