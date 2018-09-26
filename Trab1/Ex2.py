import numpy as np
import math

vals = []
i = 20


# def f(x):
#     return ((x-1)*((math.exp(x-2))**2))-1

def f(x):
    return x**2-1

def g(x):
    return f(x)-x

def pontofixo():
    while i < 30:
        val = f(g(i))
        if(f(g(i)) <= 0):
            print(f(i), g(i), f(g(i)))
        i += 1
