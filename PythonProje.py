from abc import ABC, abstractmethod
from datetime import date
class Hastane(ABC):
    kat=[1,2,3,4,5,6]
    def __init__(self,ad,soyad,cinsiyet,tcno,baslamazamani):
        self.__ad=ad
        self.__soyad=soyad
        self.__cinsiyet=cinsiyet
        self.__tcno=tcno
        self.__baslamazamani=baslamazamani  
#Kapsüllü özelliklere erişim sağlar__.        
    @property
    def ad(self):
        return self.__ad
    @property
    def soyad(self):
        return self.__soyad
    @property
    def cinsiyet(self):
        return self.__cinsiyet
    @property
    def tcno(self):
        return self.__tcno
    @property
    def baslamazamani(self):
        return self.__baslamazamani   
#Kapsüllü özelliklerin değişmesini sağlar__.    
    @property
    def set_ad(self,new):
        self.__ad=new
    @property
    def set_soyad(self,new):
        self.__soyad=new
    @property
    def set_cinsiyet(self,new):
        self.__cinsiyet=new
    @property
    def set_tcno(self,new):
        self.__tcno=new
    @property
    def set_baslamazamani(self,new):
        self.__baslamazamani=new
        
    @classmethod
    def yeniKatEkle(cls):
        cls.__kat.append(cls.__kat[-1]+1)
    
    @classmethod
    def katlariListele(cls):
        for i in cls.__kat:
            print(i)
    
    @staticmethod
    def mesaj():
        print('Hastanemize hoşgeldiniz__.')
        
    @staticmethod
    def mesaj2():
        print('Geçmiş olsun__. Acil şifalar dileriz__.')
    
    
#1.Base Class --> Çalışanlar Class'ı 
class Calisanlar(Hastane):
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas):
        self.__zam=zam
        self.__maas=maas
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani)
    
    @property
    def ad(self):
        return self.__ad
    @property
    def soyad(self):
        return self.__soyad
    @property
    def cinsiyet(self):
        return self.__cinsiyet
    @property
    def tcno(self):
        return self.__tcno
    @property
    def baslamazamani(self):
        return self.__baslamazamani
    @property
    def zam(self):
        return self.__zam
    @property
    def maas(self):
        return self.__maas

    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
      
    def set_zam(self,new):
        self.zam=new
        
    def set_maas(self,new):
        self.maas=new
    
    def set_baslamazamani(self,new):
        self.baslamazamani=new
        

#Doktor Class'ı Çalışanlar Class'ından miras alır. (1.Base Class'ın 1.Child Class'ı)
class Doktor(Calisanlar):
    
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas, poliklinik):
        self.__poliklinik=poliklinik
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas)
        
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_zam(self):
        return self.zam
    
    def get_maas(self):
        return self.maas
    
    def get_poliklinik(self):
        return self.__poliklinik
    
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
      
    def set_zam(self,new):
        self.zam=new
        
    def set_maas(self,new):
        self.maas=new
    
    def set_baslamazamani(self,new):
        self.baslamazamani=new
    
    def set_poliklinik(self,new):
        self.__poliklinik=new
        

#Hemşire Class'ı Çalışanlar Class'ından miras alır. (1.Base Class'ın 2.Child Class'ı)
class Hemsire(Calisanlar):
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas,poliklinik):
        self.__poliklinik=poliklinik
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas)
    
    #Get metodlarımız
    
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_zam(self):
        return self.zam
    
    def get_maas(self):
        return self.maas
    
    def get_poliklinik(self):
        return self.__poliklinik
    #Set metodalarımız
        
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
      
    def set_zam(self,new):
        self.zam=new
        
    def set_maas(self,new):
        self.maas=new
    
    def set_baslamazamani(self,new):
        self.baslamazamani=new
        
    def set_poliklinik(self,new):
        self.__poliklinik=new
        
#Güvenlik Class'ı Çalışanlar Class'ından miras alır. (1.Base Class'ın 3.Child Class'ı)
class Guvenlik(Calisanlar):
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas, guvenlikEgitimi,atesleyiciYeterlilikNotu):#güvenlik için hangi kapıda çalıştığını yazabilirz
        self.__guvenlikEgitimi=guvenlikEgitimi
        self.__atesleyiciYeterlilikNotu=atesleyiciYeterlilikNotu
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas)
    
    #Get metodları
    def get_guvenlikEgitimi(self):
        return self.__guvenlikEgitimi
    
    def get_atesleyiciYeterlilikNotu(self):
        return self.__atesleyiciYeterlilikNotu
    
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_zam(self):
        return self.zam
    
    def get_maas(self):
        return self.maas
    
    #Set metodları
    
    def set_guvenlikEgitimi(self,new):
        self.__guvenlikEgitimi=new
    
    def set_atesleyiciYeterlilikNotu(self,new):
        self.__atesleyiciYeterlilikNotu=new
    
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
      
    def set_zam(self,new):
        self.zam=new
        
    def set_maas(self,new):
        self.maas=new
    
    def set_baslamazamani(self,new):
        self.baslamazamani=new
    
