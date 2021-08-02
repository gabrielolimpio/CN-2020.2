import numpy as np
import time

inicio = time.time()
A = np.array(
    [
        [2, -1, 0, 0],
        [-1, 2, -1, 0],
        [0, -1, 2, -1],
        [0, 0, -1, 2],
    ]
,float)
b = np.array(
    [1, 0, 0, 0]
,float)

n = len(A)
for k in range(0, n-1):
    for i in range(k+1, n):
        if A[i,k] != 0.0:
            p = A[i,k]/A[k,k]
            A[i, k+1:n] -= p*A[k, k+1:n]
            b[i] -= p*b[k]
for k in range(n-1, -1, -1):
    b[k] = (b[k] - np.dot(A[k,k+1:n],b[k+1:n]))/A[k,k]

print(b)
fim = time.time()
print(fim-inicio)

