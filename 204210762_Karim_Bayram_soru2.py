x=str(input("Lutfen sayi giriniz"))
for i in range(len(x),0,-1):
    print(int(x[-i])*(10**(i-1)))
y=input()