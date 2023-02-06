import numpy as np;
class Geometry():
    def __init__(self,sidecount,sides=[]):
        self.sides=sides
        self.sidecount=sidecount
    def entersides(self):
        for i in range(self.sidecount):
            self.sides.append(int(input(f"{i}inci kenarin boyutu giriniz lutfen")))
    def listsides(self):
        for i in self.sides:
            print(i)
class TrianglePrism(Geometry):
    def _init__(self,sidecount,sides):
        super().__init__(sidecount,sides)
    def entersides(self):
        print("""1-3 kenarlar: Ucgen yuzunlerin kenarlari
4 kenar: Prismin boyutu""")
        for i in range(self.sidecount):
            self.sides.append(int(input(f"{i}inci kenarin boyutu giriniz lutfen")))
    def getVolume(self):
        volume = (self.sides[3]*np.sqrt((self.sides[0]-(self.sides[1]/2))))*self.sides[3]
        print(volume)
    def getArea(self):
        area= (self.sides[3]*np.sqrt((self.sides[0]-(self.sides[1]/2)))) + ((self.sides[0] + self.sides[1]+ self.sides[2] ) * self.sides[3])
        print(area)
    def getPerimeter(self):
        peri= (2*(self.sides[0] + self.sides[1]+ self.sides[2] ))+(3*self.sides[3])
        print(peri)
x = TrianglePrism(4)
x.entersides()
x.getVolume()
x.getArea()
x.getPerimeter()