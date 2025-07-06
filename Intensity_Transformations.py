import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('C://Users//ASUS//OneDrive//Desktop//avni.jpg', 0)  # Grayscale

# Intensity Transformations
negative = 255 - img
log_trans = np.uint8(30 * np.log1p(img))
gamma = np.uint8(255 * (img/255)**0.5)

# Display transformations
plt.figure(figsize=(12, 4))
plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(132), plt.imshow(negative, cmap='gray'), plt.title('Negative')
plt.subplot(133), plt.imshow(gamma, cmap='gray'), plt.title('Gamma (0.5)')
plt.tight_layout()
plt.show()