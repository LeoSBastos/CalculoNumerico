# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:07:57 2018

@author: Dhiego
"""

import numpy as np
import matplotlib.pyplot as plt

a=0
b=30
num_iter = 10000
erro = 1e-6
#definir uma função de teste
def f(x):
    return x**2-2.0

#função dropwave
def f_2(x):
    return -(1-np.cos(12*np.sqrt(x**2)))/(0.5*np.sqrt(x**2)+2)
#Iniciar os valores dentro do método da falsa posição
a0 = a
b0 = b
xfp = 1e5*np.ones((1,num_iter))
f0 = f(a)
f1 = f(b)
graf = np.ones((1,num_iter))
#atualização do ponto x
for i in range(num_iter):
    
    if (b0-a0)<erro:
        break
    else:
        xfp[0,i] = (a0*abs(f(b))+b0*abs(f(a)))/(abs(f(b))+abs(f(a)))
        f0 = f(a)
        f1 = f(b)
        fmed = f(xfp[0,i])
        
        if np.sign(f1)*np.sign(fmed)<0:
            a0 = xfp[0,i]
            if (b0-a0)<erro:
                break
        if np.sign(f0)*np.sign(fmed)<0:
            b0 = xfp[0,i]
            if (b0-a0)<erro:
                break
    graf[0,i] = f(xfp[0,i])

#plotar o valor de x a cada iteração
fig=plt.figure(1)
plt.plot(xfp[0,0:i])
plt.show()

#plotar os valores de f(x) para cada iteração
#plt.figure(2)
#plt.plot(graf[0,:])
#plt.show()