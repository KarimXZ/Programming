import numpy as np
n = int(input("Kare matrisin boyutu nedir?"))
A = np.empty((n, n))
def getvalues():
    for i in range(n):
        for j in range(n):
            A[i][j]=int(input(f"Lutfen {i} satir {j} sutun giriniz"))
def issymmetric(x):
    for a in range(n):
        for b in range(n):
            if x[a][b]!=x[b][a]:
                Symmetric=False
                break
            else:
                Symmetric=True
    if Symmetric==True:
                print(f"Matrix {x} is symmetric")
    else:
                print(f"Matrix {x} is not symmetric")
getvalues()
issymmetric(A)