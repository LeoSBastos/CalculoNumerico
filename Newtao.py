import numpy as np
from sympy import *
from functools import reduce
x=Symbol('x')

def Newtao(vet):
    val = []
    count=0
    vetdelta = [vet[i][1] for i in range(len(vet))]
    vetx = [vet[i][0] for i in range(len(vet))]
    while (len(vetdelta)>1):
        vettemp = []
        val.append(vetdelta[0])
        count+=1
        for i in range(len(vetdelta)-1):
            temp = (vetdelta[i+1]-vetdelta[i])/(vetx[i+count]-vetx[i])
            vettemp.append(temp)
        vetdelta = vettemp
    val.append(vetdelta[0])
    return val

def Polinomio(vet,val,x,grau):
    funcfinal = []
    funcfinal.append(val[0])
    for i in range(1,grau):
        functemp=[]
        for j in range(i):
            print((x-vet[j][0]))
            functemp.append(x-vet[j][0])
        print("\n")
        funcfinal.append(val[i] * reduce(lambda x, y: x*y,functemp))
    polinomio = reduce(lambda x,y:x+y,funcfinal)
    return polinomio

vet=[[-1,3],[0,1],[1,3],[3,43]]

newtao = Polinomio(vet,Newtao(vet),x,4)
print(newtao)
print(simplify(newtao))