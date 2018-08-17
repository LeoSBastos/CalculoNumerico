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

eps = np.finfo(float).eps


def f(x):
    return np.exp(x) - x -2

def printar(n,a,b,x):
    print("a: ",a,"b: " ,b,"x :",x)

def bisseccao(a,b,iteracoes):
    if(iteracoes > 0):
        if(b-a<eps):
            return (random.uniform(a,b))
        elif(f(a)<0 and f(b)>0):
            x = (a+b)/2
            if(f(x) == 0):
    	        return x
            if(x < 0):
                printar(iteracoes,a,b,x)
                bisseccao(x,b,iteracoes-1)
            else:
                printar(iteracoes,a,b,x)
                bisseccao(a,x,iteracoes-1)
        elif(f(a)>0 and f(b)<0):
            x = (a+b)/2
            if(f(x) == 0):
    	        return x
            if(x > 0):
                printar(iteracoes,a,b,x)
                bisseccao(x,b,iteracoes-1)
            else:
                printar(iteracoes,a,b,x)
                bisseccao(a,x,iteracoes-1)
    else:
        return None
                    


#Exemplo da Tabela 3.1 realizado do livro da UFRGS
a = float(-2)
b = float(0)
bisseccao(a,b,5)



