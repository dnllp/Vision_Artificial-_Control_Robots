import cv2
import sys
url = "https://192.168.1.106:8080/shot.jpg"

cap = cv2.VideoCapture(url)
if cap.isOpened():
    print("IpCam iniciada")
else:
    sys.exit("IpCam desconectada")
while True:
    cap.open(url)
    ret, frame = cap.read()
    if ret:
        cv2.imshow('img',frame)
    else:
        print("IpCam desconectada")
        break
    if (cv2.waitKey(1) & 0xff == 27):
        break
