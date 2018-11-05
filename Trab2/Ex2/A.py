import numpy as np

def decomposicaoLU(A):
    i = 1
    U = np.copy(A)  
    n = np.shape(U)[0]  
    L = np.eye(n)  
    for j in np.arange(n-1):  
        for i in np.arange(j+1,n):  
            L[i,j] = U[i,j]/U[j,j]  
            for k in np.arange(j+1,n):  
                U[i,k] = U[i,k] - L[i,j]*U[j,k]  
            U[i,j] = 0
            i = i + 1
    print(i)
    matrizLU = []
    matrizLU.append(L)
    matrizLU.append(U)
    return matrizLU

print("Matriz original:")
matriz = np.matrix("1 0 -2; -0.5 1 -0.25; 1 -0.5 1 ")
print(matriz,"\n")
list = decomposicaoLU(matriz)
print("Matriz triangular inferior:\n", np.matrix(list[0]),"\n")
print("Matriz triangular superior:\n", np.matrix(list[1]),"\n")