import numpy as np
from sympy import *

x=Symbol('x')

def Lagranja(x,vet):
    formao=[]
    for i in range(len(vet)):
        forms=[]
        for j in range(len(vet)):
            if j!=i:
                forms.append((x-vet[j][0])/(vet[i][0]-vet[j][0]))
        formao.append(vet[i][1]*forms[0]*forms[1])
    formula = 0
    for i in range(len(formao)):
        formula += formao[i]
    return formula


vet=[[-2,2],[0,-2],[4,1]]

print(Lagranja(x,vet))