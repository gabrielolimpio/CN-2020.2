import numpy as np

A = np.array(
    [
        [3, 1],
        [2, 5]
    ]
)

b = np.array(
    [2, -3]
)

solucao = np.zeros(len(b))

def gaussJacobi(A, b, solucao, iter):
    iteracoes = 0
    aux = np.zeros(len(solucao))
    while iteracoes < iter:
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i,j]*solucao[j]
            x /= A[i,i]
            aux[i] = x
        iteracoes += 1

        for l in range(len(aux)):
            solucao[l] = aux[l]
    print(solucao)

gaussJacobi(A, b, solucao, 30)
