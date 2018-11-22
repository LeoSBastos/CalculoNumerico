from Matrizes import *
import matplotlib.pyplot as plt


#H2
plt.figure(1)
for val in xb2:
    plt.plot(val)
plt.title("Hilbert de Ordem 2")

#H32
plt.figure(2)
for val in xb32:
    plt.plot(val)
plt.title("Hilbert de Ordem 32")

#H64
plt.figure(3)
for val in xb64:
    plt.plot(val)
plt.title("Hilbert de Ordem 64")

#H128
plt.figure(4)
for val in xb128:
    plt.plot(val)
plt.title("Hilbert de Ordem 128")

plt.show()