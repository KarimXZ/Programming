from abc import ABC,abstractmethod
#her kitap veya dergi icin alinan sahis var olacak. Bu kisi "taker" adi verilmis
#kod icinde
class Library(ABC):
    booklist=[]
    def __init__(self,taker):
        self.taker=taker
    @abstractmethod
    def checkout(self,name):
        pass
    @abstractmethod
    def bookstatus(self,book):
        pass
    @abstractmethod
    def returnbook(self,name):
        pass
    @classmethod
    def checkall(cls):
        for i in cls.booklist:
            print(f"{i.name},{i.authour}:{i.status}")
#Normalde, kitap kutuphanede var olacak, ve alinan kisi yok.
class Book(Library):
    def __init__(self,name,authour,status='Available' ,taker=''):
        super().__init__(taker)
        self.name=name.lower().strip()
        self.status=status
        self.authour=authour
        self.booklist.append(self)
        self.status='Available'
    def checkout(self, taker):
        if self.status=='Available':
            self.status='Taken'
            print(f'{self.name} cikis yapilmis. 14 gun icinde iade gerekiyor.')
            self.taker=str(taker)
        elif self.status=='Taken':
            print(f"Bu kitap {self.taker} tarafindan alinmis.")
        else:
            print("Bu kitap mevcut degil.")
    def bookstatus(self):
        print(self.status)
    def returnbook(self):
        if self.status=='Taken':
            self.status='Available'
            self.taker=''
            print(f"{self.name} kitab iade edilmis.")
        elif self.status=='Available':
            print("Bu kitap hala kutuphanede")
        else:
            print("Boyle bir kitap yok.")
class Magazine(Library):
    def __init__(self, name,authour,editor,edition,status='Available',taker=''):
        super().__init__(taker)
        self.name=name.lower().strip()
        self.status=status
        self.authour=authour
        self.editor=editor
        self.edition=edition
        self.booklist.append()
        self.status='Available'
    def checkout(self, taker):
        if self.status=='Available':
            self.status='Taken'
            print(f'{self.name} cikis yapilmis. 14 gun icinde iade gerekiyor.')
            self.taker=str(taker)
        elif self.status=='Taken':
            print("Bu dergi {self.taker} tarafindan alinmis.")
        else:
            print("Bu dergi mevcut degil.")
    def bookstatus(self):
        print(self.status)
    def returnbook(self):
        if self.status=='Taken':
            self.status='Available'
            self.taker=''
            print(f"{self.name} dergi iade edilmis.")
        elif self.status=='Available':
            print("Bu dergi hala kutuphanede")
        else:
            print("Boyle bir dergi yok.")
def UI():
    while True:
        n=int(input("""
Kutuphane Otomasyon Uygulamaya Hos geldiniz! Ne yapmak istiyorsun?
1:Kitap eklemek
2:Kitap almak
3:Kitap iade etmek
4:Kitapin durumu getirmek
5:Kitap listesi yazdirmak
6:Cikis yapmak"""))
        if n==1:
            a=input("Kitapin adi nedir?")
            b=input("Kitapin yazari kimdir?")
            c=Book(a, b)
            print(f"{b}'in kitabi {c.name} Kutupaheneye eklenmis")
        elif n==2:
            a = input("Hangi kitap almak istiyorsunuz?").lower().strip()
            b = input("Kim  bu kitap aliyor?")
            for i in Library.booklist:
                if a==i.name:
                    i.checkout(b)
        elif n==3:
            a = input("Hangi kitap iade etmek istiyorsunuz?").lower().strip()
            for i in Library.booklist:
                if a==i.name:
                    i.returnbook()
        elif n==4:
            a = input("Hangi kitapin durumu getirmek istiyorsunuz?").lower().strip()
            for i in Library.booklist:
                if a==i.name:
                    i.bookstatus()
                else:
                    print('Boyle bir kitap yok')
        elif n==5:
            Library.checkall()
        elif n==6:
            print("Goodbye!")
            break
        else:
            print("Hatali giris, lutfen tekrar deneyin")
try:
    UI()
except ValueError:
    print("Sadece sayilar kabul edilirler, tekrar deneyin")
    UI()