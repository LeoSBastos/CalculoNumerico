from Metodos import *

h2 = MatrizHilbert(2)
h32 = MatrizHilbert(32)
h64 = MatrizHilbert(64)
h128 = MatrizHilbert(128)

x2 = gaussseidel(h2,0,1e-6,100000)
count2 = getCount()
xb2 = calcularVetor()
x32 = gaussseidel(h32,0,1e-6,100000)
count32 = getCount()
xb32 = calcularVetor()
x64 = gaussseidel(h64,0,1e-6,100000)
count64 = getCount()
xb64 = calcularVetor()
x128 = gaussseidel(h128,0,1e-6,100000)
count128 = getCount()
xb128 = calcularVetor()