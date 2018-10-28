from prettytable import PrettyTable
from Metodos import *
from Valores import vet

tabela = PrettyTable(["Método de Interpolação","2018","2019",])

tabela.add_row(["Sistemas Linear","-","-"])
tabela.add_row(["Interpolação Lagrange",Lagranja(vet,2018),Lagranja(vet,2019)])
tabela.add_row(["Interpolação Newton",Newtao(vet,2018),Newtao(vet,2019)])