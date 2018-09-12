#           //////,           _____ _
#         */@&/////*         | __  |_|___ ___ ___ ___ ___ ___ ___
#         *//////***         | __ -| |_ -|_ -| -_|  _|  _| .'| . |
#     //////////**** &&&&    |_____|_|___|___|___|___|___|__,|___|
#    /////////****** &&&
#    //////......./&&&&&&&    Algoritmo de Bissecção
#    *//// &&&&&&&&&&&&&&(    Desenvolvido Por Luiz Gustavo Benicio Neves e Leonardo Soares
#     ///*/&&&&&&&&&&&&&%     Para a Discliplina de Calculo Numérico
#         /&&&&&&&&&
#          &&&&&&@@&
#            #&&


import numpy as np
import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable

eps = np.finfo(float).eps

tabela = PrettyTable(['Iteração', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)'])


def f(x):
    return x*x-1


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



# Exemplo da Tabela 3.1 realizado do livro da UFRGS
a = float(0)
b = float(3)
bisseccao(a, b, (1e-3), 0, 300)
print(tabela)
