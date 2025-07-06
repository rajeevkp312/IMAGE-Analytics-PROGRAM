import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", 0)

# Create an elliptical structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))

# Perform morphological operations
gray_dilate = cv2.dilate(img, kernel)
gray_erode = cv2.erode(img, kernel)

# Plot the results
plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original'), plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(gray_dilate, cmap='gray'), plt.title('Grayscale Dilate'), plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(gray_erode, cmap='gray'), plt.title('Grayscale Erode'), plt.axis('off')
plt.tight_layout()
plt.show()
