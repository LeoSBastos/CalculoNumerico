import numpy as np
import math

vals = []
i = 0


def f(x):
    return ((x-1)*((math.exp(x-2))**2))-1


def g(x):
    return f(x)-x


while i < 30:
    val = f(g(i))
    if(f(g(i)) <= 0):
        print(f(i), g(i), f(g(i)))
    i += 1
