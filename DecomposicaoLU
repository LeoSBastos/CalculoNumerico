import numpy as np
 
def decomposicaoLU(A):
    U = np.copy(A)  
    n = np.shape(U)[0]  
    L = np.eye(n)  
    for j in np.arange(n-1):  
        for i in np.arange(j+1,n):  
            L[i,j] = U[i,j]/U[j,j]  
            for k in np.arange(j+1,n):  
                U[i,k] = U[i,k] - L[i,j]*U[j,k]  
            U[i,j] = 0
    matrizLU = []
    matrizLU.append(L)
    matrizLU.append(U)
    return matrizLU

matriz = np.matrix("1 2 3; 4 5 6; 7 8 9")
print(matriz)
print(decomposicaoLU(matriz))