#HastanePolisi Class'ı Çalışanlar Class'ından miras alır. (1.Base Class'ın 4.Child Class'ı)
class HastanePolisi(Calisanlar):
    
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas,poliklinik):
        self.__poliklinik=poliklinik
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani, zam, maas)
    
    #Get metodları
    
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_zam(self):
        return self.zam
    
    def get_maas(self):
        return self.maas
    
    def get_poliklinik(self):
        return self.__poliklinik
    
    #Set metodları
    
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
      
    def set_zam(self,new):
        self.zam=new
        
    def set_maas(self,new):
        self.maas=new
    
    def set_baslamazamani(self,new):
        self.baslamazamani=new
    
    def set_poliklinik(self,new):
        self.__poliklinik=new     
        
#2.Base Class --> Destek Personeli Class'ı        
class DestekPersoneli(Hastane):
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani,saatlikUcret , gorevAlani):
        self.__saatlikUcret=saatlikUcret
        self.__gorevAlani=gorevAlani
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani)

#Get Metotları
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_saatlikUcret(self):
        return self.__saatlikUcret
    
    def get_gorevAlani(self):
        return self.__gorevAlani
    
#Set Metotları
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
        
    def set_baslamazamani(self, new):
        self.baslamazamani=new
    
    def set_gorevAlani(self,new):
        self.__gorevAlani=new
    
    def set_saatlikUcret(self,new):
        self.__saatlikUcret=new
    
class TemizlikGorevlisi(DestekPersoneli):
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani,saatlikUcret , gorevAlani,temizlikAlani):
        self.__saatlikUcret=saatlikUcret
        self.__gorevAlani=gorevAlani
        self.__temizlikAlani=temizlikAlani
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani)

#Get Metotları
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_saatlikUcret(self):
        return self.__saatlikUcret
    
    def get_gorevAlani(self):
        return self.__gorevAlani
    
    def get_temizlikAlani(self):
        return self.__temizlikAlani
    
#Set Metotları
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
        
    def set_baslamazamani(self, new):
        self.baslamazamani=new
    
    def set_gorevAlani(self,new):
        self.__gorevAlani=new
    
    def set_saatlikUcret(self,new):
        self.__saatlikUcret=new
    
    def set_temizlikAlani(self,new):
        self.__temizlikAlani=new
    
class HastaBakimElamani(DestekPersoneli):
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani,saatlikUcret , gorevAlani,gorev):
        self.__saatlikUcret=saatlikUcret
        self.__gorevAlani=gorevAlani
        self.__gorev=gorev
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani)

#Get Metotları
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_saatlikUcret(self):
        return self.saatlikUcret
    
    def get_gorevAlani(self):
        return self.__gorevAlani
    
    def get_temizlikAlani(self):
        return self.__temizlikAlani
    
    def get_gorev(self):
        return self.__gorev
    
#Set Metotları
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
        
    def set_baslamazamani(self, new):
        self.baslamazamani=new
    
    def set_gorevAlani(self,new):
        self.__gorevAlani=new
    
    def set_saatlikUcret(self,new):
        self.__saatlikUcret=new
    
    def set_temizlikAlani(self,new):
        self.__temizlikAlani=new    
    
    def set_gorev(self,new):
        self.__gorev=new

#3.Base Class --> Stajyer Class'ı        
class Stajyer(Hastane):
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani,stajGunu):
        self.__stajGunu=stajGunu
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani)

#Get Metotları
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_stajGunu(self):
        return self.__stajGunu
    
#Set Metotları
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
        
    def set_baslamazamani(self, new):
        self.baslamazamani=new
    
    def set_stajGunu(self,new):
        self.stajGunu=new
    
class StajyerOgrenci(Stajyer):
    def __init__(self, ad, soyad, cinsiyet, tcno, baslamazamani, stajGunu,sinif):
        self.__sinif=sinif
        super().__init__(ad, soyad, cinsiyet, tcno, baslamazamani, stajGunu)

#Get Metotları
    def get_ad(self):
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def get_cinsiyet(self):
        return self.cinsiyet
    
    def get_tcno(self):
        return self.tcno
    
    def get_baslamazamani(self):
        return self.baslamazamani
    
    def get_stajGunu(self):
        return self.stajGunu
    def get_sinif(self):
        return self.__sinif
    
#Set Metotları
    def set_ad(self,new):
        self.ad=new
    
    def set_soyad(self,new):
        self.soyad=new
    
    def set_cinsiyet(self,new):
        self.cinsiyet=new
        
    def set_tcno(self,new):
        self.tcno=new
        
    def set_baslamazamani(self, new):
        self.baslamazamani=new
    
    def set_stajGunu(self,new):
        self.stajGunu=new
    
    def set_sinif(self,new):
        self.__sinif=new
        
    @staticmethod
    def mesaj_stajyer():
        print('Staj haftada en fazla 6 iş günü (48 saat) yapılabilir. ')
    
#doktor ekleme çıkarma düzenleme kısmı
doktorList=[]
def doktorEkle():
    ad=input('Doktor ismi:')
    soyad=input('Doktor soyad:')
    cinsiyet=input('Doktor cinsiyet:')
    tcno=int(input('Doktor tcno su:'))
    baslamazamani=date.today()
    zam=1
    maas=int(input('Doktor Maasi:'))
    poliklinik=input('Doktor Poliklinik:')
    doktorList.append(Doktor(ad,soyad,cinsiyet,tcno,baslamazamani,zam,maas,poliklinik))
    
    
