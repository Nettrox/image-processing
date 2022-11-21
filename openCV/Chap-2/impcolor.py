import cv2
import numpy as np

img = cv2.imread("yol.png")

kernel = np.ones((4,4),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(101,101),0)
imgCanny = cv2.Canny(img,100,100)
imgCanny00 = cv2.Canny(img,700,10)
imgDialation = cv2.dilate(imgCanny00, kernel)

cv2.imshow("gray image", imgGray)
cv2.imshow("blur image", imgBlur)
cv2.imshow("canny image", imgCanny)
cv2.imshow("canny image00", imgCanny00)
cv2.imshow("dialation image", imgDialation)
cv2.waitKey(0)