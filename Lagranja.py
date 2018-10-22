import numpy as np
from sympy import *
from functools import reduce
x=Symbol('x')

def Lagranja(x,vet):
    formao=[]
    for i in range(len(vet)):
        forms=[]
        for j in range(len(vet)):
            if j!=i:
                forms.append((x-vet[j][0])/(vet[i][0]-vet[j][0]))
        formao.append(vet[i][1]*reduce(lambda x, y:x*y, forms))
    formula = 0
    for i in range(len(formao)):
        formula += formao[i]
    return formula

vet=[[1,1],[2,8],[3,27]]


lagranja = Lagranja(x,vet)
print(lagranja)
print(simplify(Lagranja(x,vet)))
