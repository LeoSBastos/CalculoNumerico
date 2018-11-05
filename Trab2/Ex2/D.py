import matplotlib.pyplot as plt
#from A import valfinalA
from B import *
from C import *


#B
plt.figure(1)
plt.plot(valfinalB[0],color="#dd001f", label="x1")
plt.plot(valfinalB[1],color="#c6001b", label="x2")
plt.plot(valfinalB[2],color="#b00018", label="x3")
plt.title("B")
plt.legend(loc="best")
#C
plt.figure(2)
plt.plot(valfinalC[0],color="#e4a2e7", label="x1")
plt.plot(valfinalC[1],color="#cd91cf", label="x2")
plt.plot(valfinalC[2],color="#b681b8", label="x3")
plt.title("C")
plt.legend(loc="best")
plt.show()