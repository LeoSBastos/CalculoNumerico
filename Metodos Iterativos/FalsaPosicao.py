import numpy as np
import random
import matplotlib.pyplot as plt

def f(x):
    return (x**2)-2

def pondmed(a0,b0):
    return ((a0*np.absolute(f(b)))+(b0*np.absolute(f(a))))/(np.absolute(f(b))+np.absolute(f(a)))

vala = []
valb = []
valx = []

def printar(n,a,b,x):
    list = [n+1,a,b,x,f(a),f(b),f(x)]
    print("Iteracao {}: \nValor de a: {} \nValor de b: {} \nValor de x: {} \nValor de função de a:{} \nValor de função de b: {} \nValor de função de x: {}".format(*list))
    vala.append(a)
    valb.append(b)
    valx.append(x)


def falsaposicao(a,b,eps,it,iteracoes):
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

#Exemplo da Tabela 3.1 realizado do livro da UFRGS
a = float(0)
b = float(30)
fp = falsaposicao(a,b,1e-6,0,10000)
if fp == None:
    print("Passou do limite, bro, fez sol!")
else:
    print("Caralho, mermão, toma uma raiz aproximada: {}".format(fp))
plt.plot(valx, color="#FF0000")
plt.show()