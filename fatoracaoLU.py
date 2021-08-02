import numpy as np

A = np.array(
    [
        [3.0, -4.0, 1.0],
        [1.0, 2.0, 2.0],
        [4.0, 0.0, -3.0]
    ]
)
b = np.array(
    [9.0, 3.0, -2.0]
)

def fatoraLU(A):
    U = np.copy(A)
    n = np.shape(U)[0]
    L = np.eye(n)
    for j in np.arange(n-1):
        for i in np.arange(j+1,n):
            L[i,j] = U[i,j]/U[j,j]
            for k in np.arange(j+1,n):
                U[i,k] = U[i,k] - L[i,j]*U[j,k]
            U[i,j] = 0
    return L, U

def resolveSistema(L, U, b):
    L = np.array(L, float)
    U = np.array(U, float)
    b = np.array(b, float)
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)

    # Triangular inferior
    for i in range(n):
        y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]

    # Triangular superior
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(U[i, i + 1:n] * x[i + 1:n])) / U[i, i]

    # solução
    return x

(L,U) = fatoraLU(A)
print('L')
print(L)
print('U')
print(U)

x = resolveSistema(L, U, b)
print('Resultado:')
print(x)
