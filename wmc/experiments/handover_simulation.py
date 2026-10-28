import numpy as np
import matplotlib.pyplot as plt
#position of mobile
x=np.linspace(0,100,101)
#base station positions
BS1=0
BS2=100
#simple signal strength model
signal_BS1=-50-0.5*x
signal_BS2=-100+0.5*x
#handover point
handover_point=50
#plot
plt.figure(figsize=(8,5))
plt.plot(x, signal_BS1, label="BS1 Signal")
plt.plot(x, signal_BS2, label="BS2 Signal")
plt.axvline(handover_point, linestyle="--", label="Handover point")
plt.scatter(handover_point, -75, s=80)
plt.xlabel("Mobile Position(m)")
plt.ylabel("Signal Strength(dBm)")
plt.grid(True)
plt.legend()
plt.show()
print("Mobile starts connected to BS1")
print("Mobile moves from BS1 towards BS2")
print("Signal from BS1 decreases")
print("Signal from BS2 increases")
print("Handover occurs at approximately 50 m")
print("Mobile is now connected to BS2")
