import cv2
from tkinter import *
from PIL import Image, ImageTk
import sys

def onClosing():
    ventana.quit()
    cap.release()
    print("Camara desconectada")
    ventana.destroy()
    

def callback():
    cap.open(url)
    ret, frame = cap.read()
    if ret:
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img.thumbnail((400,400))
        tkimage = ImageTk.PhotoImage(img)
        label.configure(image = tkimage)
        label.image = tkimage
        ventana.after(1,callback)

url = "https://192.168.1.106:8080/shot.jpg"
cap = cv2.VideoCapture(url)   


if cap.isOpened():
    print("IpCam iniciada")
else: 
    sys.exit("ipCam desconectada")

ventana = Tk()
ventana.protocol("WM_DELETE_WINDOW",onClosing)
ventana.title("Visión Artifical")
label = Label(ventana)
label.grid(row = 0)
ventana.after(1,callback)
ventana.mainloop()