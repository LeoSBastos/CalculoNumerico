import numpy as np

def MatrizHilbert(N):
	aui = []
	for i in range(1,N+1):
		auj = []
		for j in range(1,N+1):
			auj.append(1/(i+j-1))
		aui.append(auj)
	return aui