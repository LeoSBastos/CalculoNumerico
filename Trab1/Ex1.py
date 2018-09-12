import numpy as np
import random
from prettytable import PrettyTable
import math

tabelas = []


for i in range(5):
    tabela = PrettyTable(["Método","Dados Iniciais","xbarra","fi(x)","Erro","Número de Iterações"])
    tabela.add_row(["Bissecção", "-","-",i+1,"-","-"])
    tabela.add_row(["Falsa Posição", "-","-",i+1,"-","-"])
    tabela.add_row(["Ponto Fixo", "-","-",i+1,"-","-"])
    tabela.add_row(["Newton", "-","-",i+1,"-","-"])
    tabela.add_row(["Secante", "-","-",i+1,"-","-"])
    tabelas.append(tabela)


for tab in tabelas:
    print(tab)

