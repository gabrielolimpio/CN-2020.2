import numpy as np
def cholesky(M):
    #A função retorna a variante triangular inferior L (Lower)
    n = len(M) # n recebe o tamanho da matriz
    L = np.zeros((n,n)) #inicializa a matriz com zeros

    #decomposição
    for i in range(n):
        for k in range(i+1):
            #função sum soma todos os elementos de j até k
            soma = sum(L[i,j] * L[k,j] for j in range(k))
            if (i==k):
                L[i,k] = np.sqrt(M[i,i] - soma)
            else:
                L[i,k] = (1. / L[k,k] * (M[i,k] - soma))

    return L

def resolveSistema(G, G_T, b):
    G = np.array(G, float)
    G_T = np.array(G_T, float) # G transposta
    b = np.array(b, float)
    n = len(G)
    y = np.zeros(n)
    x = np.zeros(n)

    # Triangular inferior
    for i in range(n):
        y[i] = (b[i] - np.sum(G[i, :i] * y[:i]))/G[i,i]

    # Triangular superior
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.sum(G_T[i, i+1:n] * x[i+1:n]))/G_T[i,i]

    #solução
    return x

 #ex33
A = np.array(
    [
        [20.0, 7.0, 9.0],
        [7.0, 30.0, 8.0],
        [9.0, 8.0, 30.0],
    ]
)

b = np.array(
        [16.0, 38.0, 38.0]
)
'''A = np.array(
    [
        [16.0, 4.0, 8.0, 4.0],
        [4.0, 10.0, 8.0, 4.0],
        [8.0, 8.0, 12.0, 10.0],
        [4.0, 4.0, 10.0, 12.0]
    ]
)

b = np.array(
        [32.0, 26.0, 38.0, 30.0]
)'''
#x = np.linalg.eigvals(A)
#print('Autovalores')
#print(x)
r = cholesky(A)
L_T = np.transpose(r)
x = resolveSistema(r, L_T, b)
print('A: ')
print(A)
print('G: ')
print(r)
print('G tranposta: ')
print(L_T)
print('Resultado: ')
print(x)
