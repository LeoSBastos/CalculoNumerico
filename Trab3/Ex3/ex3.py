from prettytable import PrettyTable
from Metodos import *
from Valores import vet

tabela = PrettyTable(["Método de Interpolação","2018","2019",])

tabela.add_row(["Sistemas Linear","-","-"])
lagranja = Lagranja(vet)
print("\n\n")
tabela.add_row(["Interpolação Lagrange",SubstituirX(lagranja,2018),SubstituirX(lagranja,2019)])
newtao = Newtao(vet)
print("\n\n")
tabela.add_row(["Interpolação Newton",SubstituirX(newtao,2018),SubstituirX(newtao,2019)])

print(tabela)