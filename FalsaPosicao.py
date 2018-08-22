import numpy as np
import random
import matplotlib.pyplot as plt

def f(x):
    return (x**2)+2

def pondmed(a,b):
    return ((a*np.absolute(f(a)))+(b*np.absolute(f(b))))/(np.absolute(f(b))+np.absolute(f(a)))

vala = []
valb = []
valx = []

def printar(n,a,b,x):
    list = [n,a,b,x,f(a),f(b),f(x)]
    print("Iteracao {}: \nValor de a: {} \nValor de b: {} \nValor de x: {} \nValor de função de a:{} \nValor de função de b: {} \nValor de função de x: {}".format(*list))
    vala.append(a)
    valb.append(b)
    valx.append(x)


def falsaposicao(a,b,eps,it,iteracoes):
    if(it<iteracoes):
        if(b-a<eps):
            return (random.uniform(a,b))
        else:
            x = pondmed(a,b)
            if(f(x) == 0):
                return x
            if(f(a)<0 and f(b)>0):
                if(f(x) < 0):
                    printar(it,a,b,x)
                    bisseccao(x,b,eps,it+1,iteracoes)
                else:
                    printar(it,a,b,x)
                    bisseccao(a,x,eps,it+1,iteracoes)
            elif(f(a)>0 and f(b)<0):
                if(f(x) > 0):
                    printar(it,a,b,x)
                    bisseccao(x,b,eps,it+1,iteracoes)
                else:
                    printar(it,a,b,x)
                    bisseccao(a,x,eps,it+1,iteracoes)
            else:
                print("meu amigo, queria dizer não, mas vai ter que usar algo que ainda não aprendi")
    else:
        return None



#Exemplo da Tabela 3.1 realizado do livro da UFRGS
a = float(0)
b = float(3)
fp = falsaposicao(a,b,(10**-6),0,300)
if bi == None:
    print("Passou do limite, bro, fez sol!")
else:
    print("Caralho, mermão, toma uma raiz aproximada: {}".format(*bi))
plt.plot(valx, color="#FF0000")
plt.show()