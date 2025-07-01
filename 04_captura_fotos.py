from tkinter import filedialog
from tkinter import *
import os
from PIL import Image, ImageTk
import cv2
import time
import numpy as np
import sys

def onClosing():
    ventana.quit()
    cap.release()
    print("Camara desconectada")
    ventana.destroy()
    
def folder():
    directorio = filedialog.askdirectory()
    if directorio !="":
        os.chdir(directorio)
    print(directorio)

def saveImg():
    cap.open(url)
    ret,frame = cap.read()
    if ret:
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        tkimage = ImageTk.PhotoImage(img)
        label1.configure(image = tkimage)
        label1.image = tkimage
        #success = cv2.imwrite(os.getcwd()+"/imagen"+str(numImagen.get())+".jpg",frame)
        save_path = os.path.join(os.getcwd(), "imagen" + str(numImagen.get()) + ".jpg")
        print(f"Attempting to save image to: {save_path}")
        success = cv2.imwrite(save_path, frame)
        if success:
            print("Image saved successfully!")
            numImagen.set(numImagen.get() + 1)
        else:
            print("Failed to save image using cv2.imwrite")
        
        #numImagen.set(numImagen.get()+1)
        
def callback():
    cap.open(url)
    ret,frame = cap.read()
    if ret:
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        tkimage = ImageTk.PhotoImage(img)
        label.configure(image = tkimage)
        label.image = tkimage
        ventana.after(1,callback)
    else:
        onClosing()
url = "http://192.168.1.106:8080/shot.jpg"
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("Camara iniciada")
else:
    sys.exit("Camara cerrada")
ventana = Tk()
ventana.protocol("WM_DELETE_WINDOW",onClosing)
ventana.title("Captura de foto")

numImagen = IntVar()
numImagen.set(0)

label=Label(ventana)
label.grid(row = 1,padx=10,pady=20)

label1 = Label(ventana)
label1.grid(row=1,column=1,padx=20,pady=20)

buttonDir = Button(ventana, text="Carpeta",command=folder)
buttonDir.grid(row=2,padx=20,pady=20)

buttonSave = Button(ventana,text="Guardar imagen",command=saveImg)
buttonSave.grid(row=2,column=1,padx=20,pady=20)

ventana.after(1,callback)
ventana.mainloop()

