import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('C://Users//ASUS//OneDrive//Desktop//avni.jpg', 0)  # Grayscale for intensity transforms
color_img = cv2.imread('C://Users//ASUS//OneDrive//Desktop//avni.jpg')
color_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

# 1. Intensity Transformations
negative = 255 - img
log_trans = np.uint8(30 * np.log1p(img))
gamma = np.uint8(255 * (img/255)**0.5)

# 2. Histograms
plt.figure(figsize=(15, 10))

# Plot transformations
plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(232), plt.imshow(negative, cmap='gray'), plt.title('Negative')
plt.subplot(233), plt.imshow(log_trans, cmap='gray'), plt.title('Log Transform')
plt.subplot(234), plt.imshow(gamma, cmap='gray'), plt.title('Gamma (0.5)')

# Plot histograms
plt.subplot(235), plt.hist(img.ravel(), 256, [0,256]), plt.title('Histogram')
plt.subplot(236), plt.hist(log_trans.ravel(), 256, [0,256]), plt.title('Log Transform Hist')

plt.tight_layout()
plt.show()

# 3. Color Image Processing
# Smoothing (Averaging Filter)
blur = cv2.blur(color_img, (5,5))

# Sharpening (Laplacian)
kernel = np.array([[0, -1, 0], 
                   [-1, 5, -1],
                   [0, -1, 0]])
sharp = cv2.filter2D(color_img, -1, kernel)

# Display results
plt.figure(figsize=(12, 4))
plt.subplot(131), plt.imshow(color_img), plt.title('Original')
plt.subplot(132), plt.imshow(blur), plt.title('Smoothed')
plt.subplot(133), plt.imshow(sharp), plt.title('Sharpened')
plt.tight_layout()
plt.show()