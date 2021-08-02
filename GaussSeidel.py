import numpy as np

''' ex25
A = np.array(
    [
        [2, 5],
        [3, 1]

    ]
)

b = np.array(
    [2, -3]
)'''
''' ex22
A = np.array(
    [
        [10, 1, 1],
        [1, 10, 1],
        [1, 1, 10]

    ]
)

b = np.array(
    [12, 12, 12]
)
'''
A = np.array(
    [
        [4, -1, 0, 0],
        [-1, 4, -1, 0],
        [0, -1, 4, -1],
        [0, 0, -1, 4]

    ]
)

b = np.array(
    [1, 1, 1, 1]
)

solucao = np.zeros(len(b))

def gaussJacobi(A, b, solucao, iter):
    iteracoes = 0
    while iteracoes < iter:
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i,j]*solucao[j]
            x /= A[i,i]
            solucao[i] = x
        iteracoes += 1

    print(solucao)

gaussJacobi(A, b, solucao, 30)
