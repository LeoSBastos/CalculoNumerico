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

plt.plot(xb2,color='r')

