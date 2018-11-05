#gauss suicidal

import numpy as np
from scipy.linalg import solve
import collections

vals = []


def gauss(A, b, x):
    L = np.tril(A)
    U = A - L
    x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    vals.append(x)
    return x            

def gaussseidel(A,b,tol,lim):
    cont = 0
    x = [1, 1, 1]
    while(True):
        old = x
        x = gauss(A,b,x)
        cont = cont + 1
        tols = []
        for val1,val2 in zip(x,old):
            if((abs(val1-val2))<tol):
                tols.append(True)
            else:
                tols.append(False)
        aux = np.all(tols)
        if np.allclose(x,old):
            return x
        elif aux:
            print("TOL excedido")
            return x
        elif cont == lim:
            print("Iteracoes excedidas")
            return x

def calcularVetor():
    valx1 = []
    valx2 = []
    valx3  = []
    valfinal = [valx1,valx2,valx3]
    for val in vals:
        for j in range(len(val)):
            valfinal[j].append(val[j])
    return valfinal

A = np.array([[1.0, 0.0, -1.0], [-0.5, 1.0, -0.25], [1.0, -0.5, 1.0]])
b = [0.2, -1.425, 2.0]
#val = gaussseidel(A,b,1e-2,300)
#valfinal = calcularVetor()
