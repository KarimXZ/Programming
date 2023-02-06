import numpy;
size=int(input("Lutfen matrisin boyutu giriniz"));
matrix1 = numpy.empty((size,size));
for i in range(size):
    for j in range(size):
        matrix1[i][j]=int(input(f"Lutfen matrisin {i}'inci satir {j}inci sutunun degeri giriniz lutfen"));
print("Dizi:");
for i in range(size):
    print();
    for j in range(size):
        print(f'{int(matrix1[i][j])} ',end='');
if matrix1[i][j]==matrix1[j][i]:
    print("\nMatrix simetriktir");
else:
    print("\nMatrix simmetrik degil");
input()