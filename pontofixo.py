import math

def f(x):
         return pow(x,2) - math.exp(x)

def g(x):
         return -math.sqrt(math.exp(x))

def metodoPontoFixo():
         # exemplo: x0 = -0.5 e iteracoes = 15
         x0 = float(input("Digite a aproximação inicial x0: "))
         iteracoesMax = int(input("Digite a quantidade de iterações: "))
         tolerancia = float(input('Digite a tolerância desejada: '))
         iteracao = 0
         x1 = 0
         while iteracao < iteracoesMax and math.fabs(g(x0)-x0) > tolerancia:
                  x0 = g(x0)
                  iteracao += 1
         if iteracao == iteracoesMax:
             print('Número máximo de iterações atingido!')
         print('Iterações realizadas:', iteracao)
         print("A raiz encontrada foi x = ", x1)
         print("f(x) = ", f(x1)) #número próximo de 0 ou o próprio 0
         print("g(x) = ", x1) #número próximo da raiz, ou a própria raiz

metodoPontoFixo()
