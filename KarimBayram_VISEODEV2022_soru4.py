import datetime as dt;
import os;
class File():
    def __init__(self,filename,fileformat,filedate,filecontents):
        self.__filename=filename;
        self.__fileformat=fileformat;
        self.__filedate=filedate;
        self.__filecontents=filecontents;
        self.__fileupdate=0
        self.__filepath='None';
    def getfilename(self):
        return self.__filename;
    def getfileformat(self):
        return self.__fileformat;
    def getfiledate(self):
        return self.__filedate;
    def getfilecontents(self):
        return self.__filecontents;
    def getfileupdate(self):
        return self.__fileupdate;
    def getfilepath(self):
        return self.__filepath;
    def setfilename(self,newfilename):
        self.__filename=newfilename;
        self.__fileupdate=dt.datetime.now();
    def setfileformat(self,newfileformat):
        self.__fileformat=newfileformat;
        self.__fileupdate=dt.now();
    def setfiledate(self,newfiledate):
        self.__filedate=newfiledate;
        self.__fileupdate=dt.datetime.now();
    def setfilecontents(self,newfilecontents):
        self.__filecontents=newfilecontents;
        self.__fileupdate=dt.datetime.now();
KarimFile = File('Karimin Bilgiler', '.txt', dt.date(2002,8,6), ['Karim,Bayram']);
def FileTest(x):
    print('Dosya Adı: Deneme'+x.getfilename());
    print('Dosya Formatı:'+x.getfileformat());
    print('Oluşturma Tarihi:'+str(x.getfiledate()));
    print('İçerik:'+str(x.getfilecontents()));
    print('Düzenleme Tarihi:'+str(x.getfileupdate()));
    print(''+x.getfilepath());
    x.setfilecontents(['Kerim','Bayram',20,'single'])
    print('İçerik:'+str(x.getfilecontents()))
    print('Düzenleme Tarihi:'+str(x.getfileupdate()))
FileTest(KarimFile);