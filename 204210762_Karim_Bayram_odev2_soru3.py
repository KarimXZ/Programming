try:
    spaces=[]
    x=int(input("How many spaces do you want?"))
    for i in range(x):
        spaces.append(i+1)
    for i in spaces:
        print(i)
    
    while True:
        y=int(input('Reservazyon yapmak icin lutfen sayi giriniz. Cikis icin -1 giriniz'))
        if y in spaces:
            spaces.remove(y)
            for i in spaces:
                print(i)
        elif y==-1:
            break
        else:
            print("hatali giris, lutfen tekrar deneyin")
except ValueError:
    print("biz sayi istiyoruz, lutfen harflari girmeniz")
