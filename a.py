import random
from abc import ABC,abstractmethod
class Food(ABC):
    Listlist=[]
    foodordered=[]
    debt=0
    def __init__(self,name, price):
        self.name=name
        self.price=price
        self.foodid=None
    def order(self):
        setattr(Food, 'debt', self.debt+self.price)
        print(f"The guests debt is: {Food.debt}. Yemegin Fiyati:{self.price}")
        self.foodordered.append(self)
    @abstractmethod
    def AssignID():
        pass
    @staticmethod
    def totalfoodprice():
        Totalprice=0
        for i in Food.foodordered:
            Totalprice=Totalprice+i.price
        print(f"Toplam Fiyat:{Totalprice}.")
        input()
    @abstractmethod
    def AddList():
        pass


class Soup(Food):
    Souplist=[]
    def __init__(self, name, price):
        super().__init__(name, price)
        Soup.Souplist.append(self)
    def AddList():
        Food.Listlist.append(Soup.SoupList)
    def AssignID():
        j=1
        for i in Soup.Souplist:
            setattr(i, 'foodid', j)
            j=j+1
class Main(Food):
    Mainlist=[]
    def __init__(self, name, price):
        super().__init__(name, price)
        Main.Mainlist.append(self)
    def AddList():
        Food.Listlist.append(Main.Mainlist)
    def AssignID():
        j=1
        for i in Main.Mainlist:
            setattr(i, 'foodid', j)
            j=j+1
class Sweets(Food):
    Sweetlist=[]
    def __init__(self, name, price):
        super().__init__(name, price)
        Sweets.Sweetlist.append(self)
    def AddList():
        Food.Listlist.append(Sweets.Sweetlist)
    def AssignID():
        j=1
        for i in Sweets.Sweetlist:
            setattr(i, 'foodid', j)
            j=j+1
class Drinks(Food):
    Drinklist=[]
    def __init__(self, name, price):
        super().__init__(name, price)
        Drinks.Drinklist.append(self)
    def AddList():
        Food.Listlist.append(Drinks.DrinkList)
    def AssignID():
        j=1
        for i in Drinks.Drinklist:
            setattr(i, 'foodid', j)
            j=j+1
def RestaurantUI():
    a=1
    Soup.AssignID()
    Main.AssignID()
    Sweets.AssignID()
    Drinks.AssignID()
    while True:
        x=input("""
        ---Restorant Hizmetine Hosgeldiniz---
        Ne Istersiniz?:
        1-Yemek Al
        2-Ana Menuye Don""")
        if x=='1':
            while a==1:
                for i in Soup.Souplist:
                    print((f'{i.foodid}-{i.name}    Fiyat: {i.price}'))
                y=int(input("Hangi Corbayi Istersiniz?(Devam etmek icin 0 a basiniz)"))
                if y==0:
                    break
                for i in Soup.Souplist:
                    if i.foodid==y:
                        i.order()
                        a=input("Baska Corba Ister misiniz? evet/hayir")
                        if a=='evet':
                            a=1
                        else:
                            a=2
            while a==2:
                for i in Main.Mainlist:
                    print((f'{i.foodid}-{i.name}    Fiyat: {i.price}'))
                y=int(input("Ana Yemek Olarak Ne Istersiniz ?(Devam etmek icin 0 a basiniz)"))
                if y==0:
                    break
                for i in Main.Mainlist:
                    if i.foodid==y:
                        i.order()
                        a=input("Baska Ana Yemek Ister misiniz? evet/hayir")
                        if a=='evet':
                            a=2
                        else:
                            a=3
            while a==3:
                for i in Sweets.Sweetlist:
                    print((f'{i.foodid}-{i.name}-Fiyat {i.price}'))
                y=int(input("Hangi Tatliyi Istersiniz?(Devam etmek icin 0 a basiniz)"))
                if y==0:
                    break
                for i in Sweets.Sweetlist:
                    if i.foodid==y:
                        i.order()
                        a=input("Baska Bir Tatli Ister misiniz? evet/hayir")
                        if a=='evet':
                            a=3
                        else:
                            a=4
            while a==4:
                for i in Drinks.Drinklist:
                    print((f'{i.foodid}-{i.name}    Fiyat: {i.price}'))
                y=int(input("Hangi icecegi istersiniz?(Devam etmek icin 0 a basiniz)"))
                if y==0:
                    break
                for i in Drinks.Drinklist:
                    if i.foodid==y:
                        i.order()
                        a=input("Baska Icecek Ister misiniz?evet/hayir")
                        if a=='y':
                            a=4
                        else:
                            a=5
            Food.totalfoodprice()
        if x=='2':
            menu()
