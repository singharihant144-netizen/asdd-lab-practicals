import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 0, 0, 1])

weights = np.zeros(2)
bias = 0
learning_rate = 0.1

def activation(x):
    return 1 if x >= 0 else 0

for epoch in range(20):
    for i in range(len(X)):
        net = np.dot(X[i], weights) + bias
        output = activation(net)
        error = y[i] - output
        weights += learning_rate * error * X[i]
        bias += learning_rate * error

print("Trained Weights:", weights)
print("Trained Bias:", bias)
print("AND Gate Output:")

for i in X:
    net = np.dot(i, weights) + bias
    print(i, "=", activation(net))
