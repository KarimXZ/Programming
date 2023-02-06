#https://drive.google.com/file/d/1YDCBspIVMbXMvetfvfM2D3R8JN0ABbhr/view?usp=sharing
from abc import ABC, abstractmethod
import random
class Hospital(ABC):
    @abstractmethod
    def __init__(self,name,location):
        self.name=name
        self.location=location
    @abstractmethod
    def getname(self):
        pass
    @abstractmethod
    def getlocation(self):
        pass
FreeDoctors=[]
BusyDoctors=[]
Hospitalers=[]
class Doctor(Hospital):
    def __init__(self,name,title, specialty,location=None):
        super().__init__(name,location)
        self.title=title
        self.specialty=specialty
        FreeDoctors.append(self)
        Hospitalers.append(self)
        self.location=random.randint(100,300)
    def getname(self):
        print(self.title+'.'+self.name)
    def getlocation(self):
        print(f"Bu Doktor simdi ofis {self.location}'da")
    def changeavailability(self):
        FreeDoctors.remove(self)
        BusyDoctors.append(self)
class Patient(Hospital):
    def __init__(self,name,illness,cure=0,location=None,):
        super().__init__(name,location)
        self.illness=illness
        self.cure=cure
        self.location=random.randint(0,100)
        Hospitalers.append(self)
    def getname(self):
        print(self.name)
    def getlocation(self):
        print(f"Bu Kisi simdi yatak {self.location}'da")
    def getillness(self):
        print(self.illness)
    def curepotential(self):
        if len(FreeDoctors)>0:
            global Chosen
            Chosen=FreeDoctors[random.randint(0, len(FreeDoctors)-1)]
            Chosen.changeavailability()
            print(f"{Chosen.title}.{Chosen.name} simdi {self.name}'e yardim ediyor.")
            self.cure=1
        else:
            print("Yapacak bir sey yok, hic kimse musait degil. Daha beklemek lazem.")
    def getcure(self):
        if self.cure==0:
            print(f"Bu kisi hala hastali:{self.illness} yuzden\nHic kimse ona yardim etmemis.")
        if self.cure==1:
            print(f"Bu kisi {Chosen.title}.{Chosen.name} tarafindan yardim edilmis. Daha iyi olacak.")
K=Doctor('Karim', 'Dr', 'Dietician')
M=Doctor('Mansour','Prof','Opthalmologist')
J=Patient('Jad', 'Malaria')
J.curepotential()
J.getcure()
L=Patient('Ahmet', 'HIV')
L.curepotential()
L.getcure()
N=Patient('Nasser', 'Kanser')
N.curepotential()
N.getcure()
for i in Hospitalers:
    i.getname()
    i.getlocation()