#Tercume:
#Urun=Product
#budget=sermaye
#buy/sell=alis/satis
#amount=tutar
class Product:
    def __init__(self,name,price,amount):
        self.name=name
        self.price=price
        self.amount=amount
    def sell(self,sellamount):
        Mybudget.quantity=Mybudget.quantity+(int(self.price)*sellamount)
        self.amount=int(self.amount)-sellamount
        transactions.append(f"{sellamount}'tane {self.name} satilmis. {int(self.price)*sellamount} lira alinmis")
#Urunler ucretsiz degil, alirken sermaye azalacak.
    def buy(self,buyamount,buyprice):
        Mybudget.quantity=Mybudget.quantity-(buyprice*buyamount)
        self.amount=int(self.amount)+buyamount
        transactions.append(f"{buyamount}'tane {self.name} alinmis. {buyprice*buyamount} lira odenmis")
class Budget:
    def __init__(self,quantity=0):
        self.quantity=quantity
    def add(self,add):
        self.quantity=+add
        transactions.append(f"Sermayeye {add} lira eklenmis. Yeni Sermaye:{self.quantity}")
transactions=[]
Productlist=[]
Mybudget=Budget()
def Interface():
    while True:
        ui=int(input("""\nMini-ekonomik-sim'e hos geldiniz! 
                 1:Yeni urun tipi eklemek
                 2:Urunler satmak
                 3:Urunler almak
                 4:Sermaye eklemek
                 5:Stok getirmek
                 6:Sermaye durumu denetlemek
                 7:Cikmak\n"""))
        if ui == 1:
            nam=input("Urunun adi nedir?")
            pri=input("Urunun satis fiyati nedir?")
            qua=input("Stokta kac urun var?")
            prod=Product(nam, pri,qua)
            Productlist.append(prod)
        elif ui==2:
            for i in range(len(Productlist)):
                print(f"{i+1}-{Productlist[i].name}:{Productlist[i].amount}\n")
            id=int(input("Hangi urun satacaksiniz?\n"))
            sellqua=int(input("Kactane satacaksiniz?\n"))
            Productlist[id-1].sell(sellqua)
        elif ui==3:
            for i in range(len(Productlist)):
                print(f"{i+1}-{Productlist[i].name}:{Productlist[i].amount}\n")
            id=int(input("Hangi urun alacaksiniz?\n"))
            buyqua=int(input("Kactane alacaksiniz?\n"))
            buypri=int(input("Bu urunun alis fiyati ne kadar?\n"))
            Productlist[id-1].buy(buyqua,buypri)
        elif ui==4:
            budadd=int(input("Ne kadar sermayeye ekleyecek misiniz?\n"))
            Mybudget.add(budadd)
        elif ui==5:
            for i in range(len(Productlist)):
                print(f"{i+1}-{Productlist[i].name}:{Productlist[i].amount}\n")
        elif ui==6:
            for i in range(len(transactions)):
                print(transactions[i])
            print(f'Sermaye:{Mybudget.quantity}')
        elif ui==7:
            input("Tessekur ederim!")
            break
        else:
            input("Hatali giris, lutfen tekrar deneyin")
            
Interface()
