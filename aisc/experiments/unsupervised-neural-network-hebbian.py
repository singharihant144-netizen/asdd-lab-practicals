import numpy as np

X = np.array([[1, -2], [0, 1], [2, 3], [1, -1]])
weights = np.array([1.0, -1.0])
learning_rate = 1

for x in X:
    output = np.dot(weights, x)
    weights = weights + learning_rate * output * x

print("Final Weights:", weights)
