#gauss suicidal

import numpy as np
from scipy.linalg import solve
import collections

def gauss(A, b, x):
    L = np.tril(A)
    U = A - L
    x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    print(x)
    return x            

def gausssidel(A,b):
    cont = 0
    x = [1, 1, 1]
    while(True):
        old = x
        x = gauss(A,b,x)
        cont = cont + 1
        if np.allclose(x,old):
            return x

A = np.array([[1.0, 0.0, -1.0], [-0.5, 1.0, -0.25], [1.0, -0.5, 1.0]])
b = [0.2, -1.425, 2.0]

val = gausssidel(A,b)
print(val)

