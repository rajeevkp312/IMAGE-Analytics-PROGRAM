import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur = cv2.GaussianBlur(img_rgb, (7,7), 0)
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
sharp = cv2.filter2D(img_rgb, -1, kernel)

plt.figure(figsize=(12,4))
plt.subplot(1,3,1), plt.imshow(img_rgb), plt.title('Original'), plt.axis('off')
plt.subplot(1,3,2), plt.imshow(blur), plt.title('Smoothed'), plt.axis('off')
plt.subplot(1,3,3), plt.imshow(sharp), plt.title('Sharpened'), plt.axis('off')
plt.tight_layout()
plt.show()
