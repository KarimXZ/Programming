import numpy as np;
size=int(input("Ne kadar buyuk?"))
if size%2==0:
    size=size+1
y=size+1
def Diamond(x):
    if x<-y:
        print('End')
    elif x>0:
        print(' '*(x//2)+'#'*(y-x))
        return Diamond(x-2)
    elif x<0 and x>-y:
        print(' '*(abs(x)//2)+'#'*(y-np.abs(x)))
        return Diamond(x-2)
Diamond(size)
#Odevin sekile almak icin 9 kullanin
#Fonksiyon tek olursa calismayacak, Fonkisyonun disinda olan sabit bir sayi gerekiyor.
#Tek Fonksiyon asagida:

# def Diamond9(x):
#     if x<-10:
#         print('End')
#     elif x>0:
#         print(' '*(x//2)+'#'*(10-x))
#         return Diamond9(x-2)
#     elif x<0 and x>-10:
#         print(' '*(abs(x)//2)+'#'*(10-np.abs(x)))
#         return Diamond9(x-2)
# Diamond9(9)