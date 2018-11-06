#gauss suicidal
import numpy as np
from scipy.linalg import solve
import collections

vals = []

count = []

def gauss(A, b, x):
    L = np.tril(A)
    print(L)
    U = A - L
    print(U)
    x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    vals.append(x)
    return x            

def gaussseidel(A,valb,tol,lim):
    count.clear()
    b = []
    for i in range(len(A)):
        b.append([valb])
    cont = 0
    x = [1, 1, 1]
    while(True):
        old = x
        x = gauss(A,b,x)
        cont = cont + 1
        print(cont)
        tols = []
        for val1,val2 in zip(x,old):
            if((abs(val1 - val2)) < tol):
                tols.append(True)
            else:
                tols.append(False)
        aux = np.all(tols)
        if np.allclose(x,old):
            count.append(cont)
            return x
        elif aux:
            count.append(cont)
            print("TOL excedido")
            return x
        elif count == lim:
            count.append(cont)
            print("Iteracoes excedidas")
            return x

def calcularVetor():
    valx1 = []
    valx2 = []
    valx3 = []
    valfinal = [valx1,valx2,valx3]
    for val in vals:
        for j in range(len(val)):
            valfinal[j].append(val[j])
    return valfinal

def getCount():
    return count

def MatrizHilbert(N):
	aui = []
	for i in range(1,N + 1):
		auj = []
		for j in range(1,N + 1):
			auj.append(1 / (i + j - 1))
		aui.append(auj)
	return np.array(aui)

A = MatrizHilbert(2)

val = gaussseidel(A,0,1e-2,300)
print(val)
print(count)
#valfinal = calcularVetor()
