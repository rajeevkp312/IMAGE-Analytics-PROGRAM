import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

dilate = cv2.dilate(img, kernel)
erode = cv2.erode(img, kernel)
open_ = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.figure(figsize=(12,6))
titles = ['Original', 'Dilate', 'Erode', 'Open', 'Close']
images = [img, dilate, erode, open_, close]

for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
