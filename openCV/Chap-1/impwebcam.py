import cv2

cap =  cv2.VideoCapture(0) #buradaki 0 default kamera hangisi ise onu açar
cap.set(3,640)
cap.set(4,480)
cap.set(10,100) 

while True:
    success, img = cap.read()
    cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xFF == ord("q"): #q kapatmak için
        break