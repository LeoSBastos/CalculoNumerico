import numpy as np
import random
import matplotlib.pyplot as plt

def pondmed(a,b):
    x=((a*np.absolute(f(a)))+(b*np.absolute(f(b))))/(np.absolute(f(b))+np.absolute(f(a)))