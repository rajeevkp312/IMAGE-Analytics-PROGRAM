
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", cv2.IMREAD_GRAYSCALE)
# hist = cv2.calcHist([img], [0], None, [256], [0,256])
# blur = cv2.GaussianBlur(img, (5,5), 0)

# plt.figure(figsize=(10,4))
# plt.subplot(1,2,1)
# plt.plot(hist, color='black')
# plt.title('Histogram')
# plt.xlim([0,256])
# plt.subplot(1,2,2)
# plt.imshow(blur, cmap='gray')
# plt.title('Gaussian Blur')
# plt.axis('off')
# plt.tight_layout()
# plt.show()


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1), plt.hist(img.ravel(), 256, [0, 256]), plt.title('Histogram')
plt.subplot(1, 2, 2), plt.imshow(cv2.GaussianBlur(img, (5, 5), 0), cmap='gray'), plt.title('Gaussian Blur')
plt.tight_layout(), plt.show()