#Çorbalar
Domates=Soup('Domates Çorbası', 10)
Mercimek=Soup('Mercimek Çorbası', 10)
Yayla=Soup('Yayla Çorbası', 10)
İşkembe=Soup('İşkembe Çorbası', 10)
Kellepaça=Soup('Kelle Paça Çorbası', 10)
Şehriye=Soup('Şehriye Çorbası', 10)
Tavuk=Soup('Tavuk Çorbası', 10)
Düğün=Soup('Düğün Çorbası', 10)
Ezogelin=Soup('Ezogelin Çorbası', 10)
Mantar=Soup('Mantar Çorbası', 10)
Un=Soup('Un Çorbası', 10)
Tarhana=Soup('Tarhana Çorbası', 10)
#Ana Yemekler
Steak=Main('Steak Et',400)
Lahmacun=Main('Lahmacun',30)
AdanaKebap=Main('Adana Kebap',70)
Köfte=Main('Ekmek Arası Köfte',64)
Sucuk=Main('Ekmek Arası Sucuk',45)
Köfte2=Main('Porsiyon Köfte',100)
Sucuk2=Main('Porsiyon Sucuk',80)
Tavuk=Main('Ekmek Arası Tavuk',30)
Tavuk2=Main('Porsiyon Tavuk',75)
Makarna=Main('Sade Makarna',30)
Makarna2=Main('Yoğrutlu Makarna',34)
Makarna3=Main('Salçalı Makarna',40)
Makarna4=Main('Kremalı Mantarlı Makarna',50)
Makarna5=Main('Beşamel Soslu Makarna',60)
Makarna6=Main('Tavuklu Makarna',60)
Makarna7=Main('Köfteli Makarna',65)
Beyti=Main('Beyti',70)
İskender=Main('İskender',100)
BuguKebabı=Main('Buğu Kebabı',92)
Mantı=Main('Mantı',100)
SögurmeKebabı=Main('Söğürme Kebabı',120)
Suluköfte=Main('Sulu Köfte',70)
Kızartma=Main('Karışık Kızartma',40)
ArapTava=Main('Arap Tava',130)
SultanKebabı=Main('Sultan Kebabı',110)
Hamburger=Main('Hamburger',50)
Pizza=Main('Pizza',70)
Imambayıldı=Main('İmambayıldı',90)
Mücver=Main('Mücver',62)
Karnıyarık=Main('Karnıyarık',90)
Dolma=Main('Zeytin Yağlı Sarma',70)
Dolma2=Main('Biber Dolması',0)
Dolma3=Main('Patlıcan Dolması',60)
#Tatlılar
Dondurma=Sweets('Dondurma', 10)
Baklava=Sweets('Baklava', 80)
Tulumba=Sweets('Tulumba', 100)
SogukBaklava=Sweets('SogukBaklava', 100)
Sekerpare=Sweets('Sekerpare', 100)
Trilece=Sweets('Trilece', 100)
Icecream=Sweets('Icecream', 100)
Icecream=Sweets('Icecream', 100)
Icecream=Sweets('Icecream', 100)
#İçecekler
Redbull=Drinks('Redbull', 20)
Cola=Drinks('Coca Cola', 12)
Fanta=Drinks('Fanta', 10)
Elmasuyu=Drinks('Elma Suyu', 7)
Vişnesuyu=Drinks('Vişne Suyu', 7)
Seftali=Drinks('Şeftali Suyu', 7)
Portakal=Drinks('Portakal Su', 7)
Karışık=Drinks('Karışık Meyvve Suyu', 7)
Sogukcay=Drinks('Lipton Ice Tea Şeftali', 15)
Sogukcay1=Drinks('Lipton Ice Tea Limonlu', 15)
Sogukcay2=Drinks('Lipton Ice Tea Egzotik Meyveli', 15)
Sogukcay3=Drinks('Lipton Ice Tea Çilek-Karpuzlu', 15)
Sogukcay4=Drinks('Lipton Ice Tea Kavun-Çilekli', 15)
Gazoz=Drinks('Gazoz', 10)
Madensuyu=Drinks('Maden Suyu', 12)
Fanta=Drinks('Fanta', 10)
Elmasuyu=Drinks('Elma Suyu', 7)
Vişnesuyu=Drinks('Vişne Suyu', 7)
Seftali=Drinks('Şeftali Suyu', 7)
Portakal=Drinks('Portakal Su', 7)
def menu():
    x = int(input("""
    ---Python Hotel'e Hosgeldiniz---
    1-Oda Servisleri
    2-Restorant hizmetleri
    3-Tamirat
    4-Ek Hizmetler
    """))

    if x == 1:
        odaHizmetleri()
    elif x == 2:
        RestaurantUI()
    elif x == 3:
        tamirat()
    elif x == 4:
        ekHizmetler()



