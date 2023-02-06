s=str(input("Lutfen sayinin giriniz"))
for i in range(len(s)):
    print(int(s[i]))
j=0
for i in range(len(s)):
    j=j+int(s[i])
print(f"Toplam:{j}")