
def getchar():
    while True:
        global x;
        flagc=True;
        x=input("\nLutfen A,B,C den 3 karaktor seciniz");
        listc=['A','B','C']
        for i in x:
            if i not in listc:
                flagc=False;
        if len(x)!=3 or flagc==False:
            print("Hatali giris, lutfen tekrar deneyin");
        else:
            break
def printA():
    print("""
           *
          * *
         *****
         *   *
         *   *""",end="");
def printB():
    print("""
         ****
         *   *
         ****
         *   *
         ****""",end="");
def printC():
    print("""
         ******
         *
         *
         *
         ******""",end="");
def pickchar():
    for i in x:
        if i=='A':
            printA();
        elif i=='B':
            printB();
        elif i=='C':
            printC();
getchar()
pickchar()