def odaHizmetleri():
    x = int(input("""
    ---Oda Hizmetleri Menusune Hosgeldiniz---

    1- Oda Temizligi
    2- Havlu Degisimi
    3- Lavabo Temizligi
    4- Sabun ve Sampuan Degisimi 
    5- Buzdolabi Dolumu
    0- Ana Menuye Don
    """))

    if x == 1:
       print("""
       ---Talebiniz Alinmistir---
       Tahmini Temizlik Suresi: 1 Saat
       """)
       odaHizmetleri()
    elif x == 2:
        print("""
        ---Talebiniz Alinmistir---
        Tahmini Degisim Suresi: 30 Dakika
        """)
        odaHizmetleri()
    elif x == 3:
        print("""
        ---Talebiniz Alinmistir---
        Tahmini Temizlik Suresi: 1 Saat
        """)
        odaHizmetleri()
    elif x == 4:
        print("""
        ---Talebiniz Alinmistir---
        Tahmini Degisim Suresi: 30 Dakika
        """)
        odaHizmetleri()
    elif x == 5:
        print("""
        ---Talebiniz Alinmistir---
        Tahmini Degisim Suresi: 30 Dakika
       """)
        odaHizmetleri()
    else:
        print("""
            ---Ana Menüye Gönderiliyorsunuz---
            """)
        menu()

def ekHizmetler():
    x = int(input("""
    ---Ek Hizmetler Menusüne Hoşgeldiniz---
    
    1- Havuz Hizmeti
    2- Sauna Hizmeti
    3- Spa Hizmeti
    4- Masaj Hizmeti
    5- Bar Hizmeti
    0- Ana Menuye Don
    """))
    if x == 1:
        pword = random.randint(1000,10000)
        print(f"""
        ---Havuz Hizmeti---

        Havuz hizmeti icin size ozel kodunuz:{pword}
        """)
        ekHizmetler()
    elif x == 2:
        pword = random.randint(1000,10000)
        print(f"""
        ---Sauna Hizmeti---

        Sauna hizmeti icin size ozel kodunuz:{pword}
        """)
        ekHizmetler()
    elif x == 3:
        pword = random.randint(1000,10000)
        print(f"""
        ---Spa Hizmeti---

        Spa hizmeti icin size ozel kodunuz:{pword}
        """)
        ekHizmetler()
    elif x == 4:
        pword = random.randint(1000,10000)
        print(f"""
        ---Masaj Hizmeti---

        Masaj hizmeti icin size ozel kodunuz:{pword}
        """)
        ekHizmetler()
    elif x == 5:
        pword = random.randint(1000,10000)
        print(f"""
        ---Bar Hizmeti---

        Bar hizmeti icin size ozel kodunuz:{pword}
        """)
        ekHizmetler()
    else:
        print("""
            ---Ana Menüye Gönderiliyorsunuz---
            """)
        menu()



