#Student sinifa initialiser fonksiyon icinde ana liste ekleme kod var, ama video da degil
#https://drive.google.com/file/d/1AEN9cFE7rvmkimlcU8JAV2tQtS-rokux/view?usp=sharing
from abc import ABC
class University(ABC):
    DepStuds=[]
    def __init__(self):
        pass
class Department(University):
    def __init__(self,info,name,createdate):
        self._info=info
        self._name=name
        self._classes=[]
        self._Students=[]
        self._createdate=createdate
        University.DepStuds.append(self)
    def addclasses(self):
        for i in range(8):
            self._classes.append(input(f"{i+1}inci sinifin ismi yazin"))
    def addStudent(self,studname):
        x=input('Ogrencinin adi yazin lutfen')
        if x in University.DepStuds:
            self._Students.append(x)
        else:
            print('Bu ogrenci yok')
    @staticmethod
    def comparedate(dep1,dep2):
        x=abs(dep1._createdate-dep2._createdate)
        print(f'Bu depatmantlar {x} yil arasinda farki var')
    def StudentList(self):
        for i in self._Students:
            print(i)
class Student(University):
    def __init__(self,name,surname,bdate,course,avg):
        self._name=name
        self._surname=surname
        self._bdate=bdate
        self._course=course
        self._avg=avg
        University.DepStuds.append(self)
    def getinfo(self):
        print(f"{self._name} {self._surname},{self._bdate}:{self._courses}")
    @staticmethod
    def checkclassmates(stud):
        for i in University.DepStuds:
            if i._course==stud._course:
                print(i._name+i._surname)
    def checkage(self):
        print(2022-self._bdate)
    @classmethod
    def getall(cls):
        tempdep=[]
        tempstud=[]
        for i in cls.DepStuds:
            if i.info==True:
                tempdep.append(i)
            elif i.bdate==True:
                tempstud.append(i)
            else:
                continue
        for i in tempdep:
            print(i)
        for i in tempstud:
            print(i)