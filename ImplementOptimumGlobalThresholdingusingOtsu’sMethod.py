import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", 0)
val, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original'), plt.axis('off')
plt.subplot(1, 2, 2), plt.imshow(thresh, cmap='gray'), plt.title(f'Threshold = {int(val)}'), plt.axis('off')
plt.tight_layout()
plt.show()
