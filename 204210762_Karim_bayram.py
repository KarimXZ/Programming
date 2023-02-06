from abc import ABC,abstractmethod
import hashlib
class ControlPanel:
    def __init__(self,name,ver,host,password,status):
        self.name=name
        self.ver=ver
        self.host=host
        self.password=password
        self.status=status
        self.name_list=[]
    @abstractmethod
    def Login(self):
        pass
    @abstractmethod
    def status_check(self):
        pass
class Database(ControlPanel):
    tablecount=0
    def __init__(self, name, ver, host, password, status,data_name):
        super().__init__(name, ver, host, password, status)
        self.data_name=data_name
        self.name_list=[]
    def Login(self,user_pass):
        self.status=False
        if user_pass == self.password:
            self.status=True
            print("Giriş başarılı!")
        else:
            user_pass=input("Hatalı şifre, tekrar deneyin")
            Database.Login(user_pass)
    def status_check(self):
        if self.status==True:
            print("Giriş yapılmış")
        else:
            print("Giriş yapılmamış")
    def add_table(self,newtable):
        self.name_list.append(newtable)
    @classmethod
    def inc_table_count(cls):
        cls.tablecount=+1
class Server(ControlPanel):
    def Login(self,user_pass):
        self.status=False
        if hashlib.sha256(user_pass.encode()) == self.password:
            self.status=True
            print("Giriş başarılı!")
        else:
            user_pass=input("Hatalı şifre, tekrar deneyin")
            Server.Login(user_pass)
    def status_check(self):
        if self.status==True:
            print("Giriş yapılmış")
        else:
            print("Giriş yapılmamış")
    @staticmethod
    def show_ver_diff(ser1,ser2):
        if ser1.ver==ser2.ver:
            print(f"Sunucu versiyonlar aynıdır: {ser1.ver}")
        else:
            print(f"Birinci sunucun versiyonu:{ser1.ver}\nİkincisunucunun versiyonu:{ser2.ver}")
data1=Database("NoSQL", "1.0.4", "www.Karim.com/Data", "dondurmaseviyorum", False, "Student Base")
Server1=Server("Rockin Red Reaper", 2.11, "www.Karim.com/RRR", "elmaseviyorum", "False")
Server2=Server("Sweet Stylin Steve", 3.1415, "www.Karim.com/SSS", "yemekseviyorum", "False")

data1.add_table("Classes")
data1.inc_table_count()
data1.add_table("Students")
data1.inc_table_count()
Server1.show_ver_diff(Server1,Server2)