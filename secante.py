import math

def f(x):
    return math.exp(-x**2) - math.cos(x)

def metodoSecante():
    x0 = 1
    x1 = 2
    itermax = 40
    iteracao = 0
    toler = 0.0001
    Erro = 1
    while Erro >= toler and iteracao <= itermax:
        iteracao += 1
        x = (x0*f(x1) - x1*f(x0))/ (f(x1) - f(x0))
        x0 = x1
        x1 = x
        Erro = abs((x-x1)/x)
    print('Raiz: ', x)
    print('f(Raiz) = ', f(x))
    print('Erro em x = ', Erro)
    print('Número de iterações = ', iteracao)
metodoSecante()
