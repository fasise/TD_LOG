"""la bataille navale est un jeu où le joueur essaye  d'abattre tous vaisseaux advesaires pour pouvoir gangner"""
class DestroyedError(Exception):
    pass

from typing import Tuple
from weapon import Weapon
from weapon import antisurfaces,antiair,torpilles
#classe vaise
class Vaisseau:
     #constructeur de la classe vaisseau
    def __init__(self,coordinates:Tuple,maxhits:int,weapon:Weapon):
        self.coordinates=coordinates
        self.maxhits=maxhits
        self.weapon=Weapon
    def go_to(self,x,y,z):
        self.coordinates = (x,y,z)
    def get_coordinates(self):
        return self.coordinates 
    def fire_at(self,x:int,y:int,z:int):
        if self.maxhits==0:
            raise DestroyedError
        self.armes.fire_at(x,y,z)
#Classe Cruiser héritant de la classe vaisseau  
class Cruiser(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,weapon:Weapon):
        super.__init__(self,coordinates,6,antiair())
    def go_to(self, x, y, z):
        if z==0:
            super().go_to(x,y,z)
##Classe Submarine héritant de la classe vaisseaux
class Submarine(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,weapon:Weapon):
        super.__init__(self,coordinates,2,torpilles())
    def go_to(self, x, y, z):
        if z==0 or z==-1:
            super().go_to(x,y,z)
##Classe Fregate héritant de la classe vaisseaux
class Fregate(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,weapon:Weapon):
        super.__init__(self,coordinates,5,antisurfaces())
    def go_to(self, x, y, z):
        if z==0 :
            super().go_to(x,y,z)
##Classe Destroyer héritant de la classe vaisseaux
class Destroyer(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,weapon:Weapon):
        super.__init__(self,coordinates,4,torpilles())
    def go_to(self, x, y, z):
        if z==0 :
            super().go_to(x,y,z)
##Classe Aircraft héritant de la classe vaisseaux
class Airfact(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,armes:Armes):
        super.__init__(self,coordinates,1,antisurfaces())
    def go_to(self, x, y, z):
        if z==1 :
            super().go_to(x,y,z)

