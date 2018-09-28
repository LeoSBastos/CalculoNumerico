# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:21:25 2018

@author: Dhiego Loiola de Araújo

Este algoritmo implementa o método do Ponto Fixo
"""
import math

#vamos definir uma função para a entrada do algoritmo
def f(x):
    return x-(x**2-1)

def f1(x):
    return x-(x**2-1)/(x**3+8*x**2)

#expansão em série de taylor para cos(x) em a=0
def f2(x):
    return 1-(x**2)/2+(x**4)/24-(x**6)/720+(x**8)/40320

#biblioteca do python
def f3(x):
    return math.exp(x) -x -1
	
################################## Configurações iniciais ###########
erro = 1e-6
N = 1000000 #número de iterações
x = [] #lista
x0 = 1 #valor inicial
x.append(x0) #valor para a lista

#laço principal
for i in range(1,N):
    x.append(f3(x[i-1]))
    if abs(x[i]-x[i-1])<erro:
        break
    
print(i,x[i])