import numpy as np
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.segmentation import active_contour

img = io.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg")
img_gray = color.rgb2gray(img)

s = np.linspace(0, 2*np.pi, 400)
r = 100 + 80*np.sin(s)
c = 220 + 80*np.cos(s)
init = np.array([r, c]).T

snake = active_contour(img_gray, init, alpha=0.015, beta=10, gamma=0.001)

plt.figure(figsize=(8,8))
plt.imshow(img_gray, cmap='gray')
plt.plot(init[:, 1], init[:, 0], '--r', label='Initial contour')
plt.plot(snake[:, 1], snake[:, 0], '-b', label='Active contour')
plt.legend()
plt.title('Active Contour Segmentation')
plt.axis('off')
plt.show()
