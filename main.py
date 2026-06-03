import numpy as np
from Layer import input,weight,biais,biais_y,weight_y
from activation import relu,sigmoid

x = input()
w = weight()
b = biais()

wy = weight_y()
by = biais_y()

x2 = relu(np.dot(w,x)+b)

print(wy)

print(x2)

y = sigmoid(relu(np.dot(wy,x2)+by))

print(y)

