def f(x):
    return x**2-1


def secante(a, b, max_it):
    i = 0
    x = a
    aux = b
    while(i < max_it):
        x = x - (f(x)*((x-aux)/f(x)-f(aux)))
        print(i+1, x)
        i += 1


secante(2, 3, 100)
