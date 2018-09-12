import numpy as np
import random
import matplotlib.pyplot as plt
import math


eps = np.finfo(float).eps
vala = []
valb = []
valx = []

def f(x):
    return ((x-1)*math.exp((x-2)**2))-1

def printar(n,a,b,x):
    list = [n+1,a,b,x,f(a),f(b),f(x)]
    print("Iteracao {}: \nValor de a: {} \nValor de b: {} \nValor de x: {} \nValor de função de a:{} \nValor de função de b: {} \nValor de função de x: {}".format(*list))
    vala.append(a)
    valb.append(b)
    valx.append(x)


def bisseccao(a,b,eps,it,iteracoes):
    while(it<iteracoes):
        if(b-a<eps):
            return (random.uniform(a,b))
        else:
            x = (a+b)/2
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

def relerror(x,apr):
    return abs(x-aprox)/abs(x)

#Exemplo da Tabela 3.1 realizado do livro da UFRGS
a = float(0)
b = float(3)
bi = bisseccao(a,b,(1e-6),0,300)

if bi == None:
    print("Passou do limite, bro, fez sol!")
else:
    print("Caralho, mermão, toma uma raiz aproximada: {}".format(bi))


valerr = []

for aprox in valx:
    valerr.append(relerror(bi,aprox))

plt.plot(valerr, color="#00FF00")
plt.show()