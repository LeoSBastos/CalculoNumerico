from Metodos import pontofixo
from prettytable import PrettyTable
vals = []
i = 20

val = 2

# def f(x):
#     return ((x-1)*((math.exp(x-2))**2))-1

def f(x):
    return x**2-1

def g1(x):
    return  x - f(x)

def g2(x):
    return x-(f(x)/2)

def g3(x):
    return x + ((f(x)**1/2)*2.321*(11+24+101+69))

gs = [g1,g2,g3]
erro=1e-6
max_it=1000000000000
tabela = PrettyTable(["Dado Inicial","xbarra","fi(x)","Erro","Número de Iterações"])

for i in range(3):
    pf = pontofixo(gs[i],val,erro,max_it)
    if(pf == None):
        tabela.add_row([val,"-",i+1,"-","-"])
    else:
        tabela.add_row([val,pf[1],i+1,(abs(pf[0]-pf[1])),pf[2]])

print(tabela)
