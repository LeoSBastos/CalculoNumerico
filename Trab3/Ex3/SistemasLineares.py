import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg


vet = [[1,1],[2,8],[3,27]]

def criarMatrizX(vet):
    aux = []
    for i in range(len(vet)):
        aux.append([float(vet[i][0]**2),float(vet[i][0]),float(1)])
    return np.array(aux)

def criarMatrizY(vet):
    aux = []
    for i in range(len(vet)):
        aux.append([float(vet[i][1])])
    return np.array(aux)

def gauss_seidel(A,b):  
    ITERATION_LIMIT = 1000

    x = np.zeros_like(b)
    for it_count in range(1, ITERATION_LIMIT):
        x_new = np.zeros_like(x)
        print("Iteration {0}: {1}".format(it_count, x))
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new

    print("Solution: {0}".format(x))
    error = np.dot(A, x) - b
    print("Error: {0}".format(error))

A = criarMatrizX(vet)
b = criarMatrizY(vet)
print(A)
print(b)
gauss_seidel(A, b)