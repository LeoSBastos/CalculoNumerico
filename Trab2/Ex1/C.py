from Matrizes import *
from EliminacaoGaussiana import *
import matplotlib.pyplot as plt

x2 = eliminacaoGaussiana(h2,0)
xb2 = graph
x32 = eliminacaoGaussiana(h32,0)
xb32 = graph
x64 = eliminacaoGaussiana(h64,0)
xb64 = graph
x128 = eliminacaoGaussiana(h128,0)
xb128 = graph

#H2
plt.figure(1)
for val in xb2:
    for i in range(len(val)):
        plt.plot(val[i])
plt.title("Hilbert de Ordem 2")

#H32
plt.figure(2)
for val in xb32:
    for i in range(len(val)):
        plt.plot(val[i])
plt.title("Hilbert de Ordem 32")

#H64
plt.figure(3)
for val in xb64:
    for i in range(len(val)):
        plt.plot(val[i])
plt.title("Hilbert de Ordem 64")

#H128
plt.figure(4)
for val in xb128:
    for i in range(len(val)):
        plt.plot(val[i])
plt.title("Hilbert de Ordem 128")

plt.show()