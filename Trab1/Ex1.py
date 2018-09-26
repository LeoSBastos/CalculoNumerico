import numpy as np
import random
from prettytable import PrettyTable
import math
from mpmath import diff
from Metodos import *


def f(x):
    return (x**3-(3*x**2)*(2**(-x))+3*x*(4**(-x))-8**(-x))
def fteste(x):
    return x**2-1




def escrever():
    # print(newton(fteste,2,1e-6,100))
    # print(bisseccao(fteste,0,3,1e-6,0,100))
    # print(falsaposicao(fteste,0,3,1e-6,0,2600))
    # print(secante(fteste, 0, 3, 100))
    tabelas = []
    for i in range(1):
        a = 0
        b = 2
        di = [a,b]
        erro = 1e-6
        tabela = PrettyTable(["Método","Dados Iniciais","xbarra","fi(x)","Erro","Número de Iterações"])
        bi = bisseccao(f,a,b,erro,100)
        #erro = calculaErro(bi,)
        tabela.add_row(["Bissecção",di,bi[0],i+1,erro,bi[1]])
        fp = falsaposicao(f,a,b,erro,100)
        tabela.add_row(["Falsa Posição", di,fp[0],i+1,erro,fp[1]])
        tabela.add_row(["Ponto Fixo", "-","-",i+1,"-","-"])
        new = newton(f,b,1e-6,100)
        tabela.add_row(["Newton", di[1], new[0],i+1,"-",new[1]])
        sec = secante(f,a,b,1e-6,100)
        tabela.add_row(["Secante", di, sec[0],i+1,"-",sec[1]])
        tabelas.append(tabela)
    for tab in tabelas:
        print(tab)


escrever()
