import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import reconstruction

img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", 0)
seed = np.copy(img)
seed[1:-1, 1:-1] = img.max()
mask = img

reconstructed = reconstruction(seed, mask, method='erosion')

plt.figure(figsize=(8,4))
plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title('Original'), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(reconstructed, cmap='gray'), plt.title('Reconstruction'), plt.axis('off')
plt.tight_layout()
plt.show()
