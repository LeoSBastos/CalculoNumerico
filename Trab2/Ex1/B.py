from prettytable import PrettyTable
from A import *

tabela = PrettyTable(["Matriz", "Num Iteracoes", "XBarra"])

tabela.add_row(["h2", count2, x2])
tabela.add_row(["h32", count32, x32])
tabela.add_row(["h64", count64, x64])
tabela.add_row(["h128", count128, x128])

print(tabela)