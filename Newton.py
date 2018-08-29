#função
def f(x):
    return x**2-1

#derivada da função
def fdif(x):
    return 2*x

def newton(val,eps,max_i):
    i=0
    x=val
    old = None
    while(i<max_i and old != x):
        old = x
        x = x - f(x)/fdif(x)
        print(i+1,x)
        i+=1
#valor inicial, maximo de iterações
##falta adicionar eps
newton(5,50)
