from GaussSeidel import *
import numpy as np

A=np.array([[1.0,0.0,-1.0],[-0.5,1.0,-0.25],[1.0,-0.5,1.0]])
b=[0.2,-1.425,2.0]

valB = gaussseidel(A,b,1e-2,300)
valfinalB = calcularVetor()
print(valB)