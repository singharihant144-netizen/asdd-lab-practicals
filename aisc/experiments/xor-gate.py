import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(1)
W1 = np.random.randn(2, 4)
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 1)
b2 = np.zeros((1, 1))
lr = 0.5

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

for epoch in range(20000):
    h = sigmoid(X @ W1 + b1)
    o = sigmoid(h @ W2 + b2)
    error = o - y
    d2 = error * o * (1 - o)
    d1 = (d2 @ W2.T) * h * (1 - h)
    W2 -= lr * h.T @ d2 / 4
    b2 -= lr * np.mean(d2, axis=0, keepdims=True)
    W1 -= lr * X.T @ d1 / 4
    b1 -= lr * np.mean(d1, axis=0, keepdims=True)

print("XOR Gate Output:")
for i in X:
    h = sigmoid(i.reshape(1, 2) @ W1 + b1)
    output = int(sigmoid(h @ W2 + b2)[0, 0] >= 0.5)
    print(i, "=", output)
