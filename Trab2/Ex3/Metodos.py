import numpy as np
from sympy import *
from functools import reduce
x = Symbol('x')

def diferencasDivididas(vet):
    val = []
    count = 0
    vetdelta = [vet[i][1] for i in range(len(vet))]
    vetx = [vet[i][0] for i in range(len(vet))]
    while (len(vetdelta) > 1):
        vettemp = []
        val.append(vetdelta[0])
        count+=1
        for i in range(len(vetdelta) - 1):
            temp = (vetdelta[i + 1] - vetdelta[i]) / (vetx[i + count] - vetx[i])
            vettemp.append(temp)
        vetdelta = vettemp
    val.append(vetdelta[0])
    return val

def Newtao(vet):
    val = diferencasDivididas(vet)
    funcfinal = []
    funcfinal.append(val[0])
    for i in range(1,len(vet)):
        functemp = [] 
        for j in range(i):
            functemp.append(x - vet[j][0])
        funcfinal.append(val[i] * reduce(lambda x, y: x * y,functemp))        
    polinomio = simplify(reduce(lambda x,y:x + y,funcfinal))
    return polinomio

def Lagranja(vet):
    formao = []
    for i in range(len(vet)):
        forms = []
        for j in range(len(vet)):
            if j != i:
                forms.append((x - vet[j][0]) / (vet[i][0] - vet[j][0]))
        formao.append(vet[i][1] * reduce(lambda x, y:x * y, forms))
    formula = simplify(reduce(lambda x,y :x + y,formao))
    return formula

def criarMatrizA(vet):
    aux = []
    for i in range(len(vet)):
        aux.append([vet[i][0]**2,vet[i][0],1])
    return aux

def criarMatrizb(vet):
    aux = []
    for i in range(len(vet)):
        aux.append([vet[i][1]])
    return aux

def calculaCoeficientes(mat):
	for i in range(min(len(mat), len(mat[0]))):
		for r in range(i, len(mat)):
			zero_row = mat[r][i] == 0
			if zero_row:
				continue
			mat[i], mat[r] = mat[r], mat[i]
			first_row_first_col = mat[i][i]
			for rr in range(i + 1, len(mat)):
				this_row_first = mat[rr][i]
				scalarMultiple = -1 * this_row_first / first_row_first_col
				for cc in range(i, len(mat[0])):
					mat[rr][cc] += mat[i][cc] * scalarMultiple
			break
	for i in range(min(len(mat), len(mat[0])) - 1, -1, -1):
		first_elem_col = -1
		first_elem = -1
		for c in range(len(mat[0])):
			if mat[i][c] == 0:
				continue
			if first_elem_col == -1:
				first_elem_col = c
				first_elem = mat[i][c]
			mat[i][c] /= first_elem
		for r in range(i):
			this_row_above = mat[r][first_elem_col]
			scalarMultiple = -1 * this_row_above
			for cc in range(len(mat[0])):
				mat[r][cc] += mat[i][cc] * scalarMultiple



def criaMatrizAB(A, b):
	retval = []
	for i in range(len(A)):
		r = A[i]
		newrow = r[:] + b[i]
		retval.append(newrow)
	return retval
    

def transposta(mat):
	retval = []
	for c in range(len(mat[0])):
		newrow = []
		for r in range(len(mat)):
			newrow.append(mat[r][c])
		retval.append(newrow)
	return retval

def polinomioLinear(vet):
    A = criarMatrizA(vet)
    b = criarMatrizb(vet)
    Ab = criaMatrizAB(A, b)			

    calculaCoeficientes(Ab)

    x = transposta(Ab)[3]

    formula = []
    for i in reversed(range(len(x))):
        formula.append(Symbol('x')**(i))

    aux =[]
    for i in range(len(x)):
        aux.append(x[i]*formula[i])
    polinomio = reduce(lambda x,y: x+y, aux)
    return polinomio


def SubstituirX(poly,valor):
    return poly.subs(x,valor)