faktordict={}
while True:
    try:
        x = int(input("Lutfen 0-100 tam sayi girininz:\n"));
        if x>0 and x<=100:
            break;
        else:
            print("Sayinin degeri hatalidir, lutfen tekar deneyin");
    except ValueError:
        print("Sayi bulunmadi, lutfen tekrar deneyin");
for i in range(1,x+1):
    if x%i== 0:
        faktordict[i]=int(x/i);
    else:
        continue;
for i in faktordict.items():
    print(i);
print(f"{len(faktordict)} farkli carplar bulunmustur");