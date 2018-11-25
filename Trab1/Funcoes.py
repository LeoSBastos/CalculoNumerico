import math
from mpmath import *

def f1(x):
    return cos(x) + 1
def f2(x):
    return 10 + (x - 2)**2 - 10*cos(2*pi*x)
def f3(x):
    return x**3 - ((3*(x**2))*(2**(-x))) + (3*x*(4**(-x))) - (8**(-x))
def f4(x):
    return sin(x)*sin(x**2/pi)
def f5(x):
    return (x - 1.44)**5
