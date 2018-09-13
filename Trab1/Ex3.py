import numpy as np
import random
import matplotlib.pyplot as plt
import math
from prettytable import PrettyTable

tabela = PrettyTable(['Iteração', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)'])

eps = np.finfo(float).eps
vala = []
valb = []
valx = []

def f(x):
    return ((x-1)*math.exp((x-2)**2))-1

def bisseccao(a, b, eps, it, iteracoes):
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

def relerror(x,apr):
    return abs(x-aprox)/abs(x)

#Exemplo da Tabela 3.1 realizado do livro da UFRGS
a = float(0)
b = float(3)
bi = bisseccao(a,b,(1e-6),0,300)
print(tabela)

if bi == None:
    print("Passou do limite, bro, fez sol!")
else:
    print("Caralho, mermão, toma uma raiz aproximada: {}".format(bi))


valerr = []

for aprox in valx:
    valerr.append(relerror(bi,aprox))

plt.plot(valerr, color="#00FF00")
plt.show()