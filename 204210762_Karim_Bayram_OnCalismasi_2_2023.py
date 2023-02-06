import numpy;
x1=0
Arow = int(input("Lutfen 1nci matrisin satiri giriniz"))
Acolumn = int(input("Lutfen 1nci matrisin sutunu giriniz"))
Brow=Acolumn;
print(f"Matris carpimi icin 2inci matris icin {Acolumn} satir gerekiyor")
Bcolumn = int(input("\nLutfen 2nci matrisin sutunu giriniz"))
A=numpy.empty([Arow,Acolumn],int);
B=numpy.empty([Brow,Bcolumn],int);
C=numpy.zeros([Arow,Acolumn],int);
for i in range(Arow):
    for j in range(Acolumn):
        A[i][j]=int(input(f"Lutfen 1nci matrisin {i+1}nci satir {j+1}sutun giriniz"))
for i in range(Brow):
    for j in range(Bcolumn):
        B[i][j]=int(input(f"Lutfen 2nci matrisin {i+1}nci satir {j+1}sutun giriniz"))
C=numpy.matmul(A,B);
#Matris carpma metod var numpy icinde
print("Matris 1:")
print(A);
print('Matris 2:');
print(B);
print('Sonuc:');
print(C);