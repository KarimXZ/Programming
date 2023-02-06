s=str(input("Lutfen string giriniz")).lower().strip()

for i in range(len(s)):
    if s[i]!=s[-(i+1)]:
        print('palindrom degil')
        i=False
        break
    else:
        i=True
if i is True:
    print("palindromdur\n")
    # print(x[i])
    # print(x[-(i+1)])
    # 0,-1
    # 1,-2
    # 2,-3