def doktorSil(SilinecekDoktorTcno):
    for i in doktorList:
        if i.get_tcno()==SilinecekDoktorTcno:
            doktorList.remove(i)
            break
    else:
        print('Bu Tcno ya sahip bir doktor bulunumadı')

def doktorDüzenle():
    DuzenlenecekDoktorTcno=int(input('Düzenlenecek Doktor un Tcno sunu giriniz:'))
    for i in doktorList:
        
        
        if i.get_tcno()==DuzenlenecekDoktorTcno:
            DuzenlenecekDoktorOzelligi=input('Düzenlenecek doktor özelliğini giriniz:') 
            if DuzenlenecekDoktorOzelligi=='ad':
                print('Doktor ismi:',i.get_ad())
                new=input('Yeni İsim:')
                i.set_ad(new)
            elif DuzenlenecekDoktorOzelligi=='soyad':
                print('Doktor ismi:',i.get_soyad())
                new=input('Yeni Soyisim:')
                i.set_soyad(new)
            elif DuzenlenecekDoktorOzelligi=='cinsiyet':
                print('Doktor Cinsiyeti:',i.get_cinsiyet())
                new=input('Yeni Cinsiyet:')
                i.set_cinsiyet(new)
            elif DuzenlenecekDoktorOzelligi=='tcno':
                print('Doktor Tcno su:',i.get_tcno())
                new=int(input('Yeni tcno:'))
                i.set_tcno(new)
            elif DuzenlenecekDoktorOzelligi=='zam':
                print('Doktor zam mı:',i.get_zam())
                new=int(input('Yeni zam:'))
                i.set_zam(new)
            elif DuzenlenecekDoktorOzelligi=='maas':
                print('Doktor maas ı:',i.get_maas())
                new=int(input('Yeni maas:'))
                i.set_maas(new)
            elif DuzenlenecekDoktorOzelligi=='poliklinik':
                print('Doktor poliklinik:',i.get_poliklinik())
                new=input('Yeni poliklinik:')
                i.set_poliklinik(new)            
            break
    else:
        print('Bu Tcno ya sahip bir doktor bulunumadı')
        
HemsireList=[]
#hemsire ekle sil düzenle kısmınon fonksiyonları
def HemsireEkle():
    ad=input('Hemşire ismi:')
    soyad=input('Hemşire soyad:')
    cinsiyet=input('Hemşire cinsiyet:')
    tcno=int(input('Hemşire tcno su:'))
    baslamazamani=date.today()
    zam=1
    maas=int(input('Hemşire Maasi:'))
    poliklinik=input('Hemşire Poliklinik:')
    HemsireList.append(Hemsire(ad,soyad,cinsiyet,tcno,baslamazamani,zam,maas,poliklinik))

def HemsireSil(SilinecekHemsireTcno):
    for i in HemsireList:
        if i.get_tcno()==SilinecekHemsireTcno:
            HemsireList.remove(i)
            break
    else:
        print('Bu Tcno ya sahip bir Hemsire bulunumadı')

def HemsireDüzenle():
    DuzenlenecekHemsireTcno=int(input('Düzenlenecek Hemsire un Tcno sunu giriniz:'))
    for i in HemsireList:
        if i.get_tcno()==DuzenlenecekHemsireTcno:
            DuzenlenecekHemsireOzelligi=input('Düzenlenecek Hemsire özelliğini giriniz:') 
            if DuzenlenecekHemsireOzelligi=='ad':
                print('Hemsire ismi:',i.get_ad())
                new=input('Yeni İsim:')
                i.set_ad(new)
            elif DuzenlenecekHemsireOzelligi=='soyad':
                print('Hemsire ismi:',i.get_soyad())
                new=input('Yeni Soyisim:')
                i.set_soyad(new)
            elif DuzenlenecekHemsireOzelligi=='cinsiyet':
                print('Hemsire Cinsiyeti:',i.get_cinsiyet())
                new=input('Yeni Cinsiyet:')
                i.set_cinsiyet(new)
            elif DuzenlenecekHemsireOzelligi=='tcno':
                print('Hemsire Tcno su:',i.get_tcno())
                new=int(input('Yeni tcno:'))
                i.set_tcno(new)
            elif DuzenlenecekHemsireOzelligi=='zam':
                print('Hemsire zam mı:',i.get_zam())
                new=int(input('Yeni zam:'))
                i.set_zam(new)
            elif DuzenlenecekHemsireOzelligi=='maas':
                print('Hemsire maas ı:',i.get_maas())
                new=int(input('Yeni maas:'))
                i.set_maas(new)
            elif DuzenlenecekHemsireOzelligi=='poliklinik':
                print('Hemsire poliklinik:',i.get_poliklinik())
                new=input('Yeni poliklinik:')
                i.set_poliklinik(new)            
            break
    else:
        print('Bu Tcno ya sahip bir Hemsire bulunumadı')