def tamirat():
    x = int(input("""
    ---Tamirat Menusüne Hoşgeldiniz---

    1-Elektrik Tesisatı Onarımı
    2-Su Tesisatı Onarımı
    3-Mobilya Onarımı
    4-Ana Menüye Dön
    """))
    
    if x == 1:
        y = int(input("""
        ---Elektrik Tesisat Onarımına Hoşgeldiniz---
        1-Lamba Onarımmı
        2-Klima Onarımı
        3-Elektronik Cihaz Onarımı
        4-Televizyon Onarımı
        5-Buzdolabı Onarımı
        0-Tamirat Menusune Dön
        """))
        if y==1:
            print("""
           ---Lamba Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 15-20 dakika
            """)
            tamirat()
        elif y==2:
            print("""
            ---Klima Onarımı Talebiniz Alınmıştır---
            Onarım İçin Bir Görevli Atanmıştır
            Tahmini Onarım Süresi: 1-2 saat
            """)
            tamirat()
        elif y==3:
            print("""
            --- Elektronik Cihaz Onarımı Talebiniz Alınmıştır---
            Onarım İçin Bir Görevli Atanmıştır
            Tahmini Onarım Süresi: 1-2 saat
            """)
            tamirat()
        elif y==4:
            print("""
            ---Televizyon Onarım Talebiniz Alınmıştır---
            Onarım İçin Bir Görevli Atanmıştır
            Tahmini Onarım Süresi: 2-3 saat
            """)
            tamirat()
        elif y==5:
            print("""
            ---Buz Dolabı Onarımı Talebiniz Alınmıştır---
            Onarım İçin Bir Görevli Atanmıştır
            Tahmini Onarım Süresi: 3-4 saat
            """)
            tamirat()
        else:
            print("""
            ---Tamirat Menusune Gönderiliyorsunuz---
            """)
            tamirat()
        
    elif x == 2:
        y = int(input("""
        ---Su Tesisat Onarımına Hoşgeldiniz---
        1-Duş Onarımmı
        2-Lavabo Onarımı
        3-Tuvalet Onarımı
        0-Tamirat menusune Don
        """))

        if y==1:
            print("""
           ---Duş Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 2-3 saat
           """)
            tamirat()
        elif y==2:
            print("""
            ---Lavabo Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 1-2 saat
           """)
            tamirat()
        elif y==3:
            print("""
            ---Tuvalet Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 1-2 saat
           """)
            tamirat()

        else:
            print("""
            ---Tamirat Menusune Gönderiliyorsunuz---
            """)
            tamirat()
                
    elif x == 3:
        y = int(input("""
        ---Mobilya Onarımına Hoşgeldiniz---
        1-Yatak Onarımmı
        2-Koltup Onarımı
        3-Dolap Onarımı
        4-Çalışma Masası Onarımı
        5-Komodin Onarımı
        0-Tamirat menusune Don
        """))
        
        if y==1:
            print("""
            ---Yatak Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 30-40 dakika
            """)
            tamirat()
        elif y==2:
            print("""
            ---Koltuk Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 2-3 saat
            """)
            tamirat()
        elif y==3:
            print("""
            ---Dolap Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 2-3 saat
            """)
            tamirat()
        elif y==4:
            print("""
            ---Çalışma Masası Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 1-2 saat
            """)
            tamirat()
        elif y==5:
            print("""
            ---Komodin Onarımı Talebiniz Alınmıştır---
           Onarım İçin Bir Görevli Atanmıştır
           Tahmini Onarım Süresi: 1-2 saat
            """)
            tamirat()
        else:
            print("""
            ---Tamirat Menusune Gönderiliyorsunuz---
            """)
            tamirat()
    else:
         print("""
            ---Ana Menüye Yönlendiriliyorsunuz---
            """)
         menu()
menu()

