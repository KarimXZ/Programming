import random as rd;
rd.seed()
#matrix yapmak
def randomMatrix(M,N):
    matrix =[[rd.randint(0,10) for j in range(M)] for i in range(N)]
    return matrix
BizimMatrix=randomMatrix(3, 3)
print(BizimMatrix)
#bir boyutlu matrixe baglamak
k=[]
for i in BizimMatrix:
    for j in i:
        k.append(j)
print(k)
#En buyuk sayi bulmak
x=0
for i in BizimMatrix:
    for j in range(len(i)):
        if i[j]>x:
            x=i[j]
        else:
            pass
print(x)
#En kucuk sayi bulmak
y=100
for i in range(len(k)):
    if k[i]<y:
        y=k[i]
    else:
        pass
print(y)
#Sayilar degistirmek
for i in range(len(k)):
    if k[i]==y:
        k[i]=x;
    else:
        pass
print(k)