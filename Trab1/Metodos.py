import numpy as np
import random
import math
from bigfloat import *
from mpmath import diff

def bisseccao(f,a,b,eps,iteracoes):
    it = 0
    valores = []
    old=None
    x=0
    while(it<iteracoes):
        if(abs(b-a)<eps):
            x = random.uniform(b,a)
            valores.append(old)
            valores.append(x)
            valores.append(it)
            return valores
        else:
            old = x
            x = (a+b)/2
            if(f(x) == 0):
                valores.append(old)
                valores.append(x)
                valores.append(it)
                return valores
            if(f(a)<0 and f(b)>0):
                if(f(x) < 0):
                    #valores.append([it+1, a, b, x, f(a), f(b), f(x)])
                    a=x
                    it=it+1
                else:
                    #valores.append([it+1, a, b, x, f(a), f(b), f(x)])
                    b=x
                    it=it+1
            elif(f(a)>0 and f(b)<0):
                if(f(x) > 0):
                    #valores.append([it+1, a, b, x, f(a), f(b), f(x)])
                    b=x
                    it=it+1
                else:
                    #valores.append([it+1, a, b, x, f(a), f(b), f(x)])
                    a=x
                    it=it+1
            else:
                return None

def newton(f,val,eps,max_i):
    valores = []
    i=0
    x=val
    old = None
    while(i<max_i and old != x):
        old = x
        if diff(f,x) != 0:
            x = float(x - f(x)/diff(f,x))
            i+=1
        else:
            print("Deu ruim, derivada é 0")
        if(abs(old-x)<eps):
            x=random.uniform(old,x)
    valores.append(old)
    valores.append(x)
    valores.append(i)
    return valores


def pondmed(f,a,b,a0,b0):
    return ((a*np.absolute(f(b0)))+(b*np.absolute(f(a0))))/(np.absolute(f(b0))+np.absolute(f(a0)))

def falsaposicao(f,a0,b0,eps,iteracoes):
    it = 0
    valores = []
    a = a0
    b = b0
    old = None
    x = 0
    while(it<iteracoes):
        if(b-a<eps):
            x = (random.uniform(a0,b0))
            valores.append(old)
            valores.append(x)
            valores.append(it)
            return valores
        else:
            old = x
            x = pondmed(f,a,b,a0,b0)
            if(f(x) == 0):
                valores.append(old)
                valores.append(x)
                valores.append(it)
                return valores
            if(f(a)<0 and f(b)>0):
                if(f(x) < 0):
                    a=x
                    it=it+1
                else:
                    b=x
                    it=it+1
            elif(f(a)>0 and f(b)<0):
                if(f(x) > 0):
                    b=x
                    it=it+1
                else:
                    a=x
                    it=it+1
            else:
                return None

def secante(f, a, b, eps, max_it):
    valores = []
    i = 0
    x = a
    aux = b
    old = None
    while(i < max_it and x != aux):    
        res = aux - (f(aux)*((aux-x)/(f(aux)-f(x))))
        i += 1
        x=aux
        aux=res
        if(abs(x-aux)<eps):
            aux=random.uniform(x,aux)
    valores.append(x)
    valores.append(aux)
    valores.append(i)
    return valores

def pontofixo(f,val,eps,max_i):
    i=0
    x=val
    old = 2
    valores = []
    while(i < max_i and old != x):
        old = x
        x = BigFloat.exact(x) - BigFloat.exact(f(x))
        i+=1
        if(abs(old-x)<eps):
            x = random.uniform(old,x)
    valores.append(old)
    valores.append(x)
    valores.append(i)    
    return valores
