n=int(input("Lutfen Sayi giriniz:\n"))
carp=[]
for i in range(1,n+1):
    if n%i==0:
        carp.append(i)
    else:
        continue
print(f"Carpanlari:{carp}")