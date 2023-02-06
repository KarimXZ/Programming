class Geometry:
    def __init__(self,sidecount):
        self.sidecount=sidecount
        self.sides=[]
    def getsides(self):
        for i in range(self.sidecount):
            self.sides.append(int(input(f"{i+1}inci kenari giriniz lutfen")))
    def listsides(self):
        for i in range(len(self.sides)):
            print(f"{i+1}inci kenarin uzunlugu {self.sides[i]}'dir")
class Dikdortgen(Geometry):
    def __init__(self, sidecount=3):
        self.sidecount=sidecount
        self.sides=[]
    def getvolume(self):
        j=1
        for i in self.sides:
            j=j*i
        print(f"The volume is {j} meters cubed")
    def getsarea(self):
        area=(2*(self.sides[0]*self.sides[1]))+(2*(self.sides[1]*self.sides[2]))+(2*(self.sides[0*self.sides[2]]))
        print(f"The area is {area} meters squared")
    def getperimeter(self):
        per=(self.sides[0]+self.sides[1]+self.sides[2])*4
        print(f"The perimeter is {per} meters")
a1=Dikdortgen()
a1.getsides()
a1.listsides()
a1.getperimeter()
a1.getsarea()
a1.getvolume()