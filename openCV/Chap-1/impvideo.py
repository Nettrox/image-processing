import cv2
import numpy as np


cap =  cv2.VideoCapture("yol.mp4")
kernel = np.ones((8,8),np.uint8)


while True:
    success, img = cap.read()
    imgCanny = cv2.Canny(img,75,175)
    imgCanny00 = cv2.Canny(img,300,300)
    imgBlur = cv2.GaussianBlur(imgCanny,(7,7),0)
    imgDialation = cv2.dilate(imgCanny00, kernel)
    cv2.imshow("video", img)
    cv2.imshow("video canny", imgCanny)
    cv2.imshow("video canny 00", imgBlur)
    cv2.imshow("video dialation", imgDialation)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break