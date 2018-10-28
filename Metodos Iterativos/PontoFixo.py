import random
import math

def f(x):
    return x**3 - ((3*(x**2))*(2**(-x))) + (3*x*(4**(-x))) - (8**(-x))

def g(x):
    return x-f(x)

def pontofixo(val,eps,max_i):
    i=0
    x=val
    old = None 
    while(i<max_i and old != x):
        old = x
        x = g(x);
        print(i+1,x)
        i+=1
        if(abs(old-x)<eps):
            return random.uniform(old,x)
    return x
print(pontofixo(0,1e-6,50))