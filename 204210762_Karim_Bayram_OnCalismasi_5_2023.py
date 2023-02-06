class Car:
    def __init__(self,company,model,year,fuelcap):
        self.__company=company;
        self.__model=model;
        self.__year=year;
        self.__fuelcap=fuelcap;
        self.__RemFuel=0;
    def getComp(self):
        return self.__company;
    def getModel(self):
        return self.__model;
    def getYear(self):
        return self.__year;
    def getFuel(self):
        return self.__fuelcap;
    def changeComp(self,newcomp):
        self.__company=newcomp;
    def changeModel(self,newModel):
        self.__model = newModel;
    def changeYear(self,newYear):
        self.__year=newYear;
    def changeCap(self,newCap):
        self.__fuelcap=newCap;
    def setRemFuel(self,newRemFuel):
        if newRemFuel>self.__fuelcap:
            print("WARNING:Remaining Fuel over maximum capacity. Setting new cap");
            self.__fuelcap=newRemFuel;
        self.__RemFuel=newRemFuel;
    def getRem(self):
        return self.__RemFuel;
    def increaseFuel(self,Fuel):
        if self.__RemFuel+Fuel>self.__fuelcap:
            print("Benzin miktari yanlis, lutfen tekrar deneyin");
        else:
            self.__RemFuel=self.__RemFuel+Fuel;
MyCar=Car("Toyota", "Corolla", 1986, 100)
print(MyCar.getComp())
print(MyCar.getModel())
print(MyCar.getFuel())
MyCar.increaseFuel(50)
print(MyCar.getYear())
print(MyCar.getRem())
MyCar.setRemFuel(200)
MyCar.increaseFuel(500)