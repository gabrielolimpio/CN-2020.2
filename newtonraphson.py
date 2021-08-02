import math
from sympy import diff

def f(x):
    #return x**3 - x + 1
    return math.exp(-x**2) - math.cos(x)

def der(x):
    #return 3*x**2 - 1
    return -2*x*math.exp(-x**2) + math.sin(x)

#der = diff(pow(x, 2) - math.exp(x), x)

def metodoNewton():
         # exemplo: x0 = 1 e iteracoes = 30
         #f = float(input('Digite a função desejada: '))
         x0 = float(input("Digite a aproximação inicial x0: "))
         iteracoesMax = int(input("Digite a quantidade de iterações: "))
         tolerancia = float(input('Digite a tolerância desejada: '))
         iteracao = 0
         x1 = 0

         #print('teste: ', der)
         while iteracao < iteracoesMax and math.fabs(f(x0)) > tolerancia:
                  x0 = x0 - f(x0) / der(x0)
                  iteracao += 1
         if iteracao == iteracoesMax:
             print('Número máximo de iterações atingido!')
         print('Iterações realizadas:', iteracao)
         print("A raiz encontrada foi x = ", x1)
         print("f(x) = ", f(x0))
         print("der(x) = ", der(x0))

metodoNewton()
