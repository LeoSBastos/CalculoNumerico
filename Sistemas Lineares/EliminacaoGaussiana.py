from sympy import *
from functools import reduce
import numpy as np

def calculaXBarra(mat):
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

def eliminacaoLinear(vet):
    A = criarMatrizA(vet)
    print(A)
    b = criarMatrizb(vet)
    Ab = criaMatrizAB(A, b)			

    calculaCoeficientes(Ab)

    x = transposta(Ab)[3]
    return x