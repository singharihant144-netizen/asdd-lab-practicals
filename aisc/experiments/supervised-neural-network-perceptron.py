import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 0, 0, 1])

weights = np.zeros(2)
bias = 0
learning_rate = 0.1
epochs = 20

def activation(net):
    return 1 if net > 0 else 0

for epoch in range(epochs):
    for i in range(len(X)):
        net = np.dot(X[i], weights) + bias
        output = activation(net)
        error = y[i] - output
        weights += learning_rate * error * X[i]
        bias += learning_rate * error

print("Final Weights:", weights)
print("Final Bias:", bias)
print("\nPerceptron Output:")

for i in range(len(X)):
    net = np.dot(X[i], weights) + bias
    output = activation(net)
    print(X[i], "=", output)