#güvenlik ekle sil düzenle
GuvenlikList=[]
#Guvenlik ekle sil düzenle kısmınon fonksiyonları
def GuvenlikEkle():
    ad=input('Güvenlik ismi:')
    soyad=input('Güvenlik soyad:')
    cinsiyet=input('Güvenlik cinsiyet:')
    tcno=int(input('Güvenlik tcno su:'))
    baslamazamani=date.today()
    zam=1
    maas=int(input('Güvenlik Maasi:'))
    guvenlikEgitimi=input('Guvenlik Egitimi:')
    atesleyiciYeterlilikNotu=int(input('Ateşleyici Yeterlilik Notu:'))
    GuvenlikList.append(Guvenlik(ad,soyad,cinsiyet,tcno,baslamazamani,zam,maas,guvenlikEgitimi,atesleyiciYeterlilikNotu))

def GuvenlikSil(SilinecekGuvenlikTcno):
    for i in GuvenlikList:
        if i.get_tcno()==SilinecekGuvenlikTcno:
            GuvenlikList.remove(i)
            break
    else:
        print('Bu Tcno ya sahip bir Guvenlik bulunumadı')

def GuvenlikDüzenle():
    DuzenlenecekGuvenlikTcno=int(input('Düzenlenecek Guvenlik un Tcno sunu giriniz:'))
    for i in GuvenlikList:
        if i.get_tcno()==DuzenlenecekGuvenlikTcno:
            DuzenlenecekGuvenlikOzelligi=input('Düzenlenecek Guvenlik özelliğini giriniz:') 
            if DuzenlenecekGuvenlikOzelligi=='ad':
                print('Guvenlik ismi:',i.get_ad())
                new=input('Yeni İsim:')
                i.set_ad(new)
            elif DuzenlenecekGuvenlikOzelligi=='soyad':
                print('Guvenlik ismi:',i.get_soyad())
                new=input('Yeni Soyisim:')
                i.set_soyad(new)
            elif DuzenlenecekGuvenlikOzelligi=='cinsiyet':
                print('Guvenlik Cinsiyeti:',i.get_cinsiyet())
                new=input('Yeni Cinsiyet:')
                i.set_cinsiyet(new)
            elif DuzenlenecekGuvenlikOzelligi=='tcno':
                print('Guvenlik Tcno su:',i.get_tcno())
                new=int(input('Yeni tcno:'))
                i.set_tcno(new)
            elif DuzenlenecekGuvenlikOzelligi=='zam':
                print('Guvenlik zam mı:',i.get_zam())
                new=int(input('Yeni zam:'))
                i.set_zam(new)
            elif DuzenlenecekGuvenlikOzelligi=='maas':
                print('Guvenlik maas ı:',i.get_maas())
                new=int(input('Yeni maas:'))
                i.set_maas(new)
            elif DuzenlenecekGuvenlikOzelligi=='guvenlikEgitimi':
                print('Guvenlik guvenlikEgitimi:',i.get_guvenlikEgitimi())
                new=input('Yeni guvenlikEgitimi:')
                i.set_guvenlikEgitimi(new)            
            elif DuzenlenecekGuvenlikOzelligi=='atesleyiciYeterlilikNotu':
                print('Guvenlik Ateşleyici Yeterlilik Notu:',i.get_atesleyiciYeterlilikNotu())
                new=input('Yeni Ateşleyici Yeterlilik Notu:')
                i.set_atesleyiciYeterlilikNotu(new)     
            break
    else:
        print('Bu Tcno ya sahip bir Guvenlik bulunumadı')

HastanePolisiList=[]

def HastanePolisiEkle():
    ad=input('Hastane polisi ismi:')
    soyad=input('Hastane polisi soyad:')
    cinsiyet=input('Hastane polisi cinsiyet:')
    tcno=int(input('Hastane polisi tcno su:'))
    baslamazamani=date.today()
    zam=1
    maas=int(input('Hastane polisi Maasi:'))
    poliklinik=input('Hastane polisi Poliklinik:')
    HastanePolisiList.append(HastanePolisi(ad,soyad,cinsiyet,tcno,baslamazamani,zam,maas,poliklinik))
    

#sorunu çözemedim
def HastanePolisiSil(SilinecekHastanePolisiTcno):
    for i in HastanePolisiList:
        if i.get_tcno()==SilinecekHastanePolisiTcno:
            HastanePolisiList.remove(i)
            break
    else:
        print('Bu Tcno ya sahip bir Hastane Polisi bulunumadi')

def HastanePolisiDüzenle():
    DuzenlenecekHastanePolisiTcno=int(input('Düzenlenecek HastanePolisi un Tcno sunu giriniz:'))
    for i in HastanePolisiList:
        if i.get_tcno()==DuzenlenecekHastanePolisiTcno:
            DuzenlenecekHastanePolisiOzelligi=input('Düzenlenecek HastanePolisi özelliğini giriniz:') 
            if DuzenlenecekHastanePolisiOzelligi=='ad':
                print('HastanePolisi ismi:',i.get_ad())
                new=input('Yeni İsim:')
                i.set_ad(new)
            elif DuzenlenecekHastanePolisiOzelligi=='soyad':
                print('HastanePolisi ismi:',i.get_soyad())
                new=input('Yeni Soyisim:')
                i.set_soyad(new)
            elif DuzenlenecekHastanePolisiOzelligi=='cinsiyet':
                print('HastanePolisi Cinsiyeti:',i.get_cinsiyet())
                new=input('Yeni Cinsiyet:')
                i.set_cinsiyet(new)
            elif DuzenlenecekHastanePolisiOzelligi=='tcno':
                print('HastanePolisi Tcno su:',i.get_tcno())
                new=int(input('Yeni tcno:'))
                i.set_tcno(new)
            elif DuzenlenecekHastanePolisiOzelligi=='zam':
                print('HastanePolisi zam mı:',i.get_zam())
                new=int(input('Yeni zam:'))
                i.set_zam(new)
            elif DuzenlenecekHastanePolisiOzelligi=='maas':
                print('HastanePolisi maas ı:',i.get_maas())
                new=int(input('Yeni maas:'))
                i.set_maas(new)
            elif DuzenlenecekHastanePolisiOzelligi=='poliklinik':
                print('HastanePolisi poliklinik:',i.get_poliklinik())
                new=input('Yeni poliklinik:')
                i.set_poliklinik(new)            
            break
    else:
        print('Bu Tcno ya sahip bir HastanePolisi bulunumadı')

