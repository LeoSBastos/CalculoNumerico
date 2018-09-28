from Metodos import pontofixo
from prettytable import PrettyTable
import random
import matplotlib.pyplot as plt

valerror1 = []
valerror2 = []
valerror3 = []
valerrors = [valerror1,valerror2,valerror3]
i = 20

val = 2

def f(x):
    return x**2-1

def g1(x):
    return  (x - (f(x)/10))

def g2(x):
    return x-(f(x)/2)

def g3(x):
    return x - (f(x)/1000)

gs = [g1,g2,g3]

erro=1e-6
max_it=1000000000000
tabela = PrettyTable(["Dado Inicial","xbarra","fi(x)","Erro","Número de Iterações"])

def pontofixo(f,val,eps,max_i,valerror):
    i=0
    x = val
    old = None
    valores = []
    while(i < max_i and old != x):
        old = x
        x=float(x - f(x))
        i+=1
        valerror.append(abs(old-x))
        if(abs(x)>1e+20):
            return None
        if(abs(old-x)<eps):
            x = random.uniform(old,x)
    valores.append(old)
    valores.append(x)
    valores.append(i)
    return valores

for i in range(3):
    pf = pontofixo(gs[i],val,erro,max_it,valerrors[i])
    if(pf == None):
        tabela.add_row([val,"-",i+1,"-","-"])
    else:
        tabela.add_row([val,pf[1],i+1,(abs(pf[0]-pf[1])),pf[2]])

print(tabela)

plt.plot(valerror1, color="#FF0080")
plt.plot(valerror2, color="#808080")
plt.plot(valerror3, color="#FF00FF")
plt.show()
