import matplotlib.pyplot as plt
import numpy as np
import serial
import time


t = np.arange(0,10,0.1)
x = np.zeros(100) 
y = np.zeros(100)
z = np.zeros(100)  
tilt = np.zeros(100)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
for i in range(300):
    line=s.readline()
    #print (line)
    if(i%3 == 0): x[int(i/3)] = float(line)
    elif(i%3 == 1): y[int(i/3)] = float(line)
    elif(i%3 == 2): z[int(i/3)] = float(line)
    org = [x[0],y[0],z[0]]
   

for i in range(100):
    now = [x[i],y[i],z[i]]
    angle = np.dot(org,now)
    angle = angle/((np.square(abs(org[0]))+np.square(abs(org[0]))+np.square(abs(org[2])))*np.sqrt(np.square(abs(x[i]))+np.square(abs(y[i]))+np.square(abs(z[i]))))
    if angle > np.sqrt(2)/2:   tilt[i] = 0
    else:   tilt[i] = 1

fig, ax = plt.subplots(2, 1)

ax[0].plot(t,x, label = 'x')
ax[0].plot(t,y, label = 'y')
ax[0].plot(t,z, label = 'z')
ax[0].set_xlabel('t')
ax[0].set_ylabel('vector')
ax[0].legend()

ax[1].stem(t,tilt) 
ax[1].set_xlabel('time')
ax[1].set_ylabel('tilt')

plt.show()

s.close()