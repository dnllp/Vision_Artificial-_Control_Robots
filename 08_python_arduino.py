from pyArduino import *
import matplotlib.pyplot as plt
import numpy as np
import time

ts = 0.1
tf = 20
t = np.arange(0,tf+ts,ts)
N = len(t)

port = 'COM18'
baudRate = 9600
sizeData = 2

senData1 = np.sin(0.8*t)
senData2 = np.cos(0.6*t)

receiveData1 = np.zeros(N)
receiveData2 = np.zeros(N)

arduino = serialArduino(port,baudRate,sizeData)
arduino.readSerialStart()


for k in range(N):
    start_time = time.time()
    arduino.sendData([round(senData1[k],3),round(senData2[k],3)])
    
    receiveData1[k] = arduino.rawData[0]
    receiveData2[k] = arduino.rawData[1]
    
    elapsed_time = time.time() - start_time
    
    time.sleep(ts-elapsed_time)
arduino.close()

plt.figure()
plt.plot(t,senData1,label="Dato enviado 1")
plt.plot(t,receiveData1,label ="Dato recibido 1 ")

plt.figure()
plt.plot(t,senData2,label="Dato enviado 2")
plt.plot(t,receiveData2,label ="Dato recibido 2 ")

plt.legend(loc='upper left')
plt.show()
