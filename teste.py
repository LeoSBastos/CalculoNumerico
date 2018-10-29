import numpy as np


vet = [[1,1],[2,8],[3,27]]
aux = []
auy = []
for i in range(len(vet)):
    aux.append([vet[i][0]**2,vet[i][0],1])

for i in range(len(vet)):
    auy.append([vet[i][1]])

arr = np.matrix(aux)
arr2 = np.matrix(auy)
print(type(arr))
print(arr)
print(arr2)
print(len(arr))