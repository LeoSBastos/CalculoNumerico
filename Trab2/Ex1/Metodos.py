#gauss suicidal
import numpy as np
from scipy.linalg import solve
import collections

vals = []

count = 0

def gauss(A, b, x):
    L = np.tril(A)
    U = A - L
    aux1 = np.dot(U, x) 
    aux2 = np.linalg.inv(L)
    aux3 = b - aux1
    x = np.dot(aux2, aux3)
    vals.append(x)
    return x            

def gaussseidel(A,valb,tol,lim):
    global count
    b = []

    for i in range(len(A)):
        b.append(valb)
    count = 0

    x = []
    for i in range(len(b)):
        x.append(1)
    while(True):
        old = x
        x = gauss(A,b,x)
        count = count + 1
        tols = []
        for val1,val2 in zip(x,old):
            if((abs(val1 - val2)) < tol):
                tols.append(True)
            else:
                tols.append(False)
        aux = np.all(tols)
        if np.allclose(x,old):
            return x
        elif aux:
            print("TOL excedido")
            return x
        elif count == lim:
            print("Iteracoes excedidas")
            return x

def calcularVetor(A):
    valfinal = [[] for x in range(len(A))]
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

#A = MatrizHilbert(2)

#val = gaussseidel(A,0,1e-2,300)
#valfinal = calcularVetor()
