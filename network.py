import numpy as np

def relu(x):
    return np.maximum(0,x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([1,2,3])

w = np.array([
    [1,-4,0.4],
    [2,0.5,9]

])

Wout = np.array([
    [2, 0.5]
])

bw1 = np.array([2,4])

bwout = np.array([-4])

z = np.dot(w,x)+bw1

f = relu(z)

y = np.dot(Wout , f)+bwout

print(sigmoid(y))