DestekPersoneliList=[]
#DestekPersoneli ekle sil düzenle kısmınon fonksiyonları
def DestekPersoneliEkle():
    ad=input('Destek Personeli ismi:')
    soyad=input('Destek Personeli soyad:')
    cinsiyet=input('Destek Personeli cinsiyet:')
    tcno=int(input('Destek Personeli tcno su:'))
    baslamazamani=date.today()
    zam=1
    maas=int(input('Destek Personeli Maasi:'))
    saatlikUcret=int(input('Destek Personeli saatlik Ücreti:'))
    gorevAlani=input('Destek Personeli görev alanı:')
    DestekPersoneliList.append(DestekPersoneli(ad,soyad,cinsiyet,tcno,baslamazamani,zam,maas,saatlikUcret,gorevAlani))

def DestekPersoneliSil(SilinecekDestekPersoneliTcno):
    for i in DestekPersoneliList:
        if i.get_tcno()==SilinecekDestekPersoneliTcno:
            DestekPersoneliList.remove(i)
            break
    else:
        print('Bu Tcno ya sahip bir DestekPersoneli bulunumadı')

def DestekPersoneliDüzenle():
    DuzenlenecekDestekPersoneliTcno=int(input('Düzenlenecek DestekPersoneli un Tcno sunu giriniz:'))
    for i in DestekPersoneliList:
        if i.get_tcno()==DuzenlenecekDestekPersoneliTcno:
            DuzenlenecekDestekPersoneliOzelligi=input('Düzenlenecek DestekPersoneli özelliğini giriniz:') 
            if DuzenlenecekDestekPersoneliOzelligi=='ad':
                print('DestekPersoneli ismi:',i.get_ad())
                new=input('Yeni İsim:')
                i.set_ad(new)
            elif DuzenlenecekDestekPersoneliOzelligi=='soyad':
                print('DestekPersoneli ismi:',i.get_soyad())
                new=input('Yeni Soyisim:')
                i.set_soyad(new)
            elif DuzenlenecekDestekPersoneliOzelligi=='cinsiyet':
                print('DestekPersoneli Cinsiyeti:',i.get_cinsiyet())
                new=input('Yeni Cinsiyet:')
                i.set_cinsiyet(new)
            elif DuzenlenecekDestekPersoneliOzelligi=='tcno':
                print('DestekPersoneli Tcno su:',i.get_tcno())
                new=int(input('Yeni tcno:'))
                i.set_tcno(new)
            elif DuzenlenecekDestekPersoneliOzelligi=='zam':
                print('DestekPersoneli zam mı:',i.get_zam())
                new=int(input('Yeni zam:'))
                i.set_zam(new)
            elif DuzenlenecekDestekPersoneliOzelligi=='maas':
                print('DestekPersoneli maas ı:',i.get_maas())
                new=int(input('Yeni maas:'))
                i.set_maas(new)
            elif DuzenlenecekDestekPersoneliOzelligi=='poliklinik':
                print('DestekPersoneli poliklinik:',i.get_poliklinik())
                new=input('Yeni poliklinik:')
                i.set_poliklinik(new)
            elif DuzenlenecekDestekPersoneliOzelligi=='saatlikUcret':
                print('DestekPersoneli saatlikUcret:',i.get_poliklinik())
                new=input('Yeni saatlik Ücret:')
                i.set_poliklinik(new)  
            elif DuzenlenecekDestekPersoneliOzelligi=='gorevAlani':
                print('DestekPersoneli Görev Alani:',i.get_gorevAlani())
                new=input('Yeni gorevAlani:')
                i.set_gorevAlani(new)              
            break
    else:
        print('Bu Tcno ya sahip bir DestekPersoneli bulunumadı')

TemizlikGorevlisiList=[]
#TemizlikGorevlisi ekle sil düzenle kısmınon fonksiyonları
def TemizlikGorevlisiEkle():
    ad=input('Temizlik görevlisi ismi:')
    soyad=input('Temizlik görevlisi soyad:')
    cinsiyet=input('Temizlik görevlisi cinsiyet:')
    tcno=int(input('Temizlik görevlisi tcno su:'))
    baslamazamani=date.today()
    saatlikUcret=int(input('Temizlik görevlisi saatlik Ücreti:'))
    gorevAlani=input('Temizlik görevlisi görev alanı:')
    temizlikAlani=input('Temizlik Görevlisinin temizlik alanı:')
    TemizlikGorevlisiList.append(TemizlikGorevlisi(ad,soyad,cinsiyet,tcno,baslamazamani,saatlikUcret,gorevAlani,temizlikAlani))


def TemizlikGorevlisiSil(SilinecekTemizlikGorevlisiTcno):
    for i in TemizlikGorevlisiList:
        if i.get_tcno()==SilinecekTemizlikGorevlisiTcno:
            TemizlikGorevlisiList.remove(i)
            break
    else:
        print('Bu Tcno ya sahip bir TemizlikGorevlisi bulunumadı')

def TemizlikGorevlisiDüzenle():
    DuzenlenecekTemizlikGorevlisiTcno=int(input('Düzenlenecek TemizlikGorevlisi un Tcno sunu giriniz:'))
    for i in TemizlikGorevlisiList:
        if i.get_tcno()==DuzenlenecekTemizlikGorevlisiTcno:
            DuzenlenecekTemizlikGorevlisiOzelligi=input('Düzenlenecek TemizlikGorevlisi özelliğini giriniz:') 
            if DuzenlenecekTemizlikGorevlisiOzelligi=='ad':
                print('TemizlikGorevlisi ismi:',i.get_ad())
                new=input('Yeni İsim:')
                i.set_ad(new)
            elif DuzenlenecekTemizlikGorevlisiOzelligi=='soyad':
                print('TemizlikGorevlisi ismi:',i.get_soyad())
                new=input('Yeni Soyisim:')
                i.set_soyad(new)
            elif DuzenlenecekTemizlikGorevlisiOzelligi=='cinsiyet':
                print('TemizlikGorevlisi Cinsiyeti:',i.get_cinsiyet())
                new=input('Yeni Cinsiyet:')
                i.set_cinsiyet(new)
            elif DuzenlenecekTemizlikGorevlisiOzelligi=='tcno':
                print('TemizlikGorevlisi Tcno su:',i.get_tcno())
                new=int(input('Yeni tcno:'))
                i.set_tcno(new)
            elif DuzenlenecekTemizlikGorevlisiOzelligi=='poliklinik':
                print('TemizlikGorevlisi poliklinik:',i.get_poliklinik())
                new=input('Yeni poliklinik:')
                i.set_poliklinik(new)
            elif DuzenlenecekTemizlikGorevlisiOzelligi=='saatlikUcret':
                print('TemizlikGorevlisi saatlikUcret:',i.get_saatlikUcret())
                new=input('Yeni saatlik Ücret:')
                i.set_saatlikUcret(new)  
            elif DuzenlenecekTemizlikGorevlisiOzelligi=='gorevAlani':
                print('TemizlikGorevlisi Görev Alani:',i.get_gorevAlani())
                new=input('Yeni gorevAlani:')
                i.set_gorevAlani(new)              
            elif DuzenlenecekTemizlikGorevlisiOzelligi=='saatlikUcret':
                print('TemizlikGorevlisi saatlik ücreti:',i.get_saatlikUcret())
                new=int(input('Yeni saatlik ücret:'))
                i.set_saatlikUcret(new)
            elif DuzenlenecekTemizlikGorevlisiOzelligi=='gorevAlani':
                print('TemizlikGorevlisi maas ı:',i.get_gorevAlani())
                new=int(input('Yeni gorev Alanı:'))
                i.set_gorevAlani(new)
            break
    else:
        print('Bu Tcno ya sahip bir TemizlikGorevlisi bulunumadı')

#Hasta bakım elamanı
HastaBakimElamaniList=[]

#HastaBakimElamani ekle sil düzenle kısmınon fonksiyonları
def HastaBakimElamaniEkle():
    ad=input('Hasta Bakim Elamani ismi:')
    soyad=input('Hasta Bakim Elamani soyad:')
    cinsiyet=input('Hasta Bakim Elamani cinsiyet:')
    tcno=int(input('Hasta Bakim Elamani tcno su:'))
    baslamazamani=date.today()
    saatlikUcret=int(input('Hasta Bakim Elamani saatlik Ücreti:'))
    gorevAlani=input('Hasta Bakim Elamani görev alanı:')
    gorev=input('Görev Alan')
    HastaBakimElamaniList.append(HastaBakimElamani(ad,soyad,cinsiyet,tcno,baslamazamani,saatlikUcret,gorevAlani,gorev))

def HastaBakimElamaniSil(SilinecekHastaBakimElamaniTcno):
    for i in HastaBakimElamaniList:
        if i.get_tcno()==SilinecekHastaBakimElamaniTcno:
            HastaBakimElamaniList.remove(i)
            break
    else:
        print('Bu Tcno ya sahip bir HastaBakimElamani bulunumadı')

def HastaBakimElamaniDüzenle():
    DuzenlenecekHastaBakimElamaniTcno=int(input('Düzenlenecek HastaBakimElamani un Tcno sunu giriniz:'))
    for i in HastaBakimElamaniList:
        if i.get_tcno()==DuzenlenecekHastaBakimElamaniTcno:
            DuzenlenecekHastaBakimElamaniOzelligi=input('Düzenlenecek HastaBakimElamani özelliğini giriniz:') 
            if DuzenlenecekHastaBakimElamaniOzelligi=='ad':
                print('HastaBakimElamani ismi:',i.get_ad())
                new=input('Yeni İsim:')
                i.set_ad(new)
            elif DuzenlenecekHastaBakimElamaniOzelligi=='soyad':
                print('HastaBakimElamani ismi:',i.get_soyad())
                new=input('Yeni Soyisim:')
                i.set_soyad(new)
            elif DuzenlenecekHastaBakimElamaniOzelligi=='cinsiyet':
                print('HastaBakimElamani Cinsiyeti:',i.get_cinsiyet())
                new=input('Yeni Cinsiyet:')
                i.set_cinsiyet(new)
            elif DuzenlenecekHastaBakimElamaniOzelligi=='tcno':
                print('HastaBakimElamani Tcno su:',i.get_tcno())
                new=int(input('Yeni tcno:'))
                i.set_tcno(new)
            elif DuzenlenecekHastaBakimElamaniOzelligi=='saatlikUcret':
                print('TemizlikGorevlisi saatlikUcret:',i.get_saatlikUcret())
                new=input('Yeni saatlik Ücret:')
                i.set_saatlikUcret(new)  
            elif DuzenlenecekHastaBakimElamaniOzelligi=='gorevAlani':
                print('HastaBakimElamani Görev Alani:',i.get_gorevAlani())
                new=input('Yeni gorevAlani:')
                i.set_gorevAlani(new)
            elif DuzenlenecekHastaBakimElamaniOzelligi=='gorev':
                print('HastaBakimElamani görevi:',i.get_gorev())
                new=int(input('Yeni gorev:'))
                i.set_gorev(new)
            break
    else:
        print('Bu Tcno ya sahip bir HastaBakimElamani bulunumadı')
    
#stajyer hastane

StajyerOgrenciList=[]

#StajyerOgrenci ekle sil düzenle kısmınon fonksiyonları
def StajyerOgrenciEkle():
    ad=input('StajyerOgrenci ismi:')
    soyad=input('StajyerOgrenci soyad:')
    cinsiyet=input('StajyerOgrenci cinsiyet:')
    tcno=int(input('StajyerOgrenci tcno su:'))
    baslamazamani=date.today()
    stajGunu=input('StajyerOgrenci günü:')
    sinif=int(input('StajyerOgrenci sinif:'))
    print('run 1063')
    StajyerOgrenciList.append(StajyerOgrenci(ad,soyad,cinsiyet,tcno,baslamazamani,stajGunu,sinif))

def StajyerOgrenciSil(SilinecekStajyerOgrenciTcno):
    for i in StajyerOgrenciList:
        if i.get_tcno()==SilinecekStajyerOgrenciTcno:
            StajyerOgrenciList.remove(i)
            break
    else:
        print('Bu Tcno ya sahip bir StajyerOgrenci bulunumadı')

def StajyerOgrenciDüzenle():
    DuzenlenecekStajyerOgrenciTcno=int(input('Düzenlenecek StajyerOgrenci un Tcno sunu giriniz:'))
    for i in StajyerOgrenciList:
        if i.get_tcno()==DuzenlenecekStajyerOgrenciTcno:
            DuzenlenecekStajyerOgrenciOzelligi=input('Düzenlenecek StajyerOgrenci özelliğini giriniz:') 
            if DuzenlenecekStajyerOgrenciOzelligi=='ad':
                print('StajyerOgrenci ismi:',i.get_ad())
                new=input('Yeni İsim:')
                i.set_ad(new)
            elif DuzenlenecekStajyerOgrenciOzelligi=='soyad':
                print('StajyerOgrenci ismi:',i.get_soyad())
                new=input('Yeni Soyisim:')
                i.set_soyad(new)
            elif DuzenlenecekStajyerOgrenciOzelligi=='cinsiyet':
                print('StajyerOgrenci Cinsiyeti:',i.get_cinsiyet())
                new=input('Yeni Cinsiyet:')
                i.set_cinsiyet(new)
            elif DuzenlenecekStajyerOgrenciOzelligi=='tcno':
                print('StajyerOgrenci Tcno su:',i.get_tcno())
                new=int(input('Yeni tcno:'))
                i.set_tcno(new)
            elif DuzenlenecekStajyerOgrenciOzelligi=='stajGunu':
                print('StajyerOgrenci stajGunu:',i.get_stajGunu())
                new=input('Yeni stajGunu:')
                i.set_stajGunu(new)  
            elif DuzenlenecekStajyerOgrenciOzelligi=='sinif':
                print('StajyerOgrenci sinif:',i.get_sinif())
                new=input('Yeni sinif:')
                i.set_sinif(new)
            break
        
    else:
        print('Bu Tcno ya sahip bir StajyerOgrenci bulunumadı')

    
    
HastanePolisiList.append(HastanePolisi(123,123,123,123,123,123,123,123))
    
