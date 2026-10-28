import numpy as np
import matplotlib.pyplot as plt
N=1000
bits=np.random.randint(0,2,N)
bpsk_signal=2*bits-1
SNR_dB=5
SNR=10**(SNR_dB/10)
noise_variance=1/(2*SNR)
noise=np.sqrt(noise_variance)*np.random.randn(N)
received_signal=bpsk_signal+noise
received_bits=(received_signal>0).astype(int)
errors=np.sum(bits!=received_bits)
BER=errors/N

print("Number of errors:",errors)
print("Bit Error Rate (BER):",BER)
plt.figure(figsize=(10,3))
plt.stem(bits[:20])
plt.title("Original Bits")
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,3))
plt.plot(bpsk_signal[:50],marker='o')
plt.title("BPSK Modulated Signal")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,3))
plt.plot(received_signal[:50],marker='o')
plt.title("Received Signal with AWGN")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
