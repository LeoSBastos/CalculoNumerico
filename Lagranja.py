import numpy
import sympy

x=Symbol('x')

def Lagranja(x,vet):
    formula=None
    forms=[]
    for i in range(len(vet)):
        forms=[]
        for j in range(len(vet)):
            if j!=i:
                forms.append((x-vet[j][0])/(vet[i][0]-vet[j][0]))
                k+=1
        formula+=(vet[i][1]*forms[0]*form[1])
    return formula

vet=[[0,1],[],[]]

print(Lagranja(x,vet))