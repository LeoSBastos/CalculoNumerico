from Matrizes import *
from EliminacaoGaussiana import *
import time
start_time = time.time()

x128 = eliminacaoGaussiana(h128,0)
print(x128)
print("--- %s seconds ---" % (time.time() - start_time))