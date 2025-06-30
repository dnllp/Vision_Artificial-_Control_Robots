import cv2
import sys

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("Camara inicializada")
else:
    sys.exit("Camara desconectada")
while True:
    ret, frame = cap.read()
    if ret: 
        cv2.imshow('Visual',frame)
    else:
        print("Camara desconectada")
        break
    if(cv2.waitKey(1) & 0xff ==27):
        break
cap.release()
cv2.destroyAllWindows()