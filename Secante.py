def f(x):
    return x**2-1


def secante(a, b, max_it):
    i = 0
    x = a
    aux = b
    old = None
    while(i < max_it and old != aux):
        old = aux
        res = aux - (f(aux)*((aux-x)/(f(aux)-f(x))))
        print(i+1, res)
        i += 1
        x=aux
        aux=res




secante(20.0, 30.0, 100)
