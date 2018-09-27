from prettytable import PrettyTable
from Metodos import *
from Funcoes import *

func = [f1,f2,f3,f4,f5]

def f(x):
    return (x**3-(3*x**2)*(2**(-x))+3*x*(4**(-x))-8**(-x))
def fteste(x):
    return x**2-1



def escrever():
    # print(bisseccao(fteste,0,3,1e-6,2000))
    # print(falsaposicao(fteste,0,3,1e-6,2000))
    # print(pontofixo(fteste,0,1e-6,100))
    # print(newton(fteste,2,1e-6,100))
    # print(secante(fteste, 0, 3, 1e-6, 100))
    tabelas = []
    for i in range(5):
        a = 0
        b = 2
        di = [a,b]
        erro = 1e-6
        tabela = PrettyTable(["Método","Dados Iniciais","xbarra","fi(x)","Erro","Número de Iterações"])
        bi = bisseccao(func[i],a,b,erro,2000)
        if(bi == None):
            tabela.add_row(["Bissecção", "-","-",i+1,"-","-"])
        else:
            tabela.add_row(["Bissecção",di,bi[1],i+1,(abs(bi[0]-bi[1])),bi[2]])
        fp = falsaposicao(func[i],a,b,erro,2000)
        if(fp == None):
            tabela.add_row(["Falsa Posição", "-","-",i+1,"-","-"])
        else:
            tabela.add_row(["Falsa Posição", di,fp[1],i+1,(abs(fp[0]-fp[1])),fp[2]])
        pf = pontofixo(func[i],a,erro,100)
        print(pf)
        #tabela.add_row(["Ponto Fixo", di[0],pf[1],i+1,(abs(pf[0]-pf[1])),fp[2]])
        new = newton(func[i],b,erro,100)
        tabela.add_row(["Newton", di[1], new[1],i+1,(abs(new[1]-new[0])),new[2]])
        sec = secante(func[i],a,b,erro,100)
        tabela.add_row(["Secante", di, sec[1],i+1,(abs(sec[0]-sec[1])),sec[2]])
        tabelas.append(tabela)
    for tab in tabelas:
        print(tab)


escrever()
