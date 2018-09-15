import numpy as np
import random
from prettytable import PrettyTable
import math
from Metodos import *
from Funcoes import *

funcoes = [f1,f2,f3,f4,f5]
tabelas = []

it = 0

eps = 1e-6

raizes=[10,10,10,10,10]

a=1.0
b=3.0

for i in range(5):
    tabela = PrettyTable(["Método","Dados Iniciais","xbarra","fi(x)","Erro","Número de Iterações"])
    bi = bisseccao(funcoes[i],a,b,eps,100)
    tabela.add_row(["Bissecção",[a,b],bi,i+1,(raizes[i]-bi),it])
    tabela.add_row(["Falsa Posição",[a,b],"-",i+1,"-","-"])
    tabela.add_row(["Ponto Fixo",[a,b],"-",i+1,"-","-"])
    tabela.add_row(["Newton",[a,b],"-",i+1,"-","-"])
    tabela.add_row(["Secante",[a,b],"-",i+1,"-","-"])
    tabelas.append(tabela)




for tab in tabelas:
    print(tab)

