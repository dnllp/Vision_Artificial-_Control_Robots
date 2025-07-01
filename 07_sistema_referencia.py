import cv2
import sys

def getPosicion(event,x,y,flags,param):
    global coordenadas 
    
    if event == cv2.EVENT_LBUTTONDOWN:
        coordenadas = [(x,y)]
        print(coordenadas)
        
        ##Camara en mano
        #xrobot = frame.shape[1]/2 - x
        #yrobot = frame.shape[0]/2 - y
        
        ##camara fija
        xrobot = x - frame.shape[1]/2
        yrobot = frame.shape[0]/2 - y
        
        print(f"xrobot = {xrobot}")
        print(f"yrobot = {yrobot}")
        
coordenadas = []
url = "http://192.168.1.106:8080/shot.jpg"
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("Camara iniciada")
else:
    print("Camara desconectada")
    sys.exit(1)

winName = "IP_CAM"
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback(winName,getPosicion)

while True:
    cap.open(url)
    ret, frame = cap.read()
    if ret:
        cv2.circle(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)),20,(0,0,255),3)
        cv2.imshow(winName,frame)
    else:
        print("Camara desconectada")
        break
    if(cv2.waitKey(10) & 0xff ==27):
        break
cap.release()
cv2.destroyAllWindows()
