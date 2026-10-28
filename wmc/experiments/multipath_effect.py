import numpy as np
import matplotlib.pyplot as plt
#time and transmitted signal
t=np.linspace(0,1,1000)
tx=np.sin(2*np.pi*10*t)
#multipath signals: amplitude and delay
path1=tx
path2=0.6*np.roll(tx, 50)
path3=0.3*np.roll(tx,100)
#received signal
rx=path1+path2+path3
#plot
plt.plot(t,tx,label="Transmitted")
plt.plot(t,rx,label="Received")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Multipath Effect Simulation")
plt.legend()
plt.grid()
plt.show()
