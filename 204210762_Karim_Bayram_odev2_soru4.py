class Animal:
    Animallist=[]
    Animalcount=0
    def __init__(self,a_type, age,size,name=''):
        self.a_type=a_type
        self.age=age
        self.size=size
        self.name=name
        Animal.Animalcount=Animal.Animalcount+1
    def addtolist(self):
        global properties
        properties=[]
        properties.append(self.a_type)
        properties.append(self.age)
        properties.append(self.size)
        properties.append(self.name)
        self.Animallist.append(properties)
        print("The animal has been added")
    def updatename(self,newname):
        properties.remove(self.name)
        self.name=newname
        print(f'The {self.a_type}s new name is {self.name}')
        properties.append(self.name)
    def printname(self):
        print(f'The {self.a_type}s name is {self.name}')
    @staticmethod
    def printa_count():
        print(f"There is a total of {Animal.Animalcount} animals")
    @staticmethod
    def printa_list():
        for i in Animal.Animallist:
            print(i)
    @classmethod
    def strangeanimal(cls,a_type,age,size):
        return cls(a_type,age,size)
a1=Animal('Camel',12,100)
a1.addtolist()
a1.updatename('Bob')
a1.printname()
a2=Animal('Dog',11,20)
a2.addtolist()
a2.updatename('Jeff')
a2.printname()
a3=Animal.strangeanimal('unknown',10, 100)
a3.addtolist()
a3.updatename('Jeff')
a3.printname()
Animal.printa_count()
Animal.printa_list()