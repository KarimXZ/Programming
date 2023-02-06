from abc import ABC,abstractmethod
class Food(ABC):
    Listlist=[]
    foodordered=[]
    debt=0
    def __init__(self,name, price):
        self.name=name
        self.price=price
        self.foodid=None
    def order(self):
        setattr(Food, 'debt', self.debt+self.price)
        print(f"The guests debt is: {Food.debt}. The foods price was:{self.price}")
        self.foodordered.append(self)
    @abstractmethod
    def AssignID():
        pass
    @staticmethod
    def totalfoodprice():
        Totalprice=0
        for i in Food.foodordered:
            Totalprice=Totalprice+i.price
        print(f"The total food price is:{Totalprice}.")
    @abstractmethod
    def AddList():
        pass


class Soup(Food):
    Souplist=[]
    def __init__(self, name, price):
        super().__init__(name, price)
        Soup.Souplist.append(self)
    def AddList():
        Food.Listlist.append(Soup.SoupList)
    def AssignID():
        j=1
        for i in Soup.Souplist:
            setattr(i, 'foodid', j)
            j=j+1
class Main(Food):
    Mainlist=[]
    def __init__(self, name, price):
        super().__init__(name, price)
        Main.Mainlist.append(self)
    def AddList():
        Food.Listlist.append(Main.Mainlist)
    def AssignID():
        j=1
        for i in Main.Mainlist:
            setattr(i, 'foodid', j)
            j=j+1
class Sweets(Food):
    Sweetlist=[]
    def __init__(self, name, price):
        super().__init__(name, price)
        Sweets.Sweetlist.append(self)
    def AddList():
        Food.Listlist.append(Sweets.Sweetlist)
    def AssignID():
        j=1
        for i in Sweets.Sweetlist:
            setattr(i, 'foodid', j)
            j=j+1
class Drinks(Food):
    Drinklist=[]
    def __init__(self, name, price):
        super().__init__(name, price)
        Drinks.Drinklist.append(self)
    def AddList():
        Food.Listlist.append(Drinks.DrinkList)
    def AssignID():
        j=1
        for i in Drinks.Drinklist:
            setattr(i, 'foodid', j)
            j=j+1
def RestaurantUI():
    a=1
    Soup.AssignID()
    Main.AssignID()
    Sweets.AssignID()
    Drinks.AssignID()
    while True:
        x=input("""Welcome to the food order system! What would you like to do?:
1-Order food
2-Return to Main menu""")
        if x=='1':
            while a==1:
                for i in Soup.Souplist:
                    print((f'{i.foodid}-{i.name}    Fiyat: {i.price}'))
                y=int(input("Which soup do you want?(0 to continue)"))
                if y==0:
                    break
                for i in Soup.Souplist:
                    if i.foodid==y:
                        i.order()
                        a=input("Do you want another?y/n")
                        if a=='y':
                            continue
                        else:
                            a=2
                    else:
                        print("This food doesn't exist")
            while a==1:
                for i in Main.Mainlist:
                    print((f'{i.foodid}-{i.name}    Fiyat: {i.price}'))
                y=int(input("Which main course do you want?(0 to continue)"))
                if y==0:
                    break
                for i in Main.Mainlist:
                    if i.foodid==y:
                        i.order()
                        a=input("Do you want another?y/n")
                        if a=='y':
                            continue
                        else:
                            a=2
                    else:
                        print("This food doesn't exist")
            while a==1:
                for i in Sweets.Sweetlist:
                    print((f'{i.foodid}-{i.name}-Diyat {i.price}'))
                y=int(input("Which soup do you want?(0 to continue)"))
                if y==0:
                    break
                for i in Sweets.Sweetlist:
                    if i.foodid==y:
                        i.order()
                        a=input("Do you want another?y/n")
                        if a=='y':
                            continue
                        else:
                            a=2
                    else:
                        print("This food doesn't exist")
            while a==1:
                for i in Drinks.Drinklist:
                    print((f'{i.foodid}-{i.name}    Fiyat: {i.price}'))
                y=int(input("Which soup do you want?(0 to continue)"))
                if y==0:
                    break
                for i in Drinks.Drinklist:
                    if i.foodid==y:
                        i.order()
                        a=input("Do you want another?y/n")
                        if a=='y':
                            continue
                        else:
                            a=2
                    else:
                        print("This food doesn't exist")
            Food.totalfoodprice()
        if x=='2':
            break
Tomato=Soup('Tomato', 10)
Steak=Main('Steak',1000)
Icecream=Sweets('Icecream', 100)
Redbull=Drinks('Redbull', 1)
RestaurantUI()