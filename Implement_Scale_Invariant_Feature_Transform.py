import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", 0)
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(img, None)

img_kp = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img_kp, cmap='gray')
plt.title(f'SIFT: {len(keypoints)} Keypoints')
plt.axis('off')
plt.show()
