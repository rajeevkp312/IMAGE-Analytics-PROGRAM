import cv2
from skimage.feature import graycomatrix, graycoprops
import numpy as np

# Load image and threshold
img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Hu Moments
hu_moments = cv2.HuMoments(cv2.moments(thresh)).flatten()
print("Hu Moments:", hu_moments)

# GLCM Contrast & Homogeneity
glcm = graycomatrix((img // 8).astype(np.uint8), distances=[1], angles=[0], levels=32, symmetric=True, normed=True)
print("GLCM Contrast:", graycoprops(glcm, 'contrast')[0, 0])
print("GLCM Homogeneity:", graycoprops(glcm, 'homogeneity')[0, 0])
