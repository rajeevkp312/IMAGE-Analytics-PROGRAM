import cv2

img = cv2.imread("C://Users//ASUS//OneDrive//Desktop//avni.jpg", 0)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
perimeter = cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, 0.01 * perimeter, True)

print("Perimeter:", perimeter)
print("Approximated vertices count:", len(approx))