name='enes'
sifre='123'
adminList=[{'Adminİsim':name,'AdminSifre':sifre}]
#arayüz
def arayuz():
    secim=1
    while secim!=0:
        #admin girişi kısmı
        adminisim=input('Admin isminizi giriniz:')
        adminsifre=input('Admin sifrenizi giriniz:')
        for i in range(len(adminList)):
            if adminisim==adminList[i]['Adminİsim']:
                if adminsifre==adminList[i]['AdminSifre']:
                    secim=int(input('Çıkmak için 0 a basınız,Doktor işlemleri için 1 e basınız,Hemsire işlemleri için 2 e basınız,Guvenlik elamanı işlemleri için 3 e basınız,Hastane Polisi işlemleri için 4 e basınız,Destek Personeli işlemleri için 5 e basınız,Temizlik Gorevlisi işlemleri için 6 ya basınız,Hasta Bakim Elamani işlemleri için 7 ye basınız,Stajyer Ogrenci işlemleri için 8 ye basınız'))
                    if secim==1:
                    #doktor için işlemler
                        doktorsecim=int(input('Doktor eklemek için 1,Ekli doktoru düzenlemek için 2,Doktor silmek için 3 e basınız '))
                        if doktorsecim==1:
                            doktorEkle()
                        if doktorsecim==2:
                            doktorDüzenle()
                        if doktorsecim==3:
                            tcno=int(input('Silinecek doktor tc no su:'))
                            doktorSil(tcno)
                    #2 hemsire için ytapılacakj önce hemsire ekle düzenle sil fonksiyonları yap
                    if secim==2:
                        Hemsiresecim=int(input('Hemsire eklemek için 1,Ekli Hemsireu düzenlemek için 2,Hemsire silmek için 3 e basınız '))
                        if Hemsiresecim==1:
                            HemsireEkle()
                        if Hemsiresecim==2:
                            HemsireDüzenle()
                        if Hemsiresecim==3:
                            tcno=int(input('Silinecek hemsire tc no su:'))
                            HemsireSil(tcno)
                    #3Guvenlik için ekle sil düzenle
                    if secim==3:
                        Guvenliksecim=int(input('Guvenlik eklemek için 1,Ekli Guvenlik düzenlemek için 2,Guvenlik silmek için 3 e basınız '))
                        if Guvenliksecim==1:
                            GuvenlikEkle()
                        if Guvenliksecim==2:
                            GuvenlikDüzenle()
                        if Guvenliksecim==3:
                            tcno=int(input('Silinecek guvenlik tc no su:'))
                            GuvenlikSil(tcno)
                    #4 hastane polisi ekle sil düzenle
                    if secim==4:
                        HastanePolisi=int(input('Hastane Polisi eklemek için 1,Ekli Hastane Polisi düzenlemek için 2,Hastane Polisi silmek için 3 e basınız '))
                        if HastanePolisi==1:
                            HastanePolisiEkle()
                        if HastanePolisi==2:
                            HastanePolisiDüzenle()
                        if HastanePolisi==3:
                            tcno=int(input('Silinecek hastane tc no su:'))
                            HastanePolisiSil(tcno)
                    #5 hastane destek personeli ekle sil düzenle
                    if secim==5:
                        DestekPersoneli=int(input('Destek Personeli eklemek için 1,Ekli Destek Personeli düzenlemek için 2,Destek Personeli silmek için 3 e basınız '))
                        if DestekPersoneli==1:
                            DestekPersoneliEkle()
                        if DestekPersoneli==2:
                            DestekPersoneliDüzenle()
                        if DestekPersoneli==3:
                            tcno=int(input('Silinecek DestekPersoneli tc no su:'))
                            DestekPersoneliSil(tcno)
                    #6temizlik görevlisinde kaldık
                    if secim==6:
                        TemizlikGorevlisi=int(input('Temizlik Gorevlisi eklemek için 1,Ekli Temizlik Gorevlisi düzenlemek için 2,Temizlik Gorevlisi silmek için 3 e basınız '))
                        if TemizlikGorevlisi==1:
                            TemizlikGorevlisiEkle()
                        if TemizlikGorevlisi==2:
                            TemizlikGorevlisiDüzenle()
                        if TemizlikGorevlisi==3:
                            tcno=int(input('Silinecek temizlik gorevlisi tc no su:'))
                            TemizlikGorevlisiSil(tcno)
                    #7hasta bakım elamanı HastaBakimElamani
                    if secim==7:
                        HastaBakimElamani=int(input('Hasta Bakim Elamani eklemek için 1,Ekli Hasta Bakim Elamani düzenlemek için 2,Hasta Bakim Elamani silmek için 3 e basınız '))
                        if HastaBakimElamani==1:
                            HastaBakimElamaniEkle()
                        if HastaBakimElamani==2:
                            HastaBakimElamaniDüzenle()
                        if HastaBakimElamani==3:
                            tcno=int(input('Silinecek Hasta bakim elamani tc no su:'))
                            HastaBakimElamaniSil(tcno)
                    if secim==8:
                        StajyerOgrenci=int(input('Stajyer Ogrenci eklemek için 1,Ekli Stajyer Ogrenci düzenlemek için 2,Stajyer Ogrenci silmek için 3 e basınız '))
                        if StajyerOgrenci==1:
                            StajyerOgrenciEkle()
                        if StajyerOgrenci==2:
                            StajyerOgrenciDüzenle()
                        if StajyerOgrenci==3:
                            tcno=int(input('Silinecek Stajyer Ogrenci tc no su:'))
                            StajyerOgrenciSil(tcno)
                    





























