import numpy
import random
from sympy.mpmath import *

def bisseccao(f, a, b, eps, iteracoes):
    global it = 0
    while(it < iteracoes):
        if(b-a < eps):
            return (random.uniform(a, b))
        else:
            x = (a+b)/2
            if(f(x) == 0):
                return x
            if(f(a) < 0 and f(b) > 0):
                if(f(x) < 0):
                    tabela.add_row([it+1, a, b, x, f(a), f(b), f(x)])
                    a = x
                    it = it+1
                else:
                    tabela.add_row([it+1, a, b, x, f(a), f(b), f(x)])
                    b = x
                    it = it+1
            elif(f(a) > 0 and f(b) < 0):
                if(f(x) > 0):
                    tabela.add_row([it+1, a, b, x, f(a), f(b), f(x)])
                    b = x
                    it = it+1
                else:
                    tabela.add_row([it+1, a, b, x, f(a), f(b), f(x)])
                    a = x
                    it = it+1
            else:
                print("erro")
    return None


def falsaposicao(f,a,b,eps,iteracoes):
    global it = 0
    while(it<iteracoes):
        if(b-a<eps):
            return (random.uniform(a,b))
        else:
            x = pondmed(a,b)
            if(f(x) == 0):
                return x
            if(f(a)<0 and f(b)>0):
                if(f(x) < 0):
                    printar(it,a,b,x)
                    a=x
                    it=it+1
                else:
                    printar(it,a,b,x)
                    b=x
                    it=it+1
            elif(f(a)>0 and f(b)<0):
                if(f(x) > 0):
                    printar(it,a,b,x)
                    b=x
                    it=it+1
                else:
                    printar(it,a,b,x)
                    a=x
                    it=it+1
            else:
                print("meu amigo, queria dizer não, mas vai ter que usar algo que ainda não aprendi")
    return None

def newton(f,val,eps,max_i):
    global it=0
    x=val
    old = None
    while(it<max_i and old != x):
        old = x
        x = x - f(x)/diff(f,x)
        print(i+1,x)
        i+=1
#valor inicial, maximo de iterações
##falta adicionar eps
newton(5,50)

def secante(f, a, b, max_it,err):
    global it = 0
    x = a
    aux = b
    old = None
    while(i < max_it and old != aux):
        old = aux
        res = aux - (f(aux)*((aux-x)/(f(aux)-f(x))))
        print(i+1, res)
        i += 1
        x=aux
        aux=res