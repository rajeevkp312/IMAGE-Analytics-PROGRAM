# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# img = cv2.cvtColor(cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg"), cv2.COLOR_BGR2RGB)
# blur = cv2.GaussianBlur(img, (7,7), 0)
# kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
# sharp = cv2.filter2D(img, -1, kernel)

# plt.figure(figsize=(12,4))
# plt.subplot(131), plt.imshow(img), plt.title('Original'), plt.axis('off')
# plt.subplot(132), plt.imshow(blur), plt.title('Smoothed'), plt.axis('off')
# plt.subplot(133), plt.imshow(sharp), plt.title('Sharpened'), plt.axis('off')
# plt.tight_layout(), plt.show()


import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load and convert the image to RGB
img = cv2.cvtColor(cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg"), cv2.COLOR_BGR2RGB)

# Apply Gaussian Blur for smoothing
blur = cv2.GaussianBlur(img, (7, 7), 0)

# Define sharpening kernel
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharp = cv2.filter2D(img, -1, kernel)

# Display results
plt.figure(figsize=(12, 4))
plt.subplot(131), plt.imshow(img), plt.title('Original'), plt.axis('off')
plt.subplot(132), plt.imshow(blur), plt.title('Smoothed'), plt.axis('off')
plt.subplot(133), plt.imshow(sharp), plt.title('Sharpened'), plt.axis('off')
plt.tight_layout()
plt.show()

