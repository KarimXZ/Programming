from abc import ABC,abstractmethod
class Sport(ABC):
    Teams=[]
    def __init__(self):
        pass
class Team(Sport):
    def __init__(self,name,game,createdate,Players=[],pwon=0,plost=0):
        self.name=name
        self.__game=game
        self.Players=[]
        self.pwon=pwon
        self.__plost=plost
        self.__createdate=createdate
        Sport.Teams.append(self)
    def addPlayer(self,Pname):
        self.Players.append(Pname)
    def Goal(self,Team2):
        self.pwon=+1
        Team2.Goalloss()
    def Goalloss(self):
        self.__plost=+1
    def PlayerList(self):
        for i in self.Players:
            print(i.name+i.surname)
    @staticmethod
    def Showscore(Team1,Team2):
        print(f"{Team1.pwon}:{Team2.pwon}")
    @classmethod
    def TeamList(cls):
        for i in cls.Teams:
            print(i.name)
class Player(Sport):
    def __init__(self,name,surname,bdate,Team,spec1='',spec2='',spec3=''):
        self.name=name
        self.surname=surname
        self.__bdate=bdate
        self.__spec1=spec1
        self.__spec2=spec2
        self.__spec3=spec3
        self.Team=Team
        for i in Sport.Teams:
            if self.Team==i.name:
                i.addPlayer(self)
    def addspecs(self):
        self.__spec1=input("Birinci ozellikligi girdiriniz")
        self.__spec2=input("Ikinici ozelligi girdiriniz")
        self.__spec3=input("Ucuncu ozelligi girdiriniz")
Volley1=Team('Tigers', "Volleyball",1999)
Volley2=Team('Lions', "Volleyball", 2005)
Volley1.Goal(Volley2)
Team.Showscore(Volley1,Volley2)
Team.TeamList()
Karim=Player('Karim', 'Bayram', 2002, 'Tigers')
Volley1.PlayerList()