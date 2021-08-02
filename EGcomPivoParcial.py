import numpy as np
import time

'''
exemplo qualquer
A = np.array(
    [
        [1, 2, -1],
        [2, -1, 1],
        [1, 1, 1],
    ]
)
b = np.array(
    [2, 3, 6]
)'''
inicio = time.time()
#exemplo 4-c
A = np.array(
    [
        [2, -1, 0, 0],
        [-1, 2, -1, 0],
        [0, -1, 2, -1],
        [0, 0, -1, 2],
    ]
)
b = np.array(
    [1, 0, 0, 0]
)
n = len(b)
x = np.zeros(n)
custo = 0
for k in range(n-1):
    if abs(A[k,k]) < 1.0e-12:
        for i in range(k+1, n):
            if abs(A[i,k]) > abs(a[k,k]):
                A[[k,i]] = A[[i,k]]
                b[[k,i]] = b[[i,k]]
                break
    for i in range(k+1, n):
        if A[i,k] == 0: continue
        multiplicador = A[k,k]/A[i,k]
        for j in range(k,n):
            A[i,j] = A[k,j] - A[i,j]*multiplicador
        b[i] = b[k] - b[i]*multiplicador
'''print('A:')
print(A)
print('B:')
print(b)'''

x[n-1] = b[n-1]/A[n-1, n-1]
for i in range(n-2, -1, -1):
    soma = 0
    for j in range(i+1, n):
        soma += A[i,j]*x[j]
    x[i] = (b[i]-soma) / A[i,i]

print('Resultado:')
print(x)
fim = time.time()
print(fim-inicio)
