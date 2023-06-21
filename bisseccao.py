import math
def f(x):
    return (x**3-3*x**2-6*x+8)

# testando gitkraken
#Algoritmo retirado do livro Algoritmos numéricos Frederico Ferreira
def bisseccao(a, b, Toler, IterMax):
    Fa = f(a)
    Fb = f(b)
    if(Fa*Fb > 0):
        print('Função não muda de sinal nos extremos do intervalo dado')
        return
    DeltaX = abs(b-a)/2
    Iter = 0

    print(f"Interações {'':5} a {'':13} b {'':13} x {'':13} Fx {'':9} delta_x")
    while(1):
        Iter = Iter+1
        x = (a+b)/2
        Fx = f(x)
        #Método de formatação f-strings: adiciona o f antes das aspas e coloca as variáveis entre chaves
        print(f"{Iter:5}{a:16.5f}{b:16.5f}{x:16.5f}{Fx:16.5f}{DeltaX:16.5f}")
        if(DeltaX < Toler and abs(Fx) < Toler or Iter >= IterMax):
            break
        if(Fa * Fx > 0):
            a = x
            Fa = Fx
        else:
            b = x
        DeltaX = DeltaX/2
    Raiz = x
    if(DeltaX < Toler and abs(Fx) < Toler):
        Erro = 0
    else:
        Erro = 1

    print(f"\nRaiz = {Raiz:.5f}")
    print(f"Iter = {Iter}")
    print(f"Erro = {Erro}")

a = -3.83
b = -0.62
Toler = 0.05
IterMax = 20

bisseccao(a, b, Toler, IterMax)


