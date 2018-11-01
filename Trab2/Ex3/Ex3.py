from prettytable import PrettyTable
from Metodos import *
from Valores import vet

tabela = PrettyTable(["Método de Interpolação","2018","2019",])
linear = polinomioLinear(vet)
tabela.add_row(["Sistemas Linear",int(SubstituirX(linear,2018)),int(SubstituirX(linear,2019))])
lagranja = Lagranja(vet)
tabela.add_row(["Interpolação Lagrange",SubstituirX (lagranja,2018),SubstituirX(lagranja,2019)])
newtao = Newtao(vet)
tabela.add_row(["Interpolação Newton",int(SubstituirX(newtao,2018)),int(SubstituirX(newtao,2019))])

print(tabela)