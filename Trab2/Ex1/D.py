from Metodos import *
import time
start_time = time.time()
h128 = MatrizHilbert(128)
x128 = gaussseidel(h128,0,1e-6,1000000000)
print(x128)
print("--- %s seconds ---" % (time.time() - start